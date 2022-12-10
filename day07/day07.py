from collections import namedtuple
import sys

Command = namedtuple("Command", "cmd output")

def parse_input(input_path):
    # load input file
    cmds = []
    with open(input_path) as f:
        current_output = []
        for line in f:
            line = line[:-1]
            if line.startswith("$"):
                if len(cmds) != 0:
                    cmds[-1][1] = current_output # set output of command before
                    current_output = []

                cmds.append([line.removeprefix("$ "), []])
            else:
                current_output.append(line)

    if len(current_output) != 0:
        cmds[-1][1] = current_output # set output of last command

    return [Command(cmd, output) for cmd, output in cmds]

class FileTree():
    def __init__(self, name, *children, size=None) -> None:
        self.name = name
        self.children = children

        self.is_file = len(children) == 0

        # if no size is given, sum up the children
        self.size = size or sum([c.size for c in self.children])

    @classmethod
    def from_command_list(cls, cmds: list[Command], name='/', start_index=0):
        # first cmd should be the cd command into the current dir
        index = start_index + 1
        # print(cmds[index])
        if cmds[index].cmd == "ls":
            children = []
            for entry in cmds[index].output:
                split = entry.split()
                if split[0] == "dir":
                    child_name = split[1]
                    sub_tree, index = FileTree.from_command_list(
                            cmds, name=child_name, start_index=index+1)
                    children.append(sub_tree)
                else:
                    child_size = int(split[0])
                    child_name = split[1]

                    children.append(FileTree(child_name, size=child_size))

            # return tree and last index + 1 to skip the 'cd ..'
            return FileTree(name, *children), index + 1
        else:
            raise ValueError("error!")

def recurse(t: FileTree, func):
    for c in t.children:
        func(c)
        recurse(c, func)

def sum_of_under_100k(tree, max_size: int):
    """
        Recurse through the tree and add up all dir sizes over a given size.
    """
    sum = 0

    # a function we pass to the recurse function
    def add_if_small_dir(t):
        if t.size <= max_size and not t.is_file:
            nonlocal sum # not clean, I know, I know
            sum += t.size

    recurse(tree, add_if_small_dir)

    return sum

def free_memory(tree: FileTree, total: int, needed: int):
    """
        Free up just as much memory as needed by deleting one directory.
        Returns the smallest dir in the tree that has at least the size of the needed space
    """
    current_used_space = tree.size
    unused = total - current_used_space
    need_to_free = needed - unused

    if need_to_free <= 0:
        return None

    dirs_big_enough = []

    # a function we pass to the recurse function
    def add_if_big_enough(t: FileTree):
        if t.size >= need_to_free and not t.is_file:
            nonlocal dirs_big_enough # not clean, I know, I know
            dirs_big_enough.append(t.size)

    recurse(tree, add_if_big_enough)

    return min(dirs_big_enough)


if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    cmds = parse_input(input_file_path)
    tree, _ = FileTree.from_command_list(cmds)

    ANSWER = sum_of_under_100k(tree, max_size=100000)
    print(f"Task 1: {ANSWER}")

    ANSWER = free_memory(tree, total=70000000, needed=30000000)
    print(f"Task 2: {ANSWER}")



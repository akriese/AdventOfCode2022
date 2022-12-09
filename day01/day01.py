import sys

def parse_input(input_path):
    # load input file
    data = []
    with open(input_path) as f:
        for line in f:
            data.append(line[:-1])

    elves = []
    running_group = []
    for s in data:
        if s == "":
            elves.append(running_group)
            running_group = []
        else:
            running_group.append(int(s))

    elves.append(running_group)

    return elves

def max_sum(elves):
    return max([sum(elf) for elf in elves])

def top3_sum(elves):
    sums = [sum(elf) for elf in elves]
    sums.sort()
    return sum(sums[-3:])

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    elves = parse_input(input_file_path)
    ANSWER = max_sum(elves)
    print(ANSWER)

    elves = parse_input(input_file_path)
    ANSWER = top3_sum(elves)
    print(ANSWER)

import sys
from dataclasses import dataclass

import numpy as np

@dataclass
class TreeInfo:
    height: int
    visible: bool

def parse_input(input_path):
    # load input file
    tree_rows = []
    with open(input_path) as f:
        for line in f:
            tree_rows.append([int(height) for height in line[:-1]])

    return tree_rows

def number_of_visible_trees(tree_rows: list[list[int]]):
    """

    """
    n = len(tree_rows)
    matrix = []
    for row in tree_rows:
        matrix.append([TreeInfo(height, False) for height in row])

    for _ in range(4):
        rotated = list(zip(*matrix[::-1]))

        for row_idx in range(n):
            running_max = -1
            for tree in rotated[row_idx]:
                if tree.height > running_max:
                    running_max = tree.height
                    tree.visible = True

                    # no tree in this row will be visible from this side
                    if running_max == 9:
                        break

        matrix = rotated

    count = 0
    for row in matrix:
        for x in row:
            count += 1 if x.visible else 0

    return count

def dist(height, line: list[int]):
    """
        Helper function. Returns the number of trees the given tree (height)
        can overlook until its view is blocked.
        line must be a list of heights where the first height is the one
        closest to the tree that is currently checked.
    """
    if len(line) == 0:
        return 0 # distance to the edge

    if line[0] >= height:
        return 1 # distance to the neighbor tree

    # recurse on the tail of the list
    return 1 + dist(height, line[1:])


def highest_scenic_score(tree_rows: list[list[int]]):
    """
        Get the scenic score for each inner tree and return the highest.
        The scenic score is computed by looking in all four directions from a
        tree and finding the distance to the edge or the next tree which is at
        least as high as the tree itself.
    """

    matrix = np.array(tree_rows)
    maximum_score = 0
    n = len(matrix)

    for i in range(1, n-1):
        for j in range(1, n-1):
            scenic_score = 1
            this_height = matrix[i, j]

            # no edge cases needed (eg where j-1 is -1), as we exclude
            # the outermost rows and columns from the calculation
            # check right
            scenic_score *= dist(this_height, matrix[i, j+1:])

            # check left
            scenic_score *= dist(this_height, matrix[i, j-1::-1])

            # check up
            scenic_score *= dist(this_height, matrix[i-1::-1, j])

            # check down
            scenic_score *= dist(this_height, matrix[i+1:, j])

            maximum_score = max(maximum_score, scenic_score)

    return maximum_score


if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    tree_rows = parse_input(input_file_path)

    ANSWER = number_of_visible_trees(tree_rows)
    print(f"Task 1: {ANSWER}")

    ANSWER = highest_scenic_score(tree_rows)
    print(f"Task 2: {ANSWER}")



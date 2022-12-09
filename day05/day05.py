#!/usr/bin/env python
# coding: utf-8

import sys

import numpy as np

def parse_input(input_path) -> tuple[list, list]:
    # load input file
    data = []
    with open(input_path) as f:
        for line in f:
            data.append(line[:-1])

    # take lines that are used for the stacks
    input_stack_lines = []
    for line in data:
        if line == "":
            break
        input_stack_lines.append(line)

    # the rest of the lines are moves
    moves = data[len(input_stack_lines)+1: ]

    # transform stack columns to lines. Save as numpy matrix
    rev_input = input_stack_lines[-2::-1]
    rev_input = [[x for x in line] for line in rev_input]
    rev_input = np.array(rev_input)

    stacks = []
    for line in rev_input.T:
        # only some lines have information
        if line[0] not in ["[", "]", " "]:
            stack = ''.join(line.tolist()).strip() # strip spaces from end of stacks
            stacks.append([c for c in stack]) # stack as list of chars, to be mutable

    # parse moves which are of shape "move <number_of_items> from <from_stack> to <to_stack>"
    moves = [move.split(" ")[1::2] for move in moves]

    # parse chars to ints
    moves = [[int(x) for x in move] for move in moves]

    return stacks, moves


def crate_mover_9000(stacks, moves):
    # main loop for moving around cargo
    for n, fr, to in moves:
        # pop n times from from_stack and append to to_stack
        for _ in range(n):
            stacks[to-1].append(stacks[fr-1].pop())

    return [stack[-1] for stack in stacks]

def crate_mover_9001(stacks, moves):
    # main loop for moving around cargo
    for n, fr, to in moves:
        # move last n elements from from_stack in same order to to_stack
        stacks[to-1].extend(stacks[fr-1][-n:])
        stacks[fr-1] = stacks[fr-1][:-n]

    return [stack[-1] for stack in stacks]

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    stacks, moves = parse_input(input_file_path)
    ANSWER = crate_mover_9000(stacks, moves)
    print("".join(ANSWER))

    stacks, moves = parse_input(input_file_path)
    ANSWER = crate_mover_9001(stacks, moves)
    print("".join(ANSWER))


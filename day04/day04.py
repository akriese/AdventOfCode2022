#!/usr/bin/env python
# coding: utf-8

import sys

def parse_input(input_path) -> list[tuple]:
    # load input file
    data = []
    with open(input_path) as f:
        for line in f:
            data.append(line[:-1])

    # take lines that are used for the stacks
    def to_section(range_):
        numbers = range_.split("-")
        return (int(numbers[0]), int(numbers[1]))

    section_pairs = []
    for line in data:
        ranges = line.split(",")
        section_pairs.append((to_section(ranges[0]), to_section(ranges[1])))

    return section_pairs


def inclusive_section_pairs(section_pairs):
    # main loop for moving around cargo
    count = 0
    for r1, r2 in section_pairs:
        if (r1[0] <= r2[0] and r1[1] >= r2[1] or
            r1[0] >= r2[0] and r1[1] <= r2[1]):
            count += 1

    return count

def overlapping_sections(section_pairs):
    # main loop for moving around cargo
    count = 0
    for r1, r2 in section_pairs:
        if (r1[0] <= r2[0] and r1[1] >= r2[0] or
            r2[0] <= r1[0] and r2[1] >= r1[0]):
            count += 1

    return count

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    section_pairs = parse_input(input_file_path)
    ANSWER = inclusive_section_pairs(section_pairs=section_pairs)
    print(ANSWER)

    section_pairs = parse_input(input_file_path)
    ANSWER = overlapping_sections(section_pairs=section_pairs)
    print(ANSWER)


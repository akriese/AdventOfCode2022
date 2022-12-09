import sys

def parse_input(input_path):
    # load input file
    rucksacks = []
    with open(input_path) as f:
        for line in f:
            rucksacks.append(line[:-1])

    return rucksacks

def get_score(item):
    """ Return the score of a rucksack item """
    # if letter is lowercase
    if item.islower():
        return ord(item) - 97 + 1
    else: # if it is upper case, we add 26 to the score
        return ord(item) - 65 + 1 + 26

def sum_rucksack_both_comps(rucksacks):
    """
        Calculates the total sum of scores of the items
        that are in both compartments of a rucksack
    """
    sum = 0

    for rucksack in rucksacks:
        n = len(rucksack)
        left, right = set(rucksack[:n//2]), set(rucksack[n//2:])

        # only select intersection of the sets of items on  the compartments
        in_both = left.intersection(right)

        for el in in_both:
            sum += get_score(el)

    return sum

def sum_of_group_badges(rucksacks):
    """ Return the sum of elf badges in groups of 3 """
    group_size = 3
    sum = 0

    for i in range(len(rucksacks) // group_size):
        r1, r2, r3 = rucksacks[i*group_size : (i+1)*group_size]

        for el in r1:
            if el in r2 and el in r3:
                sum += get_score(el)
                break

    return sum

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    games = parse_input(input_file_path)
    ANSWER = sum_rucksack_both_comps(games)
    print(f"Task 1: {ANSWER}")

    games = parse_input(input_file_path)
    ANSWER = sum_of_group_badges(games)
    print(f"Task 2: {ANSWER}")



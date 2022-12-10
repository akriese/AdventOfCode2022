import sys

def parse_input(input_path):
    # load input file
    signals = []
    with open(input_path) as f:
        for line in f:
            signals.append(line[:-1])

    return signals

def start_of_message(signal, k):
    """
        Returns the index after the first k-substring which only consists
        of distinct characters.
    """
    n = len(signal)

    # sliding window of size k over signal
    win = signal[:k]

    i = k
    while i < n:
        # let the set class remove duplicates ;)
        if len(win) == len(list(set(win))):
            return i

        # this could be implemented more efficiently to avoid checking
        # windows that we know can not work due to former information
        # eg.: signal: 'abcbccbda' after checking 'abcb' we could make a
        # leap two indices ahead instead of one to avoid having both b's in
        # the next substring again

        # ANYWAYS, I was too lazy and the running time for the input is fine.
        i += 1
        win = signal[i-k : i]

    return i



if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    signal = parse_input(input_file_path)[0]
    ANSWER = start_of_message(signal, k=4)
    print(f"Task 1: {ANSWER}")

    signal = parse_input(input_file_path)[0]
    ANSWER = start_of_message(signal, k=14)
    print(f"Task 2: {ANSWER}")



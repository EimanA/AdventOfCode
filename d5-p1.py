# D5 - P1 Answer = 5294

import re
from collections import defaultdict


def overlaps_num(lines):
    d = defaultdict(lambda: 0)
    for line in lines:
        if line[0] == line[2]:
            start = min([line[1], line[3]])
            end = max([line[1], line[3]])
            for i in range(start, end + 1):
                d[line[0], i] += 1
        elif line[1] == line[3]:
            start = min([line[0], line[2]])
            end = max([line[0], line[2]])
            for i in range(start, end + 1):
                d[i, line[1]] += 1

    counter = 0
    for value in d.values():
        if value > 1:
            counter += 1

    return counter


def main():
    q5_file = open('d5_input.txt', 'r')
    lines = q5_file.readlines()

    lines = [list(map(int, (re.split(' -> |,', line.strip())))) for line in lines]

    print(f"final result = {overlaps_num(lines)}")


if __name__ == "__main__":
    main()

# D2 - P2 Answer = 1954293920

def pos_calculator(lines):
    lines = [line.strip().split() for line in lines]

    horizontal_pos = 0
    depth = 0
    aim = 0

    for line in lines:
        if line[0] == "forward":
            horizontal_pos += int(line[1])
            depth += aim * int(line[1])
        elif line[0] == "down":
            aim += int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])
    return horizontal_pos * depth


def main():
    q2_file = open('d2_input.txt', 'r')
    lines = q2_file.readlines()
    print(f"final result = {pos_calculator(lines)}")


if __name__ == "__main__":
    main()

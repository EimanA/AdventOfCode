# Q2 Answer = 1103

def inc_counter(lines):
    lines = list(map(int, [line.strip() for line in lines]))
    count = 0
    prev_sum = lines[0] + lines[1] + lines[2]
    print(f"{prev_sum}  (N/A - no previous sum)")
    for i in range(1, len(lines)-2):
        this_sum = lines[i] + lines[i+1] + lines[i+2]
        if this_sum > prev_sum:
            result = "(increased)"
            count += 1
        else:
            result = "(decreased)"
        prev_sum = this_sum
        print(f"{this_sum}  {result}")
    return count


def main():
    q1_file = open('q1_input.txt', 'r')
    lines = q1_file.readlines()
    print(f"final result = {inc_counter(lines)}")


if __name__ == "__main__":
    main()

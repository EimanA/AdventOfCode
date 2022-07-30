# D1-P1 Answer = 1139

def inc_counter(lines):
    lines = list(map(int, [line.strip() for line in lines]))
    count = 0
    print(f"{lines[0]}  (N/A - no previous measurement)")
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            result = "(increased)"
            count += 1
        else:
            result = "(decreased)"
        print(f"{lines[i]}  {result}")
    return count


def main():
    q1_file = open('d1_input.txt', 'r')
    lines = q1_file.readlines()
    print(f"final result = {inc_counter(lines)}")


if __name__ == "__main__":
    main()

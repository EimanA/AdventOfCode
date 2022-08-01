# D7 - P1 Answer = 364898

def find_cheapest(line):
    crab_list = list(map(int, [num for num in line.split(',')]))
    min_needed_fuel = sum(crab_list)

    for pos in range(min(crab_list), max(crab_list) + 1):
        needed_fuel = sum([abs(pos-num) for num in crab_list])
        if needed_fuel < min_needed_fuel:
            min_needed_fuel = needed_fuel

    return min_needed_fuel


def main():
    q5_file = open('d7_input.txt', 'r')
    line = q5_file.readline()

    print(f"final result = {find_cheapest(line)}")


if __name__ == "__main__":
    main()

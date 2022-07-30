# D3 - P2 Answer = 4406844

def filter_rates(i, rate, mode):
    rate_zero = []
    rate_one = []
    for item in rate:
        if item[i] == '0':
            rate_zero.append(item)
        else:
            rate_one.append(item)
    if len(rate_zero) > len(rate_one):
        rate = rate_zero if mode == "O2" else rate_one
    else:
        rate = rate_one if mode == "O2" else rate_zero
    return rate


def gamma_epsilon(lines):
    lines = [line.strip() for line in lines]

    oxygen_rate = lines
    co2_rate = lines
    i = 0
    
    while len(oxygen_rate) != 1 or len(co2_rate) != 1:
        if len(oxygen_rate) != 1:
            oxygen_rate = filter_rates(i, oxygen_rate, "O2")
        if len(co2_rate) != 1:
            co2_rate = filter_rates(i, co2_rate, "CO2")
        i += 1

    oxygen = int("".join(oxygen_rate), 2)
    co2 = int("".join(co2_rate), 2)

    return oxygen * co2


def main():
    q3_file = open('d3_input.txt', 'r')
    lines = q3_file.readlines()
    print(f"final result = {gamma_epsilon(lines)}")


if __name__ == "__main__":
    main()

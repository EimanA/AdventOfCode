# D3 - P1 Answer = 3687446


def gamma_epsilon(lines):
    lines = [line.strip() for line in lines]

    gamma_rate = []
    epsilon_rate = []

    for i in range(len(lines[0])):
        gamma_rate.append('0' if max(['0', '1'], key=[line[i] for line in lines].count) == '0' else '1')
        epsilon_rate.append('0' if gamma_rate[i] == '1' else '1')

    gamma = int("".join(gamma_rate), 2)
    epsilon = int("".join(epsilon_rate), 2)

    return gamma * epsilon


def main():
    q3_file = open('d3_input.txt', 'r')
    lines = q3_file.readlines()
    print(f"final result = {gamma_epsilon(lines)}")


if __name__ == "__main__":
    main()

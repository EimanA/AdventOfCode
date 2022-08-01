# D6 - P1 Answer = 383160

from collections import deque


def DAYS():
    return 80


def lanternfish(line):
    fish_list = list(map(int, [num for num in line.split(',')]))

    list_of_last_nine_days = [len(fish_list)]
    for day in range(1, 9):
        fish_list_temp = fish_list
        for i in range(len(fish_list)):
            if fish_list_temp[i] == 0:
                fish_list_temp.append(8)
                fish_list_temp[i] = 6
            else:
                fish_list_temp[i] -= 1
        list_of_last_nine_days.append(len(fish_list_temp))
        fish_list = fish_list_temp

    if DAYS() < 9:
        return list_of_last_nine_days[DAYS()]

    list_of_last_nine_days = deque(list_of_last_nine_days)
    for day in range(9, DAYS() + 1):
        list_of_last_nine_days.append(list_of_last_nine_days.popleft() + list_of_last_nine_days[1])
    return list_of_last_nine_days.pop()


def main():
    q5_file = open('d6_input.txt', 'r')
    line = q5_file.readline()

    print(f"final result = {lanternfish(line)}")


if __name__ == "__main__":
    main()

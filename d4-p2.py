# D4 - P2 Answer = 21184

import re


def BOARD_SIZE():
    return 5


def is_bingo(board):
    for i in range(0, len(board), BOARD_SIZE()):
        if board[i:i+BOARD_SIZE()].count(-1) == 5:
            return True

    for i in range(0, BOARD_SIZE()):
        if [board[i+j] for j in range(0, len(board), BOARD_SIZE())].count(-1) == 5:
            return True
    return False


def bingo_sub(lines, drawn_nums):
    boards = []
    for i in range(0, (len(lines))//BOARD_SIZE()):
        boards.append([])
        first_index = BOARD_SIZE() * (i-1)
        for j in range(first_index, first_index + BOARD_SIZE()):
            boards[i].extend(lines[j])

    for num in drawn_nums:
        i = 0
        while i <= len(boards) - 1:
            boards[i] = [-1 if number == num else number for number in boards[i]]
            if is_bingo(boards[i]):
                print("removed", i, num, boards[i])
                if len(boards) == 1:
                    return num * (sum(boards[0]) + boards[0].count(-1))
                boards.pop(i)
                continue
            i += 1


def main():
    q4_file = open('d4_input.txt', 'r')
    lines = q4_file.readlines()
    lines = [list(map(int, (re.split('  | |,', line.strip())))) for line in lines if line != '\n']
    drawn_nums = lines[0]

    print(f"final result = {bingo_sub(lines[1:], drawn_nums)}")


if __name__ == "__main__":
    main()

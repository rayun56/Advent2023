# helper functions
def get_number(lines: list[str], i: int, j: int) -> (int, list[(int, int)]):
    """ Finds the number (up to 3 digits) at the given location
    Returns a tuple with the number and a list of coordinates where the number is """

    num = lines[i][j]
    coords = [(i, j)]

    # start with search left
    if j > 0 and lines[i][j - 1].isdigit():
        num = lines[i][j - 1] + num
        coords.append((i, j - 1))
        if j > 1 and lines[i][j - 2].isdigit():
            num = lines[i][j - 2] + num
            coords.append((i, j - 2))

    # now search right
    if j < len(lines[i]) - 1 and lines[i][j + 1].isdigit():
        num = num + lines[i][j + 1]
        coords.append((i, j + 1))
        if j < len(lines[i]) - 2 and lines[i][j + 2].isdigit():
            num = num + lines[i][j + 2]
            coords.append((i, j + 2))

    return int(num), coords


def search_number(lines: list[str], col: int, row: int) -> list[int]:
    """ Given the coordinates of a symbol, find all numbers around it """

    nums = []
    ignore = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (col + i, row + j) not in ignore and lines[col + i][row + j].isdigit():
                num, bad = get_number(lines, col + i, row + j)
                nums.append(num)
                ignore.extend(bad)

    return nums


def part1():
    lines = []
    with open("../inputs/day3.txt", "r") as f:
        # strip the newline characters off
        lines = [x.strip() for x in f.readlines()]

    # remember in this case coordinates are lines[col][row]
    sum_of_parts = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.' and not lines[i][j].isdigit():
                symbol = lines[i][j]
                nums = search_number(lines, i, j)
                sum_of_parts += sum(nums)

    print(sum_of_parts)


def part2():
    lines = []
    with open("../inputs/day3.txt", "r") as f:
        # strip the newline characters off
        lines = [x.strip() for x in f.readlines()]

    # remember in this case coordinates are lines[col][row]
    sum_of_ratios = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                nums = search_number(lines, i, j)
                if len(nums) > 1:
                    product = 1
                    for x in nums:
                        product *= x
                    sum_of_ratios += product

    print(sum_of_ratios)


if __name__ == "__main__":
    part1()
    part2()

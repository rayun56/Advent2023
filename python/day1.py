"""Advent of Code 2023 Day 1"""


def part1():
    with open("../inputs/day1.txt") as f:
        data = f.read().splitlines()
    sum = 0
    for line in data:
        first = ""
        last = ""
        for c in line:
            if c.isdigit():
                first = c
                break

        for c in reversed(line):
            if c.isdigit():
                last = c
                break

        sum += int(first + last)

    print(sum)


def part2():
    with open("../inputs/day1.txt") as f:
        data = f.read().splitlines()
    sum = 0
    values = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for line in data:
        first = ""
        findex = len(line)
        last = ""
        lindex = 0
        for key, value in values.items():
            try:
                findex = line.index(key) if line.index(key) < findex else findex
                first = values[key] if line.index(key) <= findex else first
            except ValueError:
                continue
        for key, value in values.items():
            try:
                lindex = line.rindex(key) if line.rindex(key) > lindex else lindex
                last = values[key] if line.rindex(key) >= lindex else last
            except ValueError:
                continue
        for i in range(findex):
            if line[i].isdigit():
                first = line[i]
                break
        for i in reversed(range(lindex, len(line))):
            if line[i].isdigit():
                last = line[i]
                break
        sum += int(first + last)


    print(sum)


if __name__ == "__main__":
    part1()
    part2()

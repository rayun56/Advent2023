def parse_game(game: str) -> list[str]:
    winning, selected = game.split(":")[1].split("|")
    winning = [x for x in winning.split(" ") if x]
    selected = [x for x in selected.split(" ") if x]
    winning_nums = list(set(winning) & set(selected))
    return winning_nums


def part1():
    with open("../inputs/day4.txt", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    total_points = 0

    for game in lines:
        winning_nums = parse_game(game)

        total_points += 0 if len(winning_nums) == 0 else 1 if len(winning_nums) == 1 else pow(2, len(winning_nums) - 1)

    print(total_points)


def part2():
    with open("../inputs/day4.txt", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    mults = [1 for x in range(len(lines))]

    for i in range(len(lines)):
        winning_nums = parse_game(lines[i])
        mult = mults[i]
        for j in range(1, len(winning_nums) + 1):
            mults[i + j] += mult

    print(sum(mults))


if __name__ == "__main__":
    part1()
    part2()

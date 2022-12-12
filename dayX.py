DAY = 0


def input(example=True):

    if example:
        filename = f"input/day{DAY}-example.txt"
    else:
        filename = f"input/day{DAY}-actual.txt"

    return [line.strip() for line in open(filename).readlines()]


def part_one(input):
    result = 0

    return result


def part_two(input):
    result = 0

    return result


print(f"Day {DAY}:\n")

print(f"Part One: {part_one(input())}")
print(f"Part One: {part_two(input())}")

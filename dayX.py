DAY = 0

def input(example = True):
    if example:
        return open(f"input/day{DAY}-example.txt").readlines
    else:
        return open(f"input/day{DAY}-actual.txt").readlines

def part_one():
    result = 0

    return result   

def part_two():
    result = 0

    return result

print(f"Day {DAY}:\n")

print(f"Part One: {part_one(input())}")
print(f"Part One: {part_two(input())}")

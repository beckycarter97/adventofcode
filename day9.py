# --- Day 9: Rope Bridge ---

# This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

# It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

# You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

# Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

# Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

# Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

# ....
# .TH.
# ....

# ....
# .H..
# ..T.
# ....

# ...
# .H. (H covers T)
# ...
# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

# .....    .....    .....
# .TH.. -> .T.H. -> ..TH.
# .....    .....    .....

# ...    ...    ...
# .T.    .T.    ...
# .H. -> ... -> .T.
# ...    .H.    .H.
# ...    ...    ...
# Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

# .....    .....    .....
# .....    ..H..    ..H..
# ..H.. -> ..... -> ..T..
# .T...    .T...    .....
# .....    .....    .....

# .....    .....    .....
# .....    .....    .....
# ..H.. -> ...H. -> ..TH.
# .T...    .T...    .....
# .....    .....    .....
# You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

# For example:

# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

# == Initial State ==

# ......
# ......
# ......
# ......
# H.....  (H covers T, s)

# == R 4 ==

# ......
# ......
# ......
# ......
# TH....  (T covers s)

# ......
# ......
# ......
# ......
# sTH...

# ......
# ......
# ......
# ......
# s.TH..

# ......
# ......
# ......
# ......
# s..TH.

# == U 4 ==

# ......
# ......
# ......
# ....H.
# s..T..

# ......
# ......
# ....H.
# ....T.
# s.....

# ......
# ....H.
# ....T.
# ......
# s.....

# ....H.
# ....T.
# ......
# ......
# s.....

# == L 3 ==

# ...H..
# ....T.
# ......
# ......
# s.....

# ..HT..
# ......
# ......
# ......
# s.....

# .HT...
# ......
# ......
# ......
# s.....

# == D 1 ==

# ..T...
# .H....
# ......
# ......
# s.....

# == R 4 ==

# ..T...
# ..H...
# ......
# ......
# s.....

# ..T...
# ...H..
# ......
# ......
# s.....

# ......
# ...TH.
# ......
# ......
# s.....

# ......
# ....TH
# ......
# ......
# s.....

# == D 1 ==

# ......
# ....T.
# .....H
# ......
# s.....

# == L 5 ==

# ......
# ....T.
# ....H.
# ......
# s.....

# ......
# ....T.
# ...H..
# ......
# s.....

# ......
# ......
# ..HT..
# ......
# s.....

# ......
# ......
# .HT...
# ......
# s.....

# ......
# ......
# HT....
# ......
# s.....

# == R 2 ==

# ......
# ......
# .H....  (H covers T)
# ......
# s.....

# ......
# ......
# .TH...
# ......
# s.....
# After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

# ..##..
# ...##.
# .####.
# ....#.
# s###..
# So, there are 13 positions the tail visited at least once.

# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

DAY = 9


class Location:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def move_left(self):
        return Location(self.row, self.col - 1)

    def move_right(self):
        return Location(self.row, self.col + 1)

    def move_up(self):
        return Location(self.row + 1, self.col)

    def move_down(self):
        return Location(self.row - 1, self.col)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def __eq__(self, other) -> bool:
        return type(other) == Location and self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    def __str__(self) -> str:
        return f"Location({self.row},{self.col})"


def input(example=True):

    if example:
        filename = f"input/day{DAY}-example.txt"
    else:
        filename = f"input/day{DAY}-actual.txt"

    return [line.strip() for line in open(filename).readlines()]


def is_touching(head: Location, tail: Location):
    return (head.row <= tail.row + 1) and (head.row >= tail.row - 1) and (head.col <= tail.col + 1) and (head.col >= tail.col - 1)


def update_tail_pos(head: Location, tail: Location) -> Location:
    if is_touching(head, tail):
        return tail

    # Same row
    if head.row == tail.row:
        if head.col == tail.col + 2:
            return tail.move_right()
        elif head.col == tail.col - 2:
            return tail.move_left()
        else:
            print(f"Confused by head {head}, tail {tail}")
    # Same column
    elif head.col == tail.col:
        if head.row == tail.row + 2:
            return tail.move_up()
        elif head.row == tail.row - 2:
            return tail.move_down()
        else:
            print(f"Confused by head {head}, tail {tail}")
    else:
        if head.row > tail.row:
            tail = tail.move_up()
        elif head.row < tail.row:
            tail = tail.move_down()

        if head.col > tail.col:
            tail = tail.move_right()
        elif head.col < tail.col:
            tail = tail.move_left()

        return tail
    if not is_touching(head, tail):
        print("Error, this did not go right")


def part_one(input):

    # bottom left corner, row then column - higher row indexes are up, higher column indexes are left
    head = Location(0, 0)
    tail = Location(0, 0)
    visited = set()

    for move in input:
        direction = move[0]
        steps = int(move[2:])

        if direction == 'R':
            def change(head): return head.move_right()
        if direction == 'L':
            def change(head): return head.move_left()
        if direction == 'U':
            def change(head): return head.move_up()
        if direction == 'D':
            def change(head): return head.move_down()

        for x in range(steps):
            head = change(head)
            tail = update_tail_pos(head, tail)

            visited.add(tail)

    result = len(visited)

    return result


def part_two(input, num_knots=10):
    knot_positions = [Location(0, 0) for i in range(num_knots)]
    visited = set()

    for move in input:
        direction = move[0]
        steps = int(move[2:])

        if direction == 'R':
            def change(head) -> Location: return head.move_right()
        if direction == 'L':
            def change(head) -> Location: return head.move_left()
        if direction == 'U':
            def change(head) -> Location: return head.move_up()
        if direction == 'D':
            def change(head) -> Location: return head.move_down()

        for x in range(steps):
            # Update all knots
            for i, knot in enumerate(knot_positions):
                if i == 0:
                    new_knot = change(knot)
                else:
                    new_knot = update_tail_pos(knot_positions[i-1], knot)

                knot_positions[i] = new_knot

            visited.add(knot_positions[-1])

    return len(visited)


print(f"Day {DAY}:\n")

print(f"Part One: {part_one(input(example=False))}")
print(f"Part One: {part_two(input(example=False))}")

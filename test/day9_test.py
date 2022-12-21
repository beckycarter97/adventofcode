import unittest
from day9 import *


class Day9Tests(unittest.TestCase):
    def test_example_part_one(self):
        self.assertEqual(part_one(input(example=True)), 13)

    def test_actual_part_one(self):
        self.assertEqual(part_one(input(example=False)), 6044)

    def test_example_part_two(self):
        self.assertEqual(part_two(input(example=True), 10), 1)
        self.assertEqual(
            part_two(["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"], 10), 36)

    def test_part_one_using_part_two(self):
        self.assertEqual(part_two(input(example=True), 2), 13)

    def test_is_touching_overlap(self):
        self.assertTrue(is_touching(Location(0, 0), Location(0, 0)))

    def test_is_touching_side_by_side(self):
        self.assertTrue(is_touching(Location(0, 0), Location(0, 1)))
        self.assertTrue(is_touching(Location(0, 1), Location(0, 0)))
        self.assertTrue(is_touching(Location(0, 0), Location(1, 0)))
        self.assertTrue(is_touching(Location(1, 0), Location(0, 0)))

    def test_is_touching_diagonal(self):
        self.assertTrue(is_touching(Location(0, 0), Location(1, 1)))
        self.assertTrue(is_touching(Location(0, 2), Location(1, 1)))
        self.assertTrue(is_touching(Location(2, 2), Location(1, 1)))
        self.assertTrue(is_touching(Location(2, 0), Location(1, 1)))

    def test_update_tail_pos_sideways(self):
        self.assertEqual(update_tail_pos(
            Location(0, 2), Location(0, 0)), Location(0, 1))
        self.assertEqual(update_tail_pos(
            Location(0, 2), Location(0, 4)), Location(0, 3))
        self.assertEqual(update_tail_pos(
            Location(2, 0), Location(0, 0)), Location(1, 0))
        self.assertEqual(update_tail_pos(
            Location(2, 0), Location(4, 0)), Location(3, 0))

    def test_update_tail_pos_diagonal(self):
        self.assertEqual(update_tail_pos(
            Location(0, 0), Location(2, 2)), Location(1, 1))
        self.assertEqual(update_tail_pos(
            Location(3, 2), Location(1, 1)), Location(2, 2))
        self.assertEqual(update_tail_pos(
            Location(2, 3), Location(1, 1)), Location(2, 2))

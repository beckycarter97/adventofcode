import unittest
from day6 import part_one, part_two


class Day6Tests(unittest.TestCase):
    def test_first_eg(self):
        string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(part_one(string), 7)
        self.assertEqual(part_two(string), 19)

    def test_second(self):
        string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(part_one(string), 5)
        self.assertEqual(part_two(string), 23)

    def test_third(self):
        string = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(part_one(string), 6)
        self.assertEqual(part_two(string), 23)

    def test_fourth(self):
        string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(part_one(string), 10)
        self.assertEqual(part_two(string), 29)

    def test_fifth(self):
        string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(part_one(string), 11)
        self.assertEqual(part_two(string), 26)

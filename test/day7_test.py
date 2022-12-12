import unittest
from day7 import part_one, input, process_terminal_output

class Day7Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(part_one(input(example=True)), 95_437)

    def test_size(self):
        dir = process_terminal_output(input(example=True))

        assert dir.size() == 48_381_165

        assert dir.find_directory('e').size() == 584
        assert dir.find_directory('a').size() == 94_853
        assert dir.find_directory('d').size() == 24_933_642

    def test_sum_size(self):
        dir = process_terminal_output(input(example=True))

        a = dir.find_directory('a')

        assert a.sum_of_small_dirs(100_000) == 95437

        d = dir.find_directory('d')

        assert d.sum_of_small_dirs(100_000) == 0

    def test_find_small_dirs(self):
        dir = process_terminal_output(input(example=True))

        list = dir.find_small_dirs()

        print(list)

        assert len(list) ==2


    def test_day_7_desc(self):
        dir = process_terminal_output(input(example=True))
        
        exp = """
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
        """.strip().split('\n')

        print(exp)

        self.assertEqual(dir.describe(),exp)

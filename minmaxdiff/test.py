import unittest
from min_max_diff import min_max_diff

class MinMaxDiff(unittest.TestCase):

    def test_empty_list(self):
        list_of_nums = []
        self.assertEqual(min_max_diff(list_of_nums), 0)

if __name__ == '__main__':
    unittest.main()

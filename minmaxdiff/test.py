import unittest
from min_max_diff import min_max_diff

class MinMaxDiff(unittest.TestCase):

    def test_empty_list(self):
        list_of_nums = [ ]
        self.assertEqual(min_max_diff(list_of_nums), 0)

    def test_one_list_item(self):
        list_of_nums = [1]
        self.assertEqual(min_max_diff(list_of_nums), 0)

    def test_(self):
        list_of_nums = [5, 6, 7, 8]
        self.assertEqual(min_max_diff(list_of_nums), 3)

if __name__ == '__main__':
    unittest.main()

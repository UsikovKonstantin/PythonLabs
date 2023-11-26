import unittest
from sort import *


class TestGenerate(unittest.TestCase):
    def test_generate_list(self):
        n = 1000
        min = 0
        max = 100
        lst = generate_list(n, min, max)
        for item in lst:
            self.assertTrue(min <= item <= max)
        self.assertTrue(len(lst) == n)

    def test_generate_list2(self):
        n = 1000
        min = 100
        max = 0
        self.assertRaises(ValueError, generate_list, n, min, max)

    def test_generate_list3(self):
        n = 1000
        min = 10
        max = 10
        lst = generate_list(n, min, max)
        for item in lst:
            self.assertTrue(min <= item <= max)
        self.assertTrue(len(lst) == n)

    def test_generate_list4(self):
        n = 0
        min = 0
        max = 0
        lst = generate_list(n, min, max)
        self.assertTrue(lst == [])

    def test_generate_list5(self):
        n = -10
        min = 0
        max = 0
        lst = generate_list(n, min, max)
        self.assertTrue(lst == [])


class TestSort(unittest.TestCase):
    def test_quick_sort(self):
        inp = [4, 5, 2, 3, 1]
        lst = quick_sort(inp)
        self.assertTrue(lst == [1, 2, 3, 4, 5])

    def test_quick_sort2(self):
        inp = [1, 2, 3, 4, 5]
        lst = quick_sort(inp)
        self.assertTrue(lst == [1, 2, 3, 4, 5])

    def test_quick_sort3(self):
        inp = [5, 4, 3, 2, 1]
        lst = quick_sort(inp)
        self.assertTrue(lst == [1, 2, 3, 4, 5])

    def test_quick_sort4(self):
        inp = [1, 1, 1, 1, 1]
        lst = quick_sort(inp)
        self.assertTrue(lst == [1, 1, 1, 1, 1])

    def test_quick_sort5(self):
        inp = [4, 5, 2, 3, 1]
        lst = quick_sort(inp, True)
        self.assertTrue(lst == [5, 4, 3, 2, 1])

    def test_quick_sort6(self):
        inp = []
        lst = quick_sort(inp)
        self.assertTrue(lst == [])

    def test_quick_sort7(self):
        inp = generate_list(10000, -1000, 1000)
        lst = quick_sort(inp)
        sorted_lst = sorted(inp)
        self.assertTrue(lst == sorted_lst)

    def test_quick_sort8(self):
        inp = ["abc", "xyz", "aaa", "bca", "cca"]
        lst = quick_sort(inp)
        self.assertTrue(lst == ["aaa", "abc", "bca", "cca", "xyz"])


if __name__ == '__main__':
    unittest.main()

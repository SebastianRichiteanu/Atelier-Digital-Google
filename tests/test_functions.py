import unittest
from functions import iter_sum, iterators_sum


class TestIterSum(unittest.TestCase):
    def test_iter_sum(self):
        result = iter_sum([1, 2, 3])
        expected_result = 6

        self.assertEqual(result, expected_result)

    def test_iter_sum_with_exception(self):
        with self.assertRaises(TypeError) as type_error:
            iter_sum('abc')
            print("type_error", type_error.exception)


class TestIteratorsSum(unittest.TestCase):
    def test_iter_sum(self):
        results = iterators_sum([1, 2, 3], [4, 5], "abc")
        expected_results = [6, 9, 0]

        self.assertEqual(results, expected_results)





if '__name__' == '__main__':
    unittest.main()

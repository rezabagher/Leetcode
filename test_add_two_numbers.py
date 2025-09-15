import unittest
from Add_two_Numbers import Solution, list_to_linked, linked_to_list

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        l1 = list_to_linked([2, 4, 3])
        l2 = list_to_linked([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_to_list(result), [7, 0, 8])

    def test_different_lengths(self):
        l1 = list_to_linked([9, 9])
        l2 = list_to_linked([1])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_to_list(result), [0, 0, 1])

    def test_with_zero(self):
        l1 = list_to_linked([0])
        l2 = list_to_linked([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_to_list(result), [0])

    def test_carry_overflow(self):
        l1 = list_to_linked([9, 9, 9])
        l2 = list_to_linked([1])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linked_to_list(result), [0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()

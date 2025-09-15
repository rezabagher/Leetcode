import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def add_up(l_1, l_2):
            dummy = ListNode(0)
            current = dummy
            carry = 0
            while l_1 or l_2 or carry:
                x = l_1.val if l_1 else 0
                y = l_2.val if l_2 else 0
                total = x + y + carry
                carry = total // 10
                current.next = ListNode(total % 10)
                current = current.next
                l_1 = l_1.next if l_1 else None
                l_2 = l_2.next if l_2 else None
            return dummy.next
        return add_up(l1, l2)

# Helper functions
def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

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

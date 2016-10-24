# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        prev = head
        carry = 0
        while (l1 != None or l2 != None) or carry != 0:
            cur = ListNode(0)
            prev.next = cur
            l1v = l1.val if l1 is not None else 0
            l2v = l2.val if l2 is not None else 0
            cur.val = l1v + l2v + carry
            if cur.val >= 10:
                cur.val -= 10
                carry = 1
            else:
                carry = 0
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            prev = cur
        return head.next

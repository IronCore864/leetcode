# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        head = ListNode(None)
        prev = head
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            prev.next = node
            prev = node
        while l1:
            node = ListNode(l1.val)
            l1 = l1.next
            prev.next = node
            prev = node
        while l2:
            node = ListNode(l2.val)
            l2 = l2.next
            prev.next = node
            prev = node
        return head.next


l11 = ListNode(1)
l12 = ListNode(3)
l13 = ListNode(5)
l11.next = l12
l12.next = l13

l21 = ListNode(2)
l22 = ListNode(4)
l23 = ListNode(6)
l21.next = l22
l22.next = l23

s = Solution()
res = s.mergeTwoLists(l11, l21)
while res:
    print res.val
    res = res.next

l11 = None
l21 = ListNode(1)
res = s.mergeTwoLists(l11, l21)
while res:
    print res.val
    res = res.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = ListNode(0)
        start = prev
        prev.next = head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return start.next


head = ListNode(1)
first = ListNode(2)
second = ListNode(6)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
sixth = ListNode(6)
head.next = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
s = Solution()
res = s.removeElements(head, 6)
while res:
    print(res.val)
    res = res.next

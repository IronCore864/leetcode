class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        prev = head
        cur = prev.next
        while cur:
            if cur.val != prev.val:
                prev = cur
                cur = cur.next
            else:
                cur = cur.next
                prev.next = cur
        return head


head = ListNode(1)
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
last = ListNode(3)
head.next = first
first.next = second
second.next = third
third.next = last

s = Solution()
res = s.deleteDuplicates(head)
while res:
    print res.val
    res = res.next

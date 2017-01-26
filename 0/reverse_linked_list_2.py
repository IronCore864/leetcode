class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next is None or m == n:
            return head

        before_reverse = None
        start = head
        i = 1
        while i < m:
            before_reverse = start
            start = start.next
            i += 1

        after_reverse = None

        reverse_head = start
        prev = None

        while i <= n:
            if i == n:
                reverse_end = start
                after_reverse = start.next
            next = start.next
            start.next = prev
            prev = start
            start = next
            i += 1

        if before_reverse is not None:
            before_reverse.next = reverse_end
            reverse_head.next = after_reverse
            return head
        else:
            reverse_head.next = after_reverse
            return reverse_end


head = ListNode(1)
sec = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

head.next = sec
sec.next = third
third.next = fourth
fourth.next = fifth

s = Solution()
res = s.reverseBetween(head, 1, 3)
while res:
    print res.val
    res = res.next

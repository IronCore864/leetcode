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

        while head.val == head.next.val:
            cur = head.next.next
            while cur and cur.val == head.next.val:
                cur = cur.next
            if cur is None:
                return None
            else:
                head = cur
                if head.next is None:
                    return head

        pprev = head
        prev = head.next
        cur = head.next.next
        while cur:
            if cur.val == prev.val:
                while cur and cur.val == prev.val:
                    cur = cur.next
                if cur is None:
                    pprev.next = None
                    return head
                else:
                    pprev.next = cur
                    prev = cur
                    cur = cur.next
            else:
                pprev = prev
                prev = cur
                cur = cur.next
        return head


head = ListNode(1)
first = ListNode(2)
second = ListNode(3)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(4)
last = ListNode(5)

head.next = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = last

s = Solution()
res = s.deleteDuplicates(head)
while res:
    print res.val
    res = res.next

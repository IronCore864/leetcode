class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next is None:
            return head

        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev


head = ListNode(1)
sec = ListNode(2)
third = ListNode(3)
head.next = sec
sec.next = third

s = Solution()
res = s.reverseList(head)
while res:
    print res.val
    res = res.next

res = s.reverseList(None)
while res:
    print res.val
    res = res.next

res = s.reverseList(ListNode(1))
while res:
    print res.val
    res = res.next

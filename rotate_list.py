class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # no rotation; or empty list; or list len is 1
        if k == 0 or head is None or head.next is None:
            return head

        # get list length, and the tail node of the list
        list_len = 0
        current = head
        old_tail = None
        while current is not None:
            list_len += 1
            old_tail = current
            current = current.next
        k %= list_len

        # if k % list_len is 0, it means no rotation at all
        if k == 0:
            return head

        # decide the new head after rotation according to k
        new_head = head
        new_tail = None
        rotation = list_len - k
        while rotation > 0:
            new_tail = new_head
            new_head = new_head.next
            rotation -= 1
        new_tail.next = None
        old_tail.next = head
        return new_head


s = Solution()

l = ListNode(1)
first = ListNode(2)
second = ListNode(3)
third = ListNode(4)
last = ListNode(5)
l.next = first
first.next = second
second.next = third
third.next = last

l = s.rotateRight(l, 2)

while l is not None:
    print l.val
    l = l.next

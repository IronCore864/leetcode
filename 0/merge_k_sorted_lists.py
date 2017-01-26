from heapq import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Using heap to maintain a sorted list which contains the first element of all the arrays
# If using array to contain the first element of all arrays and compare each time it's a waste of time
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = p = ListNode(-1)
        heap = []
        for i in lists:
            if i:  heappush(heap, (i.val, i))
        while heap:
            small = heappop(heap)[1]
            p.next = small
            if small.next: heappush(heap, (small.next.val, small.next))
            p = small
            p.next = None
        return head.next


s = Solution()
l11 = ListNode(1)
l12 = ListNode(3)
l11.next = l12
l13 = ListNode(5)
l12.next = l13

l21 = ListNode(2)
l22 = ListNode(4)
l21.next = l22
l23 = ListNode(6)
l22.next = l23

l31 = ListNode(3)
l32 = ListNode(7)
l31.next = l32

res = s.mergeKLists([l11, l21, l31])
while res:
    print res.val
    res = res.next
res = s.mergeKLists([[], []])
while res:
    print res.val
    res = res.next


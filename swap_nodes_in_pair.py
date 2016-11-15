# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        res = head.next
        prev = None

        while head:
            first = head
            second = first.next
            if not second:
                if prev:
                    prev.next = first
                break
            else:
                third = second.next
                first.next = third
                second.next = first
                if prev:
                    prev.next = second
                prev = first
                head = third

        return res


s = Solution()
l11 = ListNode(2)
l12 = ListNode(1)
l13 = ListNode(4)
l14 = ListNode(3)
l11.next = l12
l12.next = l13
l13.next = l14

# res = s.mergeKLists([l11, l21, l31])
res = s.swapPairs(l11)
while res:
    print res.val
    res = res.next


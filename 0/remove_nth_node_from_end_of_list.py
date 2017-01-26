# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pos = []
        node = head
        while node.next:
            pos.append(node)
            node = node.next
        pos.append(node)
        if n < len(pos):
            pos[len(pos) - n - 1].next = pos[len(pos) - n].next
            return head
        elif n == len(pos):
            return head.next
        else:
            return None


s = Solution()

head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

res = s.removeNthFromEnd(head, 2)
print res.val
while res.next:
    res = res.next
    print res.val


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if k == 1:
            return head

        test = head
        for i in range(k - 1):
            test = test.next
            if not test:
                return head

        res = test

        prev = None

        while head:
            nodes = []
            for i in range(k):
                nodes.append(head)
                head = head.next
                if i != k - 1 and head is None:
                    prev.next = nodes[0]
                    return res
            nodes[0].next = None

            for j in reversed(range(1, k)):
                nodes[j].next = nodes[j - 1]
            if prev:
                prev.next = nodes[k - 1]
            prev = nodes[0]

        return res


s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5


res = s.reverseKGroup(l1, 2)
while res:
    print res.val
    res = res.next


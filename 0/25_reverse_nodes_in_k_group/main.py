from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # len(ListNode) < k
        a = b = head
        for i in range(k):
            if not b:
                return head
            b = b.next

        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead


if __name__ == '__main__':
    s = Solution()

    n1, n2, n3, n4, n5 = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5

    res = s.reverseKGroup(n1, 2)
    while res:
        print(res.val)
        res = res.next

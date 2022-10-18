from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        p1, p2, p = l1, l2, res

        carry = 0
        while p1 and p2:
            carry, val = divmod(p1.val+p2.val+carry, 10)
            p.next = ListNode(val)
            p1, p2, p = p1.next, p2.next, p.next

        while p1:
            carry, val = divmod(p1.val+carry, 10)
            p.next = ListNode(val)
            p1, p = p1.next, p.next

        while p2:
            carry, val = divmod(p2.val+carry, 10)
            p.next = ListNode(val)
            p2, p = p2.next, p.next

        if carry:
            p.next = ListNode(carry)

        return res.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        cur = res
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            carry, val = divmod(l1v + l2v + carry, 10)
            cur.next = ListNode(val)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return res.next


if __name__ == '__main__':
    s = Solution()

    a1 = ListNode(2)
    a1.next = ListNode(4)
    a1.next.next = ListNode(3)
    a2 = ListNode(5)
    a2.next = ListNode(6)
    a2.next.next = ListNode(4)
    res = s.addTwoNumbers(a1, a2)
    while res:
        print(res.val, end='')
        res = res.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbersEasyToRead(self, l1: ListNode, l2: ListNode) -> ListNode:
        # since l1 and l2 are not empty (at least each list has one node)
        # creating the first node of the result
        nodeval = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val)//10
        result = ListNode(nodeval)

        # and prepare three pointers l1p (to l1) l2p (to l2) and rp (to result) pointing to the first node of the list
        l1p, l2p, rp = l1, l2, result

        while l1p.next and l2p.next:
            # when l1 and l2 are both not empty yet, moving pointers to the next node for calculation
            l1p, l2p = l1p.next, l2p.next
            nodeval = (carry + l1p.val + l2p.val) % 10
            carry = (carry + l1p.val + l2p.val) // 10
            # creating the next node for the result list
            rp.next = ListNode(nodeval)
            # and moving the result pointer to the newly created node
            rp = rp.next

        while l1p.next:
            # after the previous while loop finishes, at least one of l1, l2 are empty now
            # if l1 is longer, pending all remaining nodes to the result
            l1p = l1p.next
            nodeval = (carry + l1p.val) % 10
            carry = (carry + l1p.val)//10
            rp.next = ListNode(nodeval)
            rp = rp.next

        while l2p.next:
            # if l2 is longer, pending all remaining nodes to the result
            l2p = l2p.next
            nodeval = (carry + l2p.val) % 10
            carry = (carry + l2p.val)//10
            rp.next = ListNode(nodeval)
            rp = rp.next

        if carry:
            # if after iterating both l1 and l2, carry still has a value of 1 in it
            rp.next = ListNode(carry)

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # harder to read but shorter, with the same logic
        head = ListNode(0)
        prev = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            newnode = ListNode(0)
            prev.next = newnode
            l1v = l1.val if l1 is not None else 0
            l2v = l2.val if l2 is not None else 0
            newnode.val = (l1v + l2v + carry) % 10
            carry = (l1v + l2v + carry)//10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            prev = newnode
        return head.next


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
    print()

    a1 = ListNode(0)
    a2 = ListNode(0)
    res = s.addTwoNumbers(a1, a2)
    while res:
        print(res.val, end='')
        res = res.next
    print()

    a11 = ListNode(9)
    a12 = ListNode(9)
    a13 = ListNode(9)
    a14 = ListNode(9)
    a15 = ListNode(9)
    a16 = ListNode(9)
    a17 = ListNode(9)
    a11.next = a12
    a12.next = a13
    a13.next = a14
    a14.next = a15
    a15.next = a16
    a16.next = a17

    a21 = ListNode(9)
    a22 = ListNode(9)
    a23 = ListNode(9)
    a24 = ListNode(9)
    a21.next = a22
    a22.next = a23
    a23.next = a24
    res = s.addTwoNumbers(a11, a21)
    while res:
        print(res.val, end='')
        res = res.next
    print()

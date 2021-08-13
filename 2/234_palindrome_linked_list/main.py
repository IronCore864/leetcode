from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # reverse first half, the head of the reversed list
        h = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            h, h.next, slow = slow, h, slow.next

        # odd
        if fast:
            slow = slow.next

        while h and h.val == slow.val:
            slow = slow.next
            h = h.next

        return not h


if __name__ == '__main__':
    s = Solution()
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
    n1.next, n2.next, n3.next = n2, n3, n4
    print(s.isPalindrome(n1))

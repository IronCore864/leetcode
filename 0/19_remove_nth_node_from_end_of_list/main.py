from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        slow, fast = start, start
        slow.next = head

        # move fast in front so that the gap between slow and fast becomes n
        for i in range(n+1):
            fast = fast.next

        # move fast to the end, maintaining the gap
        while fast:
            slow, fast = slow.next, fast.next

        # skip the desired node
        slow.next = slow.next.next
        return start.next


if __name__ == '__main__':
    s = Solution()
    print(s.removeNthFromEnd(ListNode(1), 0))

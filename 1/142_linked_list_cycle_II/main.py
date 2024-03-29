# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # analysis see here: https://labuladong.gitee.io/algo/2/19/50/
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head

        return None

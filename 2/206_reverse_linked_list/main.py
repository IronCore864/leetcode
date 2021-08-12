from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        previous = None
        while head:
            next = head.next
            head.next = previous

            previous = head
            head = next

        return previous

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive, slower, but much easier to read and understand
        """
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


def _print_list(head):
    """
    For testing.
    """
    res = ""
    while head:
        res += "{} -> ".format(head.val)
        head = head.next
    res += "None"
    print(res)


if __name__ == '__main__':
    s = Solution()

    # None
    res = s.reverseList(None)
    _print_list(res)

    # 3 -> 2 -> 1
    head, second, third = ListNode(1), ListNode(2), ListNode(3)
    head.next, second.next = second, third
    res = s.reverseList(head)
    _print_list(res)

    # 1
    res = s.reverseList(ListNode(1))
    _print_list(res)

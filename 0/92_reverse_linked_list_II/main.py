from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        start = head
        i = 1
        before = None
        while i < left:
            before = start
            start = start.next
            i += 1

        reverse_head = start
        previous = None
        for _ in range(right-left+1):
            next_node = start.next
            start.next = previous
            previous = start
            start = next_node

        reverse_head.next = start
        if not before:
            return previous
        else:
            before.next = previous
            return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Recursive, easier to read
        """
        if not head.next:
            return None

        if head.next is None or left == right:
            return head

        next_node = None

        def reverse_first_n(head, n):
            nonlocal next_node
            if n == 1:
                next_node = head.next
                return head
            last = reverse_first_n(head.next, n - 1)
            head.next.next = head
            head.next = next_node
            return last

        if left == 1:
            # equivalent to reversing the first "right" number of nodes
            return reverse_first_n(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


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

    # 1 -> None
    res = s.reverseBetween(ListNode(1), 1, 1)
    _print_list(res)

    # 1 -> 4 -> 3 -> 2 -> 5 -> None
    head, second, third, fourth, fifth = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    head.next, second.next, third.next, fourth.next = \
        second, third, fourth, fifth
    res = s.reverse_between(head, 3, 4)
    _print_list(res)

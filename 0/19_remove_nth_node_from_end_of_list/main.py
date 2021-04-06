class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        previous = current
        tail = current

        for i in range(n):
            tail = tail.next

        while tail:
            previous = current
            current = current.next
            tail = tail.next

        # removing from the beginning of the list
        if previous == current:
            head = previous.next
        else:
            previous.next = current.next

        return head


def construct_list_of_nodes_by_arr(nums):
    res = ListNode(nums[0])
    current = res
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return res


def print_node_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    s = Solution()

    n = 2
    nodes_list = construct_list_of_nodes_by_arr([1, 2, 3, 4, 5])
    res = s.removeNthFromEnd(nodes_list, n)
    print_node_list(res)

    # None
    print(s.removeNthFromEnd(ListNode(1), 1))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        # merge sort
        head = ListNode()
        # pointer
        p = head
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        else:
            p.next = list2
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        # empty
        if not head:
            return None

        # only 1 node in the list
        if not head.next:
            return head

        # find the middle point of the list and split them into two
        previous = None
        slow = head
        fast = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        # breaking the list into two parts
        previous.next = None

        # merge
        return self.merge(self.sortList(head), self.sortList(slow))


# for testing
def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    s = Solution()

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    assert list_to_array(s.sortList(head)) == [1, 2, 3, 4]

    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)
    assert list_to_array(s.sortList(head)) == [-1, 0, 3, 4, 5]

    assert s.sortList(None) == None

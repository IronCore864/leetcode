class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        previous = head
        current = head.next

        while current:
            if current.val >= previous.val:
                previous = current
                current = current.next
                continue

            next = current.next
            # find position to insert
            prev = None
            cur = head
            while cur.val < current.val:
                prev = cur
                cur = cur.next
            if not prev:
                current.next = head
                head = current
            else:
                prev.next = current
                current.next = cur

            previous.next = next
            current = next

        return head


head = ListNode(4)
first = ListNode(3)
second = ListNode(2)
last = ListNode(1)

head.next = first
first.next = second
second.next = last

s = Solution()
res = s.insertionSortList(head)

while res:
    print res.val
    res = res.next

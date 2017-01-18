class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = ListNode(0)
        smaller_start = smaller

        larger = ListNode(0)
        larger_start = larger

        cur = head
        while cur:
            node = ListNode(cur.val)
            if cur.val < x:
                smaller.next = node
                smaller = smaller.next
            else:
                larger.next = node
                larger = larger.next
            cur = cur.next

        smaller.next = larger_start.next
        return smaller_start.next


head = ListNode(1)
second = ListNode(4)
third = ListNode(3)
fourth = ListNode(2)
fifth = ListNode(5)
last = ListNode(2)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = last

s = Solution()


def output(res):
    while res:
        print res.val
        res = res.next
    print


res = s.partition(head, 3)
output(res)

res = s.partition(ListNode(1), 0)
output(res)

head = ListNode(2)
second = ListNode(1)
head.next = second

res = s.partition(head, 1)
output(res)

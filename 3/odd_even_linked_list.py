class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # length <= 2
        if not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        even_head = head.next

        # move odd and even pointer one step forward
        while even.next and even.next.next:
            odd.next = even.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next

        # handle odd length remaining issue
        if even.next:
            odd.next = even.next
            odd = odd.next
            even.next = None

        odd.next = even_head

        return head


n = 3
node = [ListNode(i + 1) for i in range(n)]
for i in range(n - 1):
    node[i].next = node[i + 1]

s = Solution()
res = s.oddEvenList(node[0])

while res:
    print(res.val)
    res = res.next

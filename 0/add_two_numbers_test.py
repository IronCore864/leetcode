from add_two_numbers import Solution, ListNode

n1 = ListNode(5)
l1 = n1

n2 = ListNode(5)
l2 = n2

s = Solution()

res = s.addTwoNumbers(l1, l2)

print res.val
while res.next is not None:
    res = res.next
    print res.val

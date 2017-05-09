# 2.1) L1 is defined as the distance between the head point and entry point
# 2.2) L2 is defined as the distance between the entry point and the meeting point
# 2.3) C is defined as the length of the cycle
# 2.4) n is defined as the travel times of the fast pointer around the cycle When the first encounter of the slow pointer and the fast pointer

# According to the definition of L1, L2 and C, we can obtain:
# the total distance of the slow pointer traveled when encounter is L1 + L2
# the total distance of the fast pointer traveled when encounter is L1 + L2 + n * C
# Because the total distance the fast pointer traveled is twice as the slow pointer, Thus:
# 2 * (L1+L2) = L1 + L2 + n * C => L1 + L2 = n * C => L1 = (n - 1) C + (C - L2)*
# It can be concluded that the distance between the head location and entry location is equal to the distance between the meeting location and the entry location along the direction of forward movement.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or nead.next is None:
            return None

        slow = head
        fast = head
        entry = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry

        return None

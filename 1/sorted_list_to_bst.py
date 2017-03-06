class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # finding the mid point of a linked list using slow and fast pointers, where
        # slow pointer + 1 and fast pointer + 2
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root

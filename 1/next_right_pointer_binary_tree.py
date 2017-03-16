class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left

        if root.left:
            self.connect(root.left)
        if root.right:
            self.connect(root.right)


n1 = TreeLinkNode(1)
n21 = TreeLinkNode(2)
n22 = TreeLinkNode(3)
n31 = TreeLinkNode(4)
n32 = TreeLinkNode(5)
n33 = TreeLinkNode(6)
n34 = TreeLinkNode(7)

n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n22.left = n33
n22.right = n34

s = Solution()
s.connect(n1)

print n1.next
print n21.next.val
print n22.next
print n31.next.val
print n32.next.val
print n33.next.val
print n34.next

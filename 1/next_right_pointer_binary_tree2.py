class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def _connect(self, current_layer):
        if current_layer == []:
            return
        next_layer = []
        for root in current_layer:
            if root:
                if root.left:
                    next_layer.append(root.left)
                    if root.right:
                        root.left.next = root.right
                    else:
                        current = root
                        while current.next:
                            current = current.next
                            if current.left:
                                root.left.next = current.left
                                break
                            if current.right:
                                root.left.next = current.right
                                break
                if root.right:
                    next_layer.append(root.right)
                    current = root
                    while current.next:
                        current = current.next
                        if current.left:
                            root.right.next = current.left
                            break
                        if current.right:
                            root.right.next = current.right
                            break

        self._connect(next_layer)

    def connect(self, root):
        self._connect([root])


n1 = TreeLinkNode(2)
n21 = TreeLinkNode(1)
n22 = TreeLinkNode(3)
n31 = TreeLinkNode(0)
n32 = TreeLinkNode(7)
n33 = TreeLinkNode(9)
n34 = TreeLinkNode(1)
n41 = TreeLinkNode(2)
n42 = TreeLinkNode(1)
n43 = TreeLinkNode(0)
n44 = TreeLinkNode(8)
n45 = TreeLinkNode(8)

n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n22.left = n33
n22.right = n34
n31.left = n41
n32.left = n42
n32.right = n43
n34.left = n44
n34.right = n45

s = Solution()
s.connect(n1)

print n43.next

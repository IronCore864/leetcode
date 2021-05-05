class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursive(self, root: TreeNode) -> list[int]:
        res = []

        def recursive(node):
            if not node:
                return
            recursive(node.left)
            res.append(node.val)
            recursive(node.right)

        recursive(root)

        return res

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        current = root

        # while current or stack is a trick,
        # in order not to exist when stack pops all till root node without searching for the right side
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(s.inorderTraversal(root))
    assert s.inorderTraversal(root) == [1, 3, 2]

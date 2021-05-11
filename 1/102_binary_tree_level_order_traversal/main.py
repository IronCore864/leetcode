class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if not root:
            return result

        # recursively calculate each layer's output
        # and nodes for the next layer
        def recursive(current_level: list[TreeNode]):
            if len(current_level) == 0:
                return

            level_result = []
            next_level = []

            for node in current_level:
                level_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(level_result)
            recursive(next_level)

        recursive([root])
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # print(s.levelOrder(root))
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(None) == []

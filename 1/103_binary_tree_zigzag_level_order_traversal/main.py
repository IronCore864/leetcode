class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if not root:
            return result

        # recursively calculate each layer's output
        # and nodes for the next layer
        # going_right: True means going right, False means left
        def recursive(current_level: list[TreeNode], going_right: bool):
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

            if going_right:
                result.append(level_result)
            else:
                result.append(level_result[::-1])
            going_right = not going_right

            recursive(next_level, going_right)

        recursive([root], True)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))

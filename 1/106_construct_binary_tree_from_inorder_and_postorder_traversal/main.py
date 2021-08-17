from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_val_inorder_index = inorder.index(root_val)

        left_inorder = inorder[0: root_val_inorder_index]
        right_inorder = inorder[root_val_inorder_index+1:]
        left_postorder = postorder[0: len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root


def print_tree(nodes):
    """
    for testing
    """
    empty = True
    for node in nodes:
        if node:
            empty = False
            break

    if empty:
        return

    res = []
    next_row = []
    for node in nodes:
        if node:
            res.append(node.val)
            next_row.append(node.left)
            next_row.append(node.right)
        else:
            res.append(None)
            next_row.append(None)
            next_row.append(None)

    print(res)
    print_tree(next_row)


if __name__ == '__main__':
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = s.buildTree(inorder, postorder)
    print_tree([root])

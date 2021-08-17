from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # see https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/ for more details
    # preorder[0] is the root_val
    # search the index of the root in the inorder: root_inorder_idx = inorder.index(root_val)
    # in the inorder array, before this index, it's the left subtree; and after, it's the right subtree. This is the property if inorder traverse
    # recursively construct the left subtree and the right subtree. Using the left subtree's inorder length to determine which section in the preorder belongs to the left subtree
    # do the same for the right
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_val_inorder_index = inorder.index(root_val)
        left_inorder = inorder[0:root_val_inorder_index]
        right_inorder = inorder[root_val_inorder_index+1:]
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[1+len(left_inorder):]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = s.buildTree(preorder, inorder)
    print_tree([root])

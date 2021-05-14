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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        left_tree_inorder = inorder[0:inorder.index(root_val)]
        left_tree_inorder_len = len(left_tree_inorder)
        left_tree_preorder = preorder[1:left_tree_inorder_len+1]
        root.left = self.buildTree(left_tree_preorder, left_tree_inorder)

        right_tree_inorder = inorder[inorder.index(root_val)+1:]
        right_tree_preorder = preorder[left_tree_inorder_len+1:]
        root.right = self.buildTree(right_tree_preorder, right_tree_inorder)

        return root

# for testing


def print_tree(nodes):
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

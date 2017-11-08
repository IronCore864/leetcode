import collections


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

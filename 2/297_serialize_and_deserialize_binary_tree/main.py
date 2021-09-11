# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return '#'

        res = str(root.val)
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return res + '|' + l + '|' + r

    def deserialize(self, data):
        vals = data.split('|')

        def traverse():
            val = vals.pop(0)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = traverse()
            node.right = traverse()
            return node

        return traverse()


if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.right.left, root.right.right = TreeNode(4), TreeNode(5)
    c = Codec()
    serialized = c.serialize(root)
    print(serialized)
    res = c.deserialize(serialized)
    print(res.val, res.left.val, res.right.val)

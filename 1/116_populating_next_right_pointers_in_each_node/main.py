class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_recursive(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def connect_two_nodes(a, b):
            if not a or not b:
                return
            a.next = b
            connect_two_nodes(a.left, a.right)
            connect_two_nodes(b.left, b.right)
            connect_two_nodes(a.right, b.left)

        connect_two_nodes(root.left, root.right)
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        current_level = [root]

        while current_level:
            next_level = []
            for i in range(len(current_level)):
                if i != len(current_level)-1:
                    current_level[i].next = current_level[i+1]

                if current_level[i].left:
                    next_level.append(current_level[i].left)
                if current_level[i].right:
                    next_level.append(current_level[i].right)
            current_level = next_level

        return root


if __name__ == '__main__':
    s = Solution()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    s.connect(root)
    assert root.next == None
    assert root.left.next == root.right
    assert root.right.next == None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next == None

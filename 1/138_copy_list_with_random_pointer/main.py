class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        # key: old node
        # value: new node
        mapping = {}

        cur = head
        # creating new nodes and record the mapping between the old and the new nodes
        # without setting next/random pointers of the new node
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        # setting next/random pointers based on the mapping
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next

        return mapping[head]


if __name__ == '__main__':
    s = Solution()

    head = Node(7)
    node1 = Node(13)
    node2 = Node(11)
    node3 = Node(10)
    node4 = Node(1)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = head
    node2.random = node4
    node3.random = node2
    node4.random = head

    res = s.copyRandomList(head)
    assert res.val == 7
    assert res.next.val == 13
    assert res.next.next.val == 11
    assert res.next.next.next.val == 10
    assert res.next.next.next.next.val == 1
    assert res.next.random == res
    assert res.next.next.random == res.next.next.next.next
    assert res.next.next.next.random == res.next.next
    assert res.next.next.next.next.random == res

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        if head.label in self.visited:
            return self.visited[head.label]

        clone = RandomListNode(head.label)
        self.visited[head.label] = clone

        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)
        return clone

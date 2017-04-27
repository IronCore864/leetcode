class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return None

        if node.label in self.visited:
            return self.visited[node.label]

        clone = UndirectedGraphNode(node.label)
        self.visited[node.label] = clone

        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))
        return clone


n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n0.neighbors = [n1, n2]
n1.neighbors = [n2]
n2.neighbors = [n2]

s = Solution()
print s.cloneGraph(n0)

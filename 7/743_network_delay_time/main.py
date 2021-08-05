from collections import defaultdict
from typing import List
import sys


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # construct the graph from times
        # graph[u] = [(v1, w1), (v2, w2), ...]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # distance, initialized to max int first except dist[k] = 0
        dist = {node: sys.maxsize for node in range(1, n + 1)}
        dist[k] = 0

        # current at this node
        q = [k]

        # breadth-first search
        # (or Dijkstra, which is weighted breadth-first search)
        while q:
            # get the current node and pop it
            u = q.pop(0)

            # for all possible neighbours of u:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = min(dist[v], dist[u] + w)
                    q.append(v)

        res = max(dist.values())
        # if there still is some dist that is max int
        # it means it's not reachable
        return res if res != sys.maxsize else -1


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))


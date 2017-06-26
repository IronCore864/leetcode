class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: set() for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        for (e, s) in prerequisites:
            graph[s] |= {e}
            in_degree[e] += 1

        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        visited = set(queue)

        for node in queue:
            for neighbour in graph[node]:
                if neighbour in visited:
                    return []
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    visited.add(neighbour)
                    queue += [neighbour]

        return queue if len(queue) == numCourses else []


s = Solution()
print(s.findOrder(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))

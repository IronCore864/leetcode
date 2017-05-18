import numpy as np


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        n = len(points)
        if n < 3:
            return n

        res = 0
        for i in xrange(n):
            k = {"dx=0": 1}
            same = 0
            for j in xrange(i + 1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same += 1
                    continue
                if points[i].x == points[j].x:
                    k["dx=0"] += 1
                else:
                    slope = (points[i].y - points[j].y) / np.float128(points[i].x - points[j].x)
                    if slope not in k:
                        k[slope] = 2
                    else:
                        k[slope] += 1
            res = max(res, max(k.values()) + same)
        return res


p = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
points = []
for (x, y) in p:
    points.append(Point(x, y))

s = Solution()
print s.maxPoints(points)

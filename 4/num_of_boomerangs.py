from collections import defaultdict


class Solution(object):
    def _dist(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            value_count_dict = defaultdict(int)
            for q in points:
                key = [p, q]
                key.sort()
                dist = self._dist(p, q)
                value_count_dict[dist] += 1
            for k, v in value_count_dict.items():
                res += v * (v - 1)
        return res

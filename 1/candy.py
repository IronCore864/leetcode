class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        total = 1
        prev = 1
        count = 0

        for i in xrange(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if count > 0:
                    total += (1 + count) * count / 2
                    if count >= prev:
                        total += count - prev + 1
                    count = 0
                    prev = 1
                prev = 1 if ratings[i] == ratings[i - 1] else prev + 1
                total += prev
            else:
                count += 1
        if count > 0:
            total += (1 + count) * count / 2
            if count >= prev:
                total += count - prev + 1
        return total


s = Solution()
print s.candy([1, 2, 2])
print s.candy([2, 2])
print s.candy([2, 3, 2])
print s.candy([8, 9, 7, 2])
print s.candy([4, 3, 2, 1])
print s.candy([8, 9, 7, 2, 10, 6, 3, 1, 4, 5])
print s.candy([10, 6, 3, 1, 4, 5])
print s.candy([1, 0, 2])
print s.candy([4, 3, 2, 2])
print s.candy([1, 2, 4, 4, 3])

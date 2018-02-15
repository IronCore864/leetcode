class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            return True if n == 1 and not flowerbed[0] or n == 0 else False

        c = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if i == 0 and flowerbed[i + 1] == 0:
                c += 1
                flowerbed[i] = 1
                continue
            if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                c += 1
                flowerbed[i] = 1
                continue
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                c += 1
                flowerbed[i] = 1
                continue

        return n <= c


s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))

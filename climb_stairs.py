class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_stair_before_current = 2
        two_stairs_before_current = 1
        for i in range(2, n):
            ways_to_next_stair = one_stair_before_current + two_stairs_before_current
            two_stairs_before_current = one_stair_before_current
            one_stair_before_current = ways_to_next_stair
        return ways_to_next_stair


s = Solution()
print s.climbStairs(0)
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(5)

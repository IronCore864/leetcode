class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums)[::-1]
        rank = {sort[i]:i+1 for i in range(len(sort))}
        for k, v in rank.items():
            if v == 1:
                rank[k] = "Gold Medal"
            if v == 2:
                rank[k] = "Silver Medal"
            if v == 3:
                rank[k] = "Bronze Medal"
        return [str(rank[num]) for num in nums]
        

from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: 'List[int]', K: 'int') -> 'int':
        """
        The O(n**2) solution in main1.py timed out.
        This means, we must figure out a better algo with lower time complexity.

        We can't really do binary search here (or something to that effect, logn search),
        because if we do, we are skipping some elements
        (that's the nature of binary search.)
        And if we skip some elements, we don't know what they are,
        and we can't know if we skipped some suitable subarray or not.

        This means, O(nlogn) is also out of the picture.
        So, the last choice is the only logical solution:
        we need to do an O(n) solution - sliding window.

        Logic:

        [1, 2, 1, 2, 3]
         i     j     k

        [i, j) (nums[j] not inclusive) means K different integers inside [i, j).
        [i, k] (nums[k] inclusive) means K+1 different integers inside [i, k].

        So, [1, 2], [1, 2, 1], and [1, 2, 1, 2] are all sub-arrays that has K different integers.
        And the number equals to k - j + 1
        """

        n = len(nums)

        count = defaultdict(int)

        i, j, res = 0, 0, 0

        for i in range(n):
            while j < n and len(count) < K:
                count[nums[j]] += 1
                j += 1

            if len(count) < K:
                break

            k = j
            while k < n and nums[k] in count:
                k += 1

            res += k - j + 1

            count[nums[i]] -= 1
            if count[nums[i]] == 0:
                del count[nums[i]]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))

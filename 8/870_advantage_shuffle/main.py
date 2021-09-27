from bisect import bisect_right
from typing import List


class Solution:
    def advantage_count_binarysearch(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        res = []

        for num in nums2:
            pos = bisect_right(nums1, num)
            if pos == len(nums1):
                pos = 0
            res.append(nums1.pop(pos))

        return res

    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]


if __name__ == '__main__':
    s = Solution()
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    print(s.advantageCount(nums1, nums2))
    # Output: [2,11,7,15]

    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    print(s.advantageCount(nums1, nums2))
    # Output: [24,32,8,12]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged[len(merged) / 2] if len(merged) % 2 == 1 else (merged[len(merged) / 2 - 1] + merged[len(merged) / 2]) / 2.0


s = Solution()
print s.findMedianSortedArrays([1, 3], [2])
print s.findMedianSortedArrays([1, 2], [3, 4])

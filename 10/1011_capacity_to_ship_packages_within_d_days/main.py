class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        while lo <= hi:
            mid = (lo + hi) // 2

            current = 0
            d = 1
            for w in weights:
                if current + w > mid:
                    d += 1
                    current = 0
                current += w

            if d > days:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

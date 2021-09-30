from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        if len(piles) == h:
            return hi

        while lo <= hi:
            mid = (lo + hi) // 2

            r = 0
            for pile in piles:
                a, b = divmod(pile, mid)
                r += a
                if b:
                    r += 1

            # find the left most
            if r > h:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

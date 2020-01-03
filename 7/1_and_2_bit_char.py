class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
                continue
            if bits[i] == 1:
                i += 2
                continue
        return True if i == len(bits) - 1 else False

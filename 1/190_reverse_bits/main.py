class Solution:
    def reverseBits(self, n: int) -> int:
        # convert integer to binary string
        n_binary = '{0:b}'.format(n)
        # reverse the binary string
        # if the length is less than 32 bits, append zeroes at the beginning
        n_binary = '0' * (32 - len(n_binary)) + n_binary
        # reverse, and convert back to int
        return int(n_binary[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))

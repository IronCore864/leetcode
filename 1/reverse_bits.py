class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = '{0:032b}'.format(n)
        reverse = binary[::-1]
        return int(reverse, 2)

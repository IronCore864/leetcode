class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        sign = '-' if numerator * denominator < 0 else ''
    
        numerator, denominator = abs(numerator), abs(denominator)

        res = sign + str(numerator//denominator)

        remainder = numerator % denominator
        if remainder == 0:
            return res

        res += '.'

        m = dict()
        parts = []
        
        while remainder != 0:
            # meet a known remainder
            # so we reach the end of the repeating part
            if remainder in m:
                parts.insert(m[remainder], '(')
                parts.append(')')
                break

            # the remainder is first seen
            # remember the current position for it
            m[remainder] = len(parts)

            remainder *= 10
            # append the quotient digit
            parts.append(str(remainder // denominator))
            remainder = remainder % denominator

        return res + ''.join(parts)

    
if __name__ == '__main__':
    s = Solution()
    assert s.fractionToDecimal(1, 2) == '0.5'

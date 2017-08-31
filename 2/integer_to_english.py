class Solution(object):
    def __init__(self):
        self.d = {
            '0': '',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
        }

        self.ten = {
            '0': '',
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety',
        }

    def convert(self, num, unit):
        if num == 0:
            return ''
        res = []
        if num >= 100:
            res.append(self.d[str(num // 100)])
            res.append('Hundred')
        if num % 100 // 10 == 1:
            res.append(self.d[str(num % 100)])
        else:
            ten = self.ten[str(num % 100 // 10)]
            if ten:
                res.append(ten)
            one = self.d[str(num % 100 % 10)]
            if one:
                res.append(one)
        res.append(unit)
        return ' '.join(res) + ' '

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        billion = num // 1000000000
        million = num % 1000000000 // 1000000
        thousand = num % 1000000 // 1000
        other = num % 1000

        res = self.convert(billion, 'Billion') + self.convert(million, 'Million') + \
              self.convert(thousand, 'Thousand') + self.convert(other, '')
        res = res.strip()
        return res


s = Solution()
print(s.numberToWords(3))
print(s.numberToWords(13))
print(s.numberToWords(23))
print(s.numberToWords(103))
print(s.numberToWords(113))
print(s.numberToWords(123))
print(s.numberToWords(12345))
print(s.numberToWords(1234567))
# 2147483647
print(s.numberToWords(2 ** 31 - 1))
print(s.numberToWords(2001012001))

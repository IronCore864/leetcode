class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        prev = chars[0]
        counter = 1
        pos = 0
        n = len(chars)
        for i in range(1, n):
            if chars[i] == prev:
                counter += 1
                if i == n - 1:
                    chars[pos] = prev
                    pos += 1
                    counter = [char for char in str(counter)]
                    chars[pos:pos + len(counter)] = counter
                    pos = pos + len(counter)
            else:
                if counter == 1:
                    chars[pos] = prev
                    pos += 1
                    prev = chars[i]
                else:
                    chars[pos] = prev
                    pos += 1
                    counter = [char for char in str(counter)]
                    chars[pos:pos + len(counter)] = counter
                    pos = pos + len(counter)
                    prev = chars[i]
                    counter = 1
                if i == n - 1:
                    chars[pos] = prev
                    pos += 1
        return pos


s = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
len = s.compress(chars)
print(len, chars[0:len])

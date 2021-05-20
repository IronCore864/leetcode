class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def is_palindrome(s):
            start, end = 0, len(s)-1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(index, tmpres):
            if index == len(s):
                # pass by reference
                res.append(tmpres[:])
                return

            for i in range(index+1, len(s)+1):
                word = s[index:i]
                if is_palindrome(word):
                    tmpres.append(word)
                    dfs(i, tmpres)
                    tmpres.pop()

        dfs(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.partition('a'))
    print(s.partition('aab'))
    print(s.partition('abbab'))

from typing import List


def palindrome_pairs(words: List[str]) -> List[List[int]]:
    word_dict = {}
    res = []

    for i in range(len(words)):
        word_dict[words[i]] = i

    for i in range(len(words)):
        for j in range(len(words[i]) + 1):
            tmp1 = words[i][:j]
            tmp2 = words[i][j:]
            if tmp1[::-1] in word_dict and word_dict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                res.append([i, word_dict[tmp1[::-1]]])
            if j != 0 and tmp2[::-1] in word_dict and word_dict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                res.append([word_dict[tmp2[::-1]], i])

    return res


if __name__ == "__main__":
    # Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
    # Output: [[0,1],[1,0],[3,2],[2,4]]
    print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(palindrome_pairs(["bat", "tab", "cat"]))
    print(palindrome_pairs(["a", ""]))
    print(palindrome_pairs(["a", "b", "c", "ab", "ac", "aa"]))
    print(palindrome_pairs(["a", "abc", "aba", ""]))

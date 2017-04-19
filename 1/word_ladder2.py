import collections
import string


class Solution(object):
    def findLadders(self, begin, end, words_list):
        if end not in words_list:
            return []

        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]
                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, next_word, is_forward):
            if is_forward:
                tree[word] += next_word,
            else:
                tree[next_word] += word,

        def bfs_level(forward_level, backward_level, tree, is_forward, word_set):
            if not forward_level:
                return False

            if len(forward_level) > len(backward_level):
                return bfs_level(backward_level, forward_level, tree, not is_forward, word_set)

            for word in (forward_level | backward_level):
                word_set.discard(word)

            next_level, found = set(), False
            while forward_level:
                word = forward_level.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        possbble_next_word = word[:index] + c + word[index + 1:]
                        if possbble_next_word in backward_level:
                            found = True
                            add_path(tree, word, possbble_next_word, is_forward)
                        if not found and possbble_next_word in word_set:
                            next_level.add(possbble_next_word)
                            add_path(tree, word, possbble_next_word, is_forward)
            return found or bfs_level(next_level, backward_level, tree, is_forward, word_set)

        tree, path, paths = collections.defaultdict(list), [begin], []
        is_found = bfs_level(set([begin]), set([end]), tree, True, set(words_list))
        print tree
        return construct_paths(begin, end, tree)



s = Solution()
print s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

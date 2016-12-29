class Solution(object):
    @staticmethod
    def _generate_line(words, maxWidth):
        # add first word into line
        line = words[0]
        # total spaces in the line
        space_total_len = maxWidth - len("".join(words))
        # if there is only one word in the line, adding spaces at the end and return
        if len(words) == 1:
            return line + " " * space_total_len
        # how many spaces are needed to separate all the words
        spaces_needed = len(words) - 1
        # length for each separating space
        avg_space_len = space_total_len / spaces_needed
        # remaining spaces unused
        uneven_spaces = space_total_len % spaces_needed
        for w in words[1:]:
            # if there are remaining spaces, add one to average space length
            if uneven_spaces > 0:
                line = line + " " * (avg_space_len + 1) + w
                uneven_spaces -= 1
            # if no more remaining spaces, the space len is the average space length
            else:
                line = line + " " * avg_space_len + w
        return line

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line_words = []
        i = 0
        while i < len(words):
            # new line has no word yet, and the first word does not exceed the maxWidth limit,
            # add it to new line and continue
            if len(line_words) == 0 and len(words[i]) <= maxWidth:
                line_words.append(words[i])
                i += 1
            # new line already has words
            # decide if adding at least one space and the next word will exceed the maxWidth limit or not
            elif len(line_words) != 0 and len(" ".join(line_words)) + 1 + len(words[i]) <= maxWidth:
                line_words.append(words[i])
                i += 1
            # line is full and cannot add another word without exceeding the maxWidth limit
            # output the line
            else:
                line = self._generate_line(line_words, maxWidth)
                res.append(line)
                line_words = []
        # dealing with the last line
        res.append(" ".join(line_words) + " " * (maxWidth - len(" ".join(line_words))))
        return res


def output(arr):
    for i in arr:
        print "|" + i + "|"
    print ""


s = Solution()

res = s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
output(res)

res = s.fullJustify(["This"], 16)
output(res)

res = s.fullJustify(["This"], 4)
output(res)

res = s.fullJustify(["a", "b", "c", "d", "e"], 3)
output(res)

res = s.fullJustify(["What", "must", "be", "shall", "be."], 12)
output(res)

res = s.fullJustify(
    ["Given", "an", "array", "of", "words", "and", "a", "length", "L,", "format", "the", "text", "such", "that", "each",
     "line", "has", "exactly", "L", "characters", "and", "is", "fully", "(left", "and", "right)", "justified.", "You",
     "should", "pack", "your", "words", "in", "a", "greedy", "approach;", "that", "is,", "pack", "as", "many", "words",
     "as", "you", "can", "in", "each", "line.", "Pad", "extra", "spaces", "'", "'", "when", "necessary", "so", "that",
     "each", "line", "has", "exactly", "L", "characters.", "Extra", "spaces", "between", "words", "should", "be",
     "distributed", "as", "evenly", "as", "possible.", "If", "the", "number", "of", "spaces", "on", "a", "line", "do",
     "not", "divide", "evenly", "between", "words,", "the", "empty", "slots", "on", "the", "left", "will", "be",
     "assigned", "more", "spaces", "than", "the", "slots", "on", "the", "right.", "For", "the", "last", "line", "of",
     "text,", "it", "should", "be", "left", "justified", "and", "no", "extra", "space", "is", "inserted", "between",
     "words."], 20)
output(res)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort intervals by start, using the key function in sort() function
        intervals.sort(key=lambda x: x[0])

        result = []

        for i, interval in enumerate(intervals):
            if i == 0:
                # initialize result to be the first interval of the input
                result = [intervals[0]]

            # then merging others one by one into the result

            # if not overlapping (second interval start > first interval end), append to result
            if interval[0] > result[-1][1]:
                result.append(interval)
            # if exactly overlapping, expand the interval to [first interval start, second interval end]
            elif interval[0] == result[-1][1]:
                result[-1] = [result[-1][0], interval[1]]
            else:
                # if overlapping (second interval start < first interval end)
                # because it's sorted, it's guaranteed that first interval start <= second interval start
                # in this case, expand the result to [first interval start, max(first interval end, second interval end)]
                # the max() function handles if the second interval is completely in the first interval or not.
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]

        return result


if __name__ == '__main__':
    s = Solution()
    # There is no guarantee by the problem that the intervals are sorted,
    # although the example given is sorted.

    # By observing the example input, it's not hard to find out, that the intuitive solution is to sort it first.
    # Because if it's sorted, it's easy to compare the two adjacent intervals.
    # If the adjacent two overlap, merge; else, append.
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert s.merge(intervals) == [[1, 6], [8, 10], [15, 18]]

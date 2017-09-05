class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.i = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        res = self.nums[self.i]
        self.i += 1
        return res


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_called = False
        self.peek_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peek_called:
            self.peek_value = self.iterator.next()
            self.peek_called = True
        return self.peek_value

    def next(self):
        """
        :rtype: int
        """
        if self.peek_called:
            self.peek_called = False
            return self.peek_value
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.peek_called else self.iterator.hasNext()


iter = PeekingIterator(Iterator([1, 2, 3]))
while iter.hasNext():
    val = iter.peek()  # Get the next element but not advance the iterator.
    print(val)
    print(iter.next())  # Should return the same value as [val].

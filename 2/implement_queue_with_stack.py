from copy import deepcopy


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []
        self.rs = []
        self.len = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        self.len += 1
        c = deepcopy(self.s)
        self.rs = []
        while c:
            self.rs.append(c.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        res = self.rs.pop()
        self.len -= 1
        c = deepcopy(self.rs)
        self.s = []
        while c:
            self.s.append(c.pop())
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.rs[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.len == 0


obj = MyQueue()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.s)
print(obj.pop())
print(obj.peek())
print(obj.s)
print(obj.empty())

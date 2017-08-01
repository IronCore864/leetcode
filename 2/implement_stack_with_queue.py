class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        l = len(self.q)
        self.q.append(x)
        if l > 0:
            for i in range(l):
                self.q.append(self.q.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.q)

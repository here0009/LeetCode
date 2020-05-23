class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.min_stack.append(x)

        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.min_stack) > 0: 
            self.min_stack.pop()
        return None
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0: 
            return self.min_stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return None
        else: 
            return min(self.min_stack)

        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())

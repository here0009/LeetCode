"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
Thought: we can only use the sepcified API, so methods such as append or extend may not be used
"""
class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nestedList):
            res = []
            for element in nestedList:
                if type(element) is int:
                    res.append(element)
                elif type(element) is list:
                    res.extend(flatten(element))
            return res
        self.lst = flatten(nestedList)
        self.length = len(self.lst)
        self.index = 0
        # print(self.lst)

    def next(self) -> int:
        if self.hasNext():
            v = self.lst[self.index]
            self.index += 1
            return v

    def hasNext(self) -> bool:
        return self.index < self.length


class NestedIterator:
    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    yield from gen(x.getList())
        self.gen = gen(nestedList)

    def next(self) -> int:
        return self.value

    def hasNext(self) -> bool:
        try:
            self.value = next(self.gen)
            return True
        except:
            return False


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False

# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    k = i.next()
    print(k)
    v.append(k)
print(v)
nestedList = [1,[4,[6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    k = i.next()
    print(k)
    v.append(k)
print(v)

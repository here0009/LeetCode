"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
 

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""


from typing import List
from bisect import bisect_left, insort
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = [float('inf')]
        self.right = [float('inf')]
        
    def addNum(self, val: int) -> None:
        lval, rval = val - 1, val + 1
        r_i = bisect_left(self.right, lval)
        l_i = bisect_left(self.left, rval)
        if self.right[r_i] == lval and self.left[l_i] == rval:  # merge 2 intervals
            self.left.pop(l_i)
            self.right.pop(r_i)
            return
        l_j = bisect_left(self.left, rval)
        if self.left[l_j] == rval:  # merge one num
            self.left[l_j] = val
            return
        r_j = bisect_left(self.right, lval)
        if self.right[r_j] == lval:  # merge one num
            self.right[r_j] = val
            return
        insort(self.left, val)
        insort(self.right, val)

    def getIntervals(self) -> List[List[int]]:
        res = []
        for i in range(len(self.left) - 1):
            res.append([self.left[i], self.right[i]])
        return res


from typing import List
from bisect import bisect_left, insort
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = [-float('inf'), float('inf')]
        self.right = [-float('inf'), float('inf')]

    def addNum(self, val: int) -> None:
        r_i = bisect_left(self.right, val)
        l_i = bisect_left(self.left, val)
        # print(val, l_i, r_i)
        if self.left[l_i] == val or self.right[r_i] == val or (r_i + 1 == l_i and self.right[r_i] > val and self.left[l_i - 1] < val):   # already added or in range
            return
        if r_i == l_i and self.right[r_i - 1] == val - 1 and self.left[l_i] == val + 1:
            self.left.pop(l_i)
            self.right.pop(r_i - 1)
            return
        if self.left[l_i] == val + 1:
            self.left[l_i] = val
            return
        if self.right[r_i - 1] == val - 1:
            self.right[r_i - 1] = val
            return
        insort(self.left, val)
        insort(self.right, val)

    def getIntervals(self) -> List[List[int]]:
        res = []
        for i in range(1, len(self.left) - 1):
            res.append([self.left[i], self.right[i]])
        return res
  


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
val_list = [1,3,7,2,6]
for val in val_list:
    obj.addNum(val)
    print(obj.getIntervals())

action = ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
parameters = [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]]
output = [None,None,[[6,6]],None,[[6,6]],None,[[0,0],[6,6]],None,[[0,0],[4,4],[6,6]],None,[[0,0],[4,4],[6,6],[8,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,7],[7,8]],None,[[0,0],[4,7],[7,8]]]
expected = [None,None,[[6,6]],None,[[6,6]],None,[[0,0],[6,6]],None,[[0,0],[4,4],[6,6]],None,[[0,0],[4,4],[6,6],[8,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,4],[6,8]],None,[[0,0],[4,8]]]
for i in range(len(action)):
    print(action[i], parameters[i], output[i], expected[i])



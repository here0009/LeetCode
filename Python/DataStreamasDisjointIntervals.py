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
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addNum(self, val: int) -> None:
        

    def getIntervals(self):
        


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
val_list = [1,3,7,2,6]
for val in val_list:
    obj.addNum(val)
    print(obj.getIntervals())
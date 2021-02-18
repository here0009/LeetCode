"""
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
"""


# https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


# Test
"""
from bisect import bisect_left, bisect_right
lst = []

start = bisect_left(lst, 10)
end = bisect_right(lst, 20)
print(start, end)
lst[start: end] = [10, 20]
print(lst)
start = bisect_right(lst, 13)
end = bisect_left(lst, 15)
print(start, end)

start = bisect_left(lst, 14)
end = bisect_right(lst, 16)
print(start, end)
lst[start: end] = [14, 16]
print(lst)

start = bisect_right(lst, 16)
end = bisect_left(lst, 17)
print(start, end)
"""


from bisect import bisect_left, bisect_right
class RangeModule:
    """
    Thoughts: because left < right, lef and right was always added on the track in pairs
    so if the index of a num in track is even, it stands for left.
    otherwise it stands for right
    """

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect_left(self.track, left)  # if left == self.track[start] and start % 2 == 1, use bisect_left will get the correct answer, bisect_right will get it wrong
        end = bisect_right(self.track, right)
        tmp = [left] * (start % 2 == 0) + [right] * (end % 2 == 0)
        self.track[start: end] = tmp  #lst[0:0] = [a] is equvilant to lst[0:1] = [a]

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect_right(self.track, left)
        end = bisect_left(self.track, right)
        return start == end and start % 2 == 1


    def removeRange(self, left: int, right: int) -> None:
        start = bisect_left(self.track, left)
        end = bisect_left(self.track, right)
        tmp = [left] * (start % 2 == 1) + [right] * (end % 2 == 1)
        self.track[start: end] = tmp


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
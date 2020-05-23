"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution_1:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for _s, _e in intervals[1:]:
            if _s <= end:
                end = max(end, _e)
            else:
                res.append([start, end])
                start = _s
                end = _e
        res.append([start, end])
        return res

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res



s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))

intervals = [[1,4],[4,5]]
print(s.merge(intervals))

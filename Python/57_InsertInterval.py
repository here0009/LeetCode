"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


class Solution:
    def insert(self, intervals, newInterval):
        res = []
        start, end = newInterval
        length = len(intervals)
        index = 0
        while index < length:
            i, j = intervals[index]
            if i > end:
                break
            elif j < start:
                res.append([i,j])
            else:
                start = min(i, start)
                end = max(j, end)
            index += 1
        res.append([start, end])
        res.extend(intervals[index:])
        return res


S = Solution()
intervals = [[1,1]]
newInterval = [2,5]
print(S.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(S.insert(intervals, newInterval))

intervals = []
newInterval = [5,7]
print(S.insert(intervals, newInterval))
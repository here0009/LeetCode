"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        length = len(intervals)
        if length <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # print(intervals)
        _, end = intervals[0]
        res = 0
        for i in range(1, length):
            s_i, e_i = intervals[i]
            if s_i < end:
                res += 1
                end = min(end, e_i) #remove the one got larger end
            else:
                end = e_i
        return res

S = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(S.eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(S.eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(S.eraseOverlapIntervals(intervals))
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(S.eraseOverlapIntervals(intervals))

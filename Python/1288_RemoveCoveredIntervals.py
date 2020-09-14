"""
Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
 

Constraints:

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j
"""


class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x:(x[0], -x[1]))
        res = 1
        pre = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[1] <= pre[1]:
                continue
            res += 1
            pre = curr
        return res

class Solution:
    def removeCoveredIntervals(self, A):
        res = right = 0
        A.sort(key=lambda a: (a[0], -a[1]))
        for _, j in A:
            res += j > right
            right = max(right, j)
        return res

S = Solution()
intervals = [[1,4],[3,6],[2,8]]
print(S.removeCoveredIntervals(intervals))
intervals = [[1,4],[1,8],[3,6],[2,8]]
print(S.removeCoveredIntervals(intervals))
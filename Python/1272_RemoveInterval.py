"""
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        start, end = toBeRemoved
        for i, j in intervals:
            if i < start:
                res.append([i, min(j, start)])
            if j > end:
                res.append([max(i, end), j])
        return sorted(res)


S = Solution()
intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
print(S.removeInterval(intervals, toBeRemoved))
intervals = [[0,5]]
toBeRemoved = [2,3]
print(S.removeInterval(intervals, toBeRemoved))
intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]]
toBeRemoved = [-1,4]
print(S.removeInterval(intervals, toBeRemoved))
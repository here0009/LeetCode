"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution:
    def minimumTotal(self, triangle) -> int:
        pre = triangle[0]
        curr = pre[:]
        for i in range(1,len(triangle)):
            curr = triangle[i]
            curr[0] += pre[0]
            curr[-1] += pre[-1]
            for j in range(1,len(curr)-1):
                curr[j] += min(pre[j],pre[j-1])
            # print(curr)
            pre = curr
        return min(curr)

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))

triangle = [[-10]]
print(s.minimumTotal(triangle))
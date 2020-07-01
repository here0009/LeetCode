"""
Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 

Constraints:

2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= points[i][0], points[i][1] <= 10^8
0 <= k <= 2 * 10^8
points[i][0] < points[j][0] for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
"""

import bisect
class Solution:
    """
    TLE
    """
    def findMaxValueOfEquation(self, points, k: int) -> int:
        def cal(i, j):
            xi, yi = points[i]
            xj, yj = points[j]
            return abs(xj - xi) + yi + yj

        length = len(points)
        res = float('-inf')
        for left in range(length - 1):
            xi, yi = points[left]
            index = bisect.bisect_right(points, [xi+k, float('inf')])
            # print(left, index)
            for right in range(left+1, index):
                res = max(res, cal(left, right))
        return res


from collections import deque
class Solution:
    """
    yi + yj + |xi - xj|, since xj > xi, the equation is yj + xj + yi - xi, so we want to keep the largest the value of yi - xi and try others js to see if we can get a larger value
    """
    def findMaxValueOfEquation(self, points, k: int) -> int:
        dq = deque()  # [x, y-x]
        res = float('-inf')
        for x, y in points:
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                res = max(res, dq[0][1] + y + x)
            while dq and dq[-1][1] <= y - x:
                dq.pop()
            dq.append([x, y-x])
        return res
                
                
import heapq
class Solution:
    """
    yi + yj + |xi - xj|, since xj > xi, the equation is yj + xj + yi - xi, so we want to keep the largest the value of yi - xi and try others js to see if we can get a larger value
    """
    def findMaxValueOfEquation(self, points, k: int) -> int:
        hp = []   #(-(y-x), x)
        res = float('-inf')
        for x, y in points:
            while hp and x - hp[0][1] > k:
                heapq.heappop(hp)
            if hp:
                res = max(res, -1*hp[0][0] + x + y)
            heapq.heappush(hp, (x-y, x))
        return res




S = Solution()
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(S.findMaxValueOfEquation(points, k))
points = [[0,0],[3,0],[9,2]]
k = 3
print(S.findMaxValueOfEquation(points, k))

"""
You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of points on a 2D plane. 

Return the maximum number of points that are within or lie on any circular dartboard of radius r.

 

Example 1:



Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
Example 2:



Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
Example 3:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
Example 4:

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
 

Constraints:

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
"""


from typing import List
from math import sqrt
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def dist(x1, y1, x2, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        def calcCircle(x1, y1, x2, y2):
            d = dist(x1, y1, x2, y2)
            q = sqrt(r**2 - (d / 2)**2)
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            x3, y3 = (x1 + x2)/2, (y1 + y2)/2
            tx, ty = dy / d * q, dx / d * q
            return [(x3 - tx, y3 + ty), (x3 + tx, y3 - ty)]

        min_v = 1E-6
        len_p = len(points)
        res = 1
        for i in range(len_p - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len_p):
                x2, y2 = points[j]
                if dist(x1, y1, x2, y2) <= 2 * r + min_v:
                    c1, c2 = calcCircle(x1, y1, x2, y2)
                    res = max(res, sum(dist(c1[0], c1[1], x, y) <= r + min_v for x, y in points))
                    res = max(res, sum(dist(c2[0], c2[1], x, y) <= r + min_v for x, y in points))
        return res

S = Solution()
points = [[-2,0],[2,0],[0,2],[0,-2]]
r = 2
print(S.numPoints(points, r))
points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
r = 5
print(S.numPoints(points, r))
points = [[-2,0],[2,0],[0,2],[0,-2]]
r = 1
print(S.numPoints(points, r))
points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]]
r = 2
print(S.numPoints(points, r))

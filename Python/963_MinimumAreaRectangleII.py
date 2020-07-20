"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
"""


from math import sqrt
class Solution:
    def minAreaFreeRect(self, points) -> float:
        def dotProduct(i, j, k):
            """
            return lines of points[i]-points[j] and points[k]-points[i] is perpendicular
            """
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            return (x3 - x1)*(x2 - x1) + (y3 - y1)*(y2 - y1) == 0

        def lastPoints(i, j, k):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            return x3 + (x2 - x1), y3 + (y2 - y1)

        def area(i, j, k):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            return sqrt((x2 - x1)**2 + (y2 - y1)**2) * sqrt((x3 - x1)**2 + (y3 - y1)**2)

        points_set = set(map(tuple, points))
        print(points_set)
        length = len(points)
        res = float('inf')
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if dotProduct(i,j,k) and lastPoints(i,j,k) in points_set:
                        res = min(res, area(i,j,k))
        return res if res != float('inf') else 0

import math
from collections import defaultdict
class Solution:
    def minAreaFreeRect(self, P) -> float:
        if len(P) < 4:return 0
        
        def dis(A, B):
            return (A[0]-B[0])**2 + (A[1]-B[1])**2
        
        D = defaultdict(lambda:[])
        ans = math.inf
        for i in range(len(P)-1):
            for j in range(i+1, len(P)):
                D[dis(P[i], P[j])].append(((P[i][0], P[i][1]), (P[j][0],P[j][1])))
        
        for d in D:
            for i in range(len(D[d])-1):
                for j in range(i+1, len(D[d])):
                    if dis(D[d][i][0], D[d][j][0]) == dis(D[d][i][1], D[d][j][1]):
                        if dis(D[d][i][0], D[d][j][1]) == dis(D[d][i][1], D[d][j][0]):
                            ans = min(ans, dis(D[d][i][0], D[d][j][0])*dis(D[d][i][0], D[d][j][1]))

        return math.sqrt(ans) if ans != float('inf') else 0


# https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/208351/Python-Complex
from collections import defaultdict
from itertools import combinations
class Solution:
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in sorted(points)]
        print(points)
        seen = defaultdict(list)
        for P, Q in combinations(points, 2):
            seen[Q - P].append((P + Q) / 2)
        print(seen)
        ans = float("inf")
        for A, candidates in seen.items():
            for P, Q in combinations(candidates, 2):
                if A.real * (P - Q).real == -A.imag * (P - Q).imag:
                    ans = min(ans, abs(A) * abs(P - Q))
        return ans if ans < float("inf") else 0

# https://leetcode.com/articles/minimum-area-rectangle-ii/
"""
Intuition

Consider opposite points AC and BD of a rectangle ABCD. They both have the same center O, which is the midpoint of AC and the midpoint of AB; and they both have the same radius dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D). Notice that a necessary and sufficient condition to form a rectangle with two opposite pairs of points is that the points must have the same center and radius.

Motivated by that result, let's classify each pair of points PQ by their center C = the midpoint of PQ, and the radius r = dist(P, C). Our strategy is to brute force on pairs of points with the same classification.

Algorithm

For each pair of points, classify them by center and radius. We only need to record one of the points P, since the other point is P' = 2 * center - P (using vector notation).

For each center and radius, look at every possible rectangle (two pairs of points P, P', Q, Q'). The area of this rectangle dist(P, Q) * dist(P, Q') is a candidate answer.
"""
from collections import defaultdict
from itertools import combinations
class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = defaultdict(list)
        for P, Q in combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))
        return ans if ans < float("inf") else 0


S = Solution()
points = [[1,2],[2,1],[1,0],[0,1]]
print(S.minAreaFreeRect(points))
points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
print(S.minAreaFreeRect(points))
points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
print(S.minAreaFreeRect(points))
points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
print(S.minAreaFreeRect(points))

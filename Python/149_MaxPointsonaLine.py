"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


from math import gcd
from collections import defaultdict
from collections import Counter
from functools import reduce
class Solution_1:
    def maxPoints(self, points) -> int:
        length = len(points)
        if length < 2:
            return length
        lines = defaultdict(set)
        for i in range(length):
            xi, yi = points[i]
            for j in range(i+1, length):
                xj, yj = points[j]
                if xi == xj:
                    a, b, c = 1, 0, -xi # equation x + x1 = 0
                else:
                    a, b, c = yj - yi, xi - xj, xj * yi - xi * yj
                    if a < 0:
                        a, b, c = -a, -b, -c
                    g = reduce(gcd, (a, b, c))
                    a, b, c = a//g, b//g, c//g
                # reduce fraction
                lines[(a,b,c)].add(i) #y = kx+b; flag,dx,dy represent k and m represent b
                lines[(a,b,c)].add(j)

        # print(lines)
        res = max([len(l) for l in lines.values()])
        return res



from math import gcd
from collections import defaultdict
from collections import Counter
class Solution:
    """
    we can just try to calculate the points formed a line with a fixed point
    Yes, my first thought was similar to yours. I stored a pair, which was the slope and y-intercept to uniquely define a single line, then check each line with all points, totally O(n^3).

But actually, better solution just needs the slope (O(n^2)). The key points are following:

There will be a fixed point (let's say A). Then we can choose another point (B or C or D) to define a single line (AB or AC or AD). If AB and AC have the same slope, then B and C must be on the same line.

The map is temporary in a single loop. For each fixed point, we will start with a cleared map, so there is no interference between any rounds.

After we used point A, we can just abandon it, since we have counted all the lines that contain A.

Corner cases are: (1) vertical line without slope. (2) duplicate point.

Hope it makes sense.
    """
    def maxPoints(self, points) -> int:
        def reduce_gcd(dx, dy):
            if dx == 0 and dy == 0:
                return 0, 0
            flag = dx*dy < 0
            g = gcd(abs(dx), abs(dy))
            dx, dy = dx//g, dy//g
            if not flag:
                dx = -dx
            return dx, dy

        length = len(points)
        if length < 2:
            return length
        res = 0
        for i in range(length):
            xi, yi = points[i]
            counts = 1
            lines = Counter()
            for j in range(i+1, length):
                xj, yj = points[j]
                if (xi, yi) == (xj, yj):
                    counts += 1
                    continue
                dx, dy = xi - xj, yi - yj
                dx, dy = reduce_gcd(dx, dy)
                lines[(dx, dy)] += 1

            res = max(res, counts + max(list(lines.values()) + [0]))
        return res


class Solution_2(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(a, b):
            return gcd(b % a, a) if a != 0 else b
        pointsInLine = {}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    a, b, c = 1, 0, -x1
                else:
                    a, b, c = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
                    if a < 0:
                        a, b, c = -a, -b, -c
                    g = reduce(gcd, (a, b, c))
                    a, b, c = a / g, b / g, c / g
                line = (a, b, c)
                pointsInLine.setdefault(line, set())
                pointsInLine[line].add(i)
                pointsInLine[line].add(j)
        print(pointsInLine)
        return max(map(len, pointsInLine.values())) if pointsInLine else len(points)

S = Solution_1()
points = [[4,4],[1,1],[2,2],[3,3]]
print(S.maxPoints(points))
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(S.maxPoints(points))
points = [[0,0],[0,0]]
print(S.maxPoints(points))
points = [[1,1],[2,1],[2,2],[1,4],[3,3]]
print(S.maxPoints(points))
points = [[15,12],[9,10],[-16,3],[-15,15],[11,-10],[-5,20],[-3,-15],[-11,-8],[-8,-3],[3,6],[15,-14],[-16,-18],[-6,-8],[14,9],[-1,-7],[-1,-2],[3,11],[6,20],[10,-7],[0,14],[19,-18],[-10,-15],[-17,-1],[8,7],[20,-18],[-4,-9],[-9,16],[10,14],[-14,-15],[-2,-10],[-18,9],[7,-5],[-12,11],[-17,-6],[5,-17],[-2,-20],[15,-2],[-5,-16],[1,-20],[19,-12],[-14,-1],[18,10],[1,-20],[-15,19],[-18,13],[13,-3],[-16,-17],[1,0],[20,-18],[7,19],[1,-6],[-7,-11],[7,1],[-15,12],[-1,7],[-3,-13],[-11,2],[-17,-5],[-12,-14],[15,-3],[15,-11],[7,3],[19,7],[-15,19],[10,-14],[-14,5],[0,-1],[-12,-4],[4,18],[7,-3],[-5,-3],[1,-11],[1,-1],[2,16],[6,-6],[-17,9],[14,3],[-13,8],[-9,14],[-5,-1],[-18,-17],[9,-10],[19,19],[16,7],[3,7],[-18,-12],[-11,12],[-15,20],[-3,4],[-18,1],[13,17],[-16,-15],[-9,-9],[15,8],[19,-9],[9,-17]]
print(S.maxPoints(points))
points = [[0,0],[-1,-1],[2,2]]
print(S.maxPoints(points))
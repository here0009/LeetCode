"""
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

 

Example 1:

Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:

Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
 

Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """
        find the points got min_y, set it as the start point.
        sweep a line of angle 0, set the 1st met point as new start point. the line between pre start point and current point as new line, sweep the line counter-clockwise.
        meet another point. iterater the process, untill we met the point of ymin. 
        then the search is completed
        hard to implement the rotation of the line
        """
        pass
# Monotone Chain Algorithm

# https://leetcode.com/problems/erect-the-fence/discuss/103306/C%2B%2B-and-Python-easy-wiki-solution
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """
        we can use right hand rule to calculate the direction of the product a * b,
        1st finger a, 2nd finger b, thumb will be a*b.
        if a*b is up then rotate a->b is counter-clockwise, otherwise, it is clockwise
        """
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

        points.sort()
        ups = []
        for p in points:
            while len(ups) > 1 and cross(ups[-2], ups[-1], p) < 0:
                ups.pop()
            ups.append(p)
        lows = []
        for p in points[::-1]:
            while len(lows) > 1 and cross(lows[-2], lows[-1], p) < 0:
                lows.pop()
            lows.append(p)
        # print(ups, lows)
        res = list(set(tuple(lst) for lst in ups + lows))
        return sorted(list(t) for t in res)


# Java Graham scan
from typing import Tuple
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """
        although it pass all test cases, it is wrong for the test case 
        points =  [[0,0],[1,1],[2,2],[3,3],[1,2]]
        because the colinear problem
        wrong answer
        """
        def slope(a, b) -> Tuple[int]:
            if a[0] == b[0]:
                return float('inf'), 1
            return b[1] - a[1], b[0] - a[0]

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        start = min(points)
        points.pop(points.index(start))
        slope_dict = dict()
        for p in points:
            d = dist(p, start)
            s = slope(start, p)
            if s not in slope_dict or d > slope_dict[s][0]:
                slope_dict[s] = (d, p)

        print(slope_dict)
        print('start', start)
        keys = sorted(slope_dict.keys(), key=lambda x: (x[0] / x[1]))
        print(keys)
        print([slope_dict[key] for key in keys])
        res = [start]
        for key in keys:
            _, p = slope_dict[key]
            while len(res) > 1 and cross(res[-2], res[-1], p) < 0:
                res.pop()
            res.append(p)
        return res


from collections import namedtuple
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        # Computes the cross product of vectors p1p2 and p2p3
        # value of 0 means points are colinear; < 0, cw; > 0, ccw
        point = namedtuple("point","x y")
        points = [point(e[0],e[1]) for e in points]
        def cross(p1, p2, p3):
            return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

        # Computes slope of line between p1 and p2
        def slope(p1, p2):
            return 1.0*(p1.y-p2.y)/(p1.x-p2.x) if p1.x != p2.x else float('inf')

        # distance of p1 and p2
        def dis(p1, p2):
            return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
        
        # Find the smallest left point and remove it from points
        start = min(points, key=lambda p: (p.x, p.y))
        points.pop(points.index(start))

        # Sort points so that traversal is from start in a ccw circle.
        points_slopes = [(p, slope(p, start)) for p in points]
        points_slopes.sort(key=lambda e: e[1])
        points = []
        i = 0
        for j in range(1,len(points_slopes)):
            if points_slopes[j][1] != points_slopes[i][1]:
                if j-i == 1:
                    points.append(points_slopes[i])
                else:
                    points_cl = sorted(points_slopes[i:j], key=lambda e: dis(start, e[0]))
                    points.extend(points_cl)
                i = j
        points_cl = sorted(points_slopes[i:], key=lambda e: -dis(start, e[0]))
        points.extend(points_cl)
        points = [p[0] for p in points]

        # Add each point to the convex hull.
        # If the last 3 points make a cw turn, the second to last point is wrong. 
        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(ans[-3], ans[-2], ans[-1]) < 0:
                ans.pop(-2)
        return [[p.x, p.y] for p in ans]


S = Solution()
# points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# print(S.outerTrees(points))
# points = [[1,2],[2,2],[4,2]]
# print(S.outerTrees(points))
# points = [[0,0],[1,1],[2,2],[3,3],[1,2]]
# print(S.outerTrees(points))
points = [[5,5],[4,8],[1,3],[5,9],[3,0],[0,4],[3,2],[8,9],[9,3]]
print(S.outerTrees(points))
# Output
# [[0,4],[3,0],[9,3],[8,9],[5,9]]
# Expected
# [[9,3],[5,9],[4,8],[3,0],[0,4],[8,9]]
# sorted points: [[3, 0], [1, 3], [3, 2], [9, 3], [5, 5], [8, 9], [5, 9], [4, 8]]
"""
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

 

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
 

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convex-polygon
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# https://blog.csdn.net/sunbobosun56801/article/details/78980467


class Solution:
    def isConvex(self, points) -> bool:
        points = points + points[:2]
        pre = 0
        for i in range(len(points)-2):
            x1, y1 = points[i+1][0]-points[i][0], points[i+1][1]-points[i][1]
            x2, y2 = points[i+2][0]-points[i][0], points[i+2][1]-points[i][1]
            curr = x1*y2 - x2*y1
            print(pre, curr, points[i])
            if curr != 0:
                if curr*pre < 0:
                    return False
                pre = curr
        return True

S = Solution()
points = [[0,0],[0,1],[1,1],[1,0]]
print(S.isConvex(points))
points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
print(S.isConvex(points))
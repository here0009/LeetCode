"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""
class Solution:
    def isBoomerang(self, points) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]: #same point
            return False
        if points[0][0] == points[1][0] and points[0][0] == points[2][0]: #same line, cannot calculated by the fourth if
            return False
        if points[0][0] == points[1][0] or points[0][0] == points[2][0] or points[1][0] == points[2][0]: #two points got same x(but different y because the 1st if), the thrid one got different x(because the 2nd if), so they are valid boomerang
            return True
        if (points[1][1] - points[0][1])/(points[1][0] - points[0][0]) == (points[2][1] - points[0][1])/(points[2][0] - points[0][0]): #same line
            return False

        return True

s = Solution()
points = [[1,1],[2,3],[3,2]]
print(s.isBoomerang(points))

points = [[1,1],[2,3],[1,1]]
print(s.isBoomerang(points))

points = [[1,1],[2,2],[3,3]]
print(s.isBoomerang(points))

points = [[1,1],[1,2],[1,3]]
print(s.isBoomerang(points))

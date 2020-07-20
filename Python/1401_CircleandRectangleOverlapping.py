"""
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.

 

Example 1:



Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0) 
Example 2:



Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
Example 3:



Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
Output: true
Example 4:

Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
 

Constraints:

1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2
"""

from math import sqrt
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        wrong answer
        """
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for di,dj in directions:
            xi,xj = x_center + di*radius, y_center + dj*radius
            if x1 <= xi <= x2 and y1 <= xj <= y2:
                return True
        for x, y in [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]:
            if sqrt((x - x_center)**2 + (y - y_center)**2) <= radius:
                return True
        return False

from math import sqrt
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        move the coordinate, x_center, y_center is (0,0)
        """
        x1 -= x_center
        y1 -= y_center
        x2 -= x_center
        y2 -= y_center
        minX = min(x1**2, x2**2) if x1*x2 > 0 else 0
        minY = min(y1**2, y2**2) if y1*y2 > 0 else 0
        return minX + minY <= radius**2

        
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = 0 if x1 <= x_center <= x2 else min(abs(x1-x_center), abs(x2-x_center))
        y = 0 if y1 <= y_center <= y2 else min(abs(y1-y_center), abs(y2-y_center))
        return x**2 + y**2 <= radius**2

S = Solution()

radius = 1
x_center = 0
y_center = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1
print(S.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
radius = 1
x_center = 0
y_center = 0
x1 = -1
y1 = 0
x2 = 0
y2 = 1
print(S.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
radius = 1
x_center = 1
y_center = 1
x1 = -3
y1 = -3
x2 = 3
y2 = 3
print(S.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
radius = 1
x_center = 1
y_center = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1
print(S.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
radius = 5
x_center = 8
y_center = 8
x1 = 9
y1 = 5
x2 = 12
y2 = 8
print(S.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
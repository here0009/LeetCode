"""
(This problem is an interactive problem.)

On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example :



Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 

Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:

class Point(object):
  def __init__(self, x: int, y: int):
      self.x = x
      self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def countX(x, y1, y2):
            if not sea.hasShips(Point(y2, x), Point(y1,x)):
                return 0
            if y1 == y2:
                return int(sea.hasShips(Point(x, y1), Point(x, y1)))
            if y2 - y1 == 1:
                return sea.hasShips(Point(x, y1), Point(x, y1)) + sea.hasShips(Point(x, y2), Point(x, y2))
            mid = (y1 + y2)//2
            return countX(x, y1, mid) + countX(x, mid, y2) - countX(x, mid, mid)

        def countY(y, x1, x2):
            if not sea.hasShips(Point(y, x2), Point(y, x1)):
                return 0
            if x1 == x2:
                return int(sea.hasShips(Point(x1, y), Point(x1, y)))
            if x2 - x1 == 1:
                return sea.hasShips(Point(x1, y), Point(x1, y)) + sea.hasShips(Point(x2, y), Point(x2, y))
            mid = (x1 + x2)//2
            return countY(y, x1, mid) + countY(y, mid, x2) - countY(y, mid, mid)

        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        print((x1, y1), (x2, y2))
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if x1 == x2 and y1 == y2:
            return 1
        if x2 - x1 == 1 and y2 - y1 == 1:
            return sea.hasShips(bottomLeft, bottomLeft) + sea.hasShips(topRight, topRight) + sea.hasShips(Point(x1, y2), Point(x1, y2)) + sea.hasShips(Point(x2, y1), Point(x2, y1))
        if x1 == x2:
            return self.countX(x1, y1, y2)
        if y1 == y2:
            return self.counY(y1, x1, x2)

        mid_x = (x1 + x2)//2
        mid_y = (y1 + y2)//2
        midPoint = Point(mid_x, mid_y)
        return self.countShips(sea, midPoint, bottomLeft) + self.countShips(sea, topRight, midPoint) + self.countShips(sea, Point(mid_x, y2), Point(x1, mid_y)) + self.countShips(sea, Point(x2, mid_y), Point(mid_x, y1)) - countX(mid_x, y1, y2) - countY(mid_y, x1, x2) - int(sea.hasShips(midPoint, midPoint))




# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle/solution/python-by-intoloop-19/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight,bottomLeft):return 0
        xl,yl,xr,yr=bottomLeft.x,bottomLeft.y,topRight.x,topRight.y
        x,y=(xl+xr)//2,(yl+yr)//2

        if xl==xr and yl==yr:return 1
        elif xl==xr:return self.countShips(sea,Point(x,y),Point(x,yl))+self.countShips(sea,Point(x,yr),Point(x,y+1))
        elif yl==yr:return self.countShips(sea,Point(x,y),Point(xl,y))+self.countShips(sea,Point(xr,y),Point(x+1,y))
        else:return self.countShips(sea,Point(x,y),Point(xl,yl))+self.countShips(sea,Point(x,yr),Point(xl,y+1))+self.countShips(sea,Point(xr,y),Point(x+1,yl))+self.countShips(sea,Point(xr,yr),Point(x+1,y+1))

 

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        we should split from the mid point instead of minus the coutShips of mid point.
        think the grid is discrete rather than continous
        """
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        x1, y1, x2, y2 = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
        if x1 == x2 and y1 == y2:
            return 1
        mid_x = (x1 + x2)//2
        mid_y = (y1 + y2)//2
        if x1 == x2:
            return self.countShips(sea, Point(x1, mid_y), bottomLeft) + self.countShips(sea, topRight, Point(x1, mid_y +1))
        if y1 == y2:
            return self.countShips(sea, Point(mid_x, y1), bottomLeft) + self.countShips(sea, topRight, Point(mid_x+1, y1))

        return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + self.countShips(sea, topRight, Point(mid_x+1, mid_y+1)) + self.countShips(sea, Point(mid_x, y2), Point(x1, mid_y+1)) + self.countShips(sea, Point(x2, mid_y), Point(mid_x+1, y1))

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle/solution/ju-xing-nei-chuan-zhi-de-shu-mu-by-leetcode-soluti/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft):
            return 0

        if (x1, y1) == (x2, y2):
            return 1

        xmid = (x1 + x2) // 2
        ymid = (y1 + y2) // 2
        return self.countShips(sea, Point(xmid, ymid), Point(x2, y2)) + \
               self.countShips(sea, Point(xmid, y1), Point(x2, ymid + 1)) + \
               self.countShips(sea, Point(x1, ymid), Point(xmid + 1, y2)) + \
               self.countShips(sea, Point(x1, y1), Point(xmid + 1, ymid + 1))


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point', claim: bool=False) -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        if x1 < x2 or y1 < y2:
            return 0

        judge = True if claim else sea.hasShips(topRight, bottomLeft)
        if not judge:
            return 0
        if (x1, y1) == (x2, y2):
            return 1

        if x1 == x2:
            ymid = (y1 + y2) // 2
            A = self.countShips(sea, Point(x1, ymid), Point(x1, y2))
            return A + self.countShips(sea, Point(x1, y1), Point(x1, ymid + 1), A == 0)
        else:
            xmid = (x1 + x2) // 2
            A = self.countShips(sea, Point(xmid, y1), Point(x2, y2))
            return A + self.countShips(sea, Point(x1, y1), Point(xmid + 1, y2), A == 0)


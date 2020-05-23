"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""
class Solution_1:
    def minKnightMoves(self, x, y):
        x2,x1 = divmod(x,2)
        y2,y1 = divmod(y,2)
        print(x2,x1)
        print(y2,y1)
        return max(x2,y1) + max(x1,y2)


class Solution:
    def minKnightMoves(self, x, y):
        if x < y:
            x,y = y,x
        if x //y >= 2:
            return x//2
        else:
            x2,x1 = divmod(x,2)
            y2,y1 = divmod(y,2)
            return max(x2,y1) + max(x1,y2)


class Solution:
    def minKnightMoves(self, x, y):
        if x < y:
            x,y = y,x
        counts = 0
        while x != 0 or y != 0:
            print(x,y)
            if x - y == 3:
                x += 1
                y += 2
            else:
                if abs(x) >= 2*abs(y):
                    if x > 0:
                        x -= 2
                    else:
                        x += 2
                    if y > 0:
                        y -= 1
                    else:
                        y += 1
                else:
                    if x > 0:
                        x -= 1
                    else:
                        x += 1
                    if y > 0:
                        y -= 2
                    else:
                        y += 2
            counts += 1
        return counts

s = Solution()
# x = 2
# y = 1
# print(s.minKnightMoves(x,y))

x = 5
y = 5
print(s.minKnightMoves(x,y))

# x = 2
# y = 112
# print(s.minKnightMoves(x,y))

# x = 217
# y = 47
# print(s.minKnightMoves(x,y))
"""
Output:
108
Expected:
110
"""

# x = 130
# y = -86
# print(s.minKnightMoves(x,y))
"""
Output:
92
Expected:
72
"""
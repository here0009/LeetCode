"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def isValid(x,y):
            return 0<=x<m and 0<=y<n

        res = 0
        pos = [(i,j)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while N > 0:
            print(pos)
            next_pos = []
            for x,y in pos:
                for dx,dy in directions:
                    x2, y2 = x+dx, y+dy
                    if isValid(x2, y2):
                        next_pos.append((x2,y2))
                    else:
                        res += 1
            pos = next_pos
            N -= 1
        return res

s = Solution()
# print(s.findPaths(2,2,2,0,0))
# print(s.findPaths(1,3,3,0,1))
print(s.findPaths(10,10,11,5,5))       
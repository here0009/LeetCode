"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

 

Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]


 

Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


 

Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""
class Solution_1:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        def inRange(i,j):
            return i>=0 and i<R and j>=0 and j<C

        total = R*C
        res = [[r0,c0]]
        counts = 1
        si,sj = r0,c0
        length = 1
        while counts < total:
            si, sj, length = si-1, sj+1, length+2 #update start point and length of the square, si,sj represents the northeast coordinate of the square
            out_layer = []
            out_layer.extend([[i,sj] for i in range(si+1,si+length) if inRange(i,sj)]) #right
            out_layer.extend([[si+length-1,j] for j in range(sj-1,sj-length,-1) if inRange(si+length-1,j)]) #bottom
            out_layer.extend([[i,sj-length+1] for i in range(si,si+length-1)[::-1] if inRange(i,sj-length+1)] ) #left
            out_layer.extend([[si,j] for j in range(sj,sj-length+1,-1)[::-1] if inRange(si,j)]) #top
            extend_length = min(len(out_layer),total-counts)
            res.extend(out_layer[:extend_length])
            counts += extend_length
        return res

# from math import atan2
# class Solution_2:
#     def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
#         def absAngle((x,y)):
#             #sort x,y 1st by distance to r0, c0, then by angle to r0,c0
#             return (max(abs(x-c),abs(y-c), atan2(y-r0,x-c0)))

#         return sorted([(i,j) for i in range(R) for j in range(C)], key = absAngle)
from math import pi
from math import atan2
class Solution_2:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        #sort x,y 1st by distance to r0, c0, then by angle to r0,c0
        res = sorted([[i,j] for i in range(R) for j in range(C)], key = lambda x: (max(abs(x[0]-r0),abs(x[1]-c0)), -((atan2(-1,1)-atan2(x[0]-r0,x[1]-c0))%(2*pi))))
        print(res)
        for i,j in res:
            # print(i,j)
            print(i,j, 'length',max(abs(i-r0),abs(j-c0)), 'angle',-((atan2(-1,1)-atan2(i-r0,j-c0))%(2*pi)))
        return res


from math import pi
from math import atan2
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        #sort x,y 1st by distance to r0, c0, then by angle to r0,c0, the angle (1,-1) is the largest one (the northeast direction)
        return sorted([[i,j] for i in range(R) for j in range(C)], key = lambda x: (max(abs(x[0]-r0),abs(x[1]-c0)), -((atan2(-1,1)-atan2(x[0]-r0,x[1]-c0))%(2*pi))))

# class Solution_3:
#     def spiralMatrixIII(self, R, C, r, c):
#         def key((x, y)):
#             x, y = x - r, y - c
#             return (max(abs(x), abs(y)), -((math.atan2(-1, 1) - math.atan2(x, y)) % (math.pi * 2)))
#         return sorted([(i, j) for i in xrange(R) for j in xrange(C)], key=key)
S = Solution()
R = 1
C = 4
r0 = 0
c0 = 0
print(S.spiralMatrixIII(R,C,r0,c0))


R = 5
C = 6
r0 = 1
c0 = 4
print(S.spiralMatrixIII(R,C,r0,c0))


R = 3
C = 3
r0 = 2
c0 = 0
print(S.spiralMatrixIII(R,C,r0,c0))

# Output
# [[2,0],[2,1],[1,0],[1,1],[2,2],[0,0],[0,1],[0,2],[1,2]]
# Expected
# [[2,0],[2,1],[1,0],[1,1],[1,2],[2,2],[0,0],[0,1],[0,2]]

# -((math.atan2(-1, 1) - math.atan2(x, y)) % (math.pi * 2))
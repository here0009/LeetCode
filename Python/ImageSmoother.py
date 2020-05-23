"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""
import math
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        directions = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        m,n = len(M), len(M[0])
        M_res = [row[:] for row in M]
        for i in range(m):
            for j in range(n):
                surrounding = [M[di][dj] for di in (i-1,i,i+1) for dj in (j-1,j,j+1) if inRange(di,dj)]
                M_res[i][j] = math.floor(sum(surrounding)/len(surrounding))
                # counts = 1
                # # M_res
                # for di,dj in directions:
                #     if inRange(i+di,j+dj):
                #         counts += 1
                #         M_res[i][j] += M[i+di][j+dj]
                # M_res[i][j] = math.floor(M_res[i][j]/counts)
        # for row in M_res:
        #     print(row)
        return M_res

s = Solution()
M = [[1,1,1],[1,0,1],[1,1,1]]
print(s.imageSmoother(M))

M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(s.imageSmoother(M))
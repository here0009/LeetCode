"""
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
"""
class Solution_1:
    def largest1BorderedSquare(self, grid) -> int:
        def check(start_x, start_y, end_x, end_y, max_len):
            if sum(grid[x][end_y-1] for x in range(start_x, end_x)) == max_len and sum(grid[x][start_y] for x in range(start_x, end_x)) == max_len and sum(grid[end_x-1][start_y:end_y]) == max_len:
                return max_len
            else:
                return check(start_x, start_y, end_x-1, end_y-1, max_len-1)


        def maxLen(start_x, start_y,length):
            # print(start_x,start_y)
            """
            return the largest boarder square start with(left corner) x,y
            """
            tmp_y = start_y
            while tmp_y < N and grid[start_x][tmp_y] == 1:
                tmp_y += 1
            max_len =  min(tmp_y - start_y, M - start_x)
            end_x = start_x + max_len
            end_y = start_y + max_len
            # print('maxLen',start_x,start_y,max_len)
            # print('end_x,M:',end_x,M)
            if max_len <= res:
                return 0
            return check(start_x, start_y, end_x, end_y, max_len)
                
        M,N = len(grid),len(grid[0])
        res = 0
        for i in range(M):
            if res >= M -i:
                    break
            for j in range(N):
                if res >= N -j:
                    break
                if grid[i][j] == 1:
                    res = max(res, maxLen(i,j,res))
                # print('pos',i,j)
                # print('res',res)
                # print('RES',maxLen(i,j,res))
        return res**2

class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        """
        the solution from leetcode, more fast
        """
        M,N = len(grid),len(grid[0])
        res = 0
        horizontal = [[0]*N for _ in range(M)]
        vertical = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if i > 0:
                        horizontal[i][j] = horizontal[i-1][j]+1
                    else:
                        horizontal[i][j] = grid[i][j]
                    if j > 0:
                        vertical[i][j] = vertical[i][j-1]+1
                    else:
                        vertical[i][j] = grid[i][j]

        # print(horizontal)
        # print(vertical)
        for r in range(min(M,N), 0, -1):
            for i in range(M+1-r): #i+r-1 < M
                for j in range(N+1-r): #j+r-1 < N
                    if min(horizontal[i+r-1][j], horizontal[i+r-1][j+r-1], vertical[i][j+r-1], vertical[i+r-1][j+r-1]) >= r:
                        return r*r
        return 0




s = Solution()
grid = [[1,1,1],[1,0,1],[1,1,1]]
print(s.largest1BorderedSquare(grid))
grid = [[1,1,0,0]]
print(s.largest1BorderedSquare(grid))
grid = [[0,0,0,1]]
print(s.largest1BorderedSquare(grid))

grid = [[1,1,1,1,1,1],[1,0,1,0,1,1],[1,1,1,0,1,1],[1,1,1,1,1,1],[1,1,1,1,1,0]]
# for row in grid:
#     print(row)
print(s.largest1BorderedSquare(grid))
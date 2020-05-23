"""
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
class Solution:
    def hasValidPath(self, grid) -> bool:
        def inRange(i,j):
            return i>=0 and i<m and j>=0 and j<n

        def dfs(di,i,j):
            
            #di represent which direction the street is from

            if (i==m and j==n-1) or (i==m-1 and j==n) :
                return True
            if not inRange(i,j):
                return False
            if visited[i][j] == 1:
                return False
            visited[i][j] = 1
            g = grid[i][j]
            # print(di,i,j,grid[i][j])
            if g == 2: #vertical line
                if di == 'S' : #from south 
                    
                    return dfs('S',i-1,j)
                elif di == 'N' or di == 0:
                    return dfs('N',i+1,j)
                else:
                    return False
            elif g == 1:
                if di == 'E':
                    return dfs('E',i,j-1)
                elif di == 'W' or di == 0:
                    return dfs('W',i,j+1)
                else:
                    return False
            elif g == 3:
                if di == 'W' or di == 0:
                    return dfs('N',i+1,j)
                elif di == 'S':
                    return dfs('E',i,j-1)
                else:
                    return False
            elif g == 4:
                if di == 'E':
                    return dfs('N',i+1,j)
                elif di == 'S':
                    return dfs('W',i,j+1)
                else:
                    return False
            elif g == 5:
                if di == 'W':
                    return dfs('S',i-1,j)
                elif di == 'N':
                    return dfs('E',i,j-1)
                else:
                    return False
            elif g == 6:
                if di == 'N' or di == 0:
                    return dfs('W',i,j+1)
                elif di == 'E':
                    return dfs('S',i-1,j)
                else:
                    return False
            
        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        return dfs(0,0,0)

S = Solution()
# grid = [[2,4,3],[6,5,2]]
# print(S.hasValidPath(grid))
# grid = [[1,2,1],[1,2,1]]
# print(S.hasValidPath(grid))
# grid = [[1,1,2]]
# print(S.hasValidPath(grid))
# grid = [[1,1,1,1,1,1,3]]
# print(S.hasValidPath(grid))
# grid = [[2],[2],[2],[2],[2],[2],[6]]
# print(S.hasValidPath(grid))
grid = [[4,1],[6,1]]
print(S.hasValidPath(grid))
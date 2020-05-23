"""
the grid is a N*N matrix, so we can use a double for loop to traverse all the rows ans cols
"""
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ans = 0
        N = len(grid)
        for i in range(N):
            best_row = 0
            best_col = 0
            for j in range(N):
                if grid[i][j]:
                    ans += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row
            ans += best_col
        return ans

s = Solution()
input_big_list =[ [[1,2],[3,4]], [[1,0],[0,2]], [[1,1,1],[1,0,1],[1,1,1]], [[2,2,2],[2,1,2],[2,2,2]] ]
for input_list in input_big_list:
    print(input_list)
    print(s.projectionArea(input_list))

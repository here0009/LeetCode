from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        row, col = len(grid), len(grid[0])
        res = []
        idx = 0
        for i in range(row):
            if i % 2 == 0:
                col_range = range(col)
            else:
                col_range = range(col - 1, -1, -1)
            for j in col_range:
                if idx % 2 == 0:
                    res.append(grid[i][j])
                idx += 1
        return res
            
s = Solution()
grid = [[1,2],[3,4]]
print(s.zigzagTraversal(grid))
grid = [[2,1],[2,1],[2,1]]
print(s.zigzagTraversal(grid))
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(s.zigzagTraversal(grid))



from typing import List
from collections import defaultdict,Counter

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        diagnol_acc_counter = defaultdict(Counter)
        m, n = len(grid), len(grid[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp_counter =  diagnol_acc_counter[(i-1, j-1)].copy()
                tmp_counter[grid[i][j]] += 1
                diagnol_acc_counter[(i,j)] = tmp_counter
        for i in range(m):
            for j in range(n):
                k = min(m-i, n-j) - 1
                res[i][j] =  abs(len(diagnol_acc_counter[(i+k, j+k)] - diagnol_acc_counter[(i,j)]) - len(diagnol_acc_counter[(i-1, j-1)]))
        return res

sol = Solution()
grid = [[1,2,3],[3,1,5],[3,2,1]]
print(sol.differenceOfDistinctValues(grid))
grid = [[1]]
print(sol.differenceOfDistinctValues(grid))

"""
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 200
grid[i][j] is 0 or 1
"""


class Solution:
    def minSwaps(self, grid) -> int:
        def backZeros(lst):
            """
            count zeros from the back end
            """
            res = 0
            index = n - 1
            while index >= 0 and lst[index] == 0:
                index -= 1
                res += 1
            return res

        end_zeros = []
        n = len(grid)
        for row in grid:
            end_zeros.append(backZeros(row))
        # print(end_zeros)
        target = n - 1
        res = 0
        index = 0
        while index < n:
            # print(index, target)
            t_index = index
            while t_index < n:
                if end_zeros[t_index] >= target:
                    break
                t_index += 1
            if t_index == n:
                return -1
            for i in range(t_index, index, -1):
                end_zeros[i], end_zeros[i-1] = end_zeros[i-1], end_zeros[i]
                res += 1
            index += 1
            target -= 1
        return res


class Solution:
    def minSwaps(self, grid) -> int:
        def endZeros(lst):
            """
            count zeros from the back end
            """
            res = 0
            index = n - 1
            while index >= 0 and lst[index] == 0:
                index -= 1
                res += 1
            return res

        end_zeros = []
        n = len(grid)
        for row in grid:
            end_zeros.append(endZeros(row))

        res = 0
        index = 0
        while index < n:
            t_index = index
            while t_index < n:
                if end_zeros[t_index] >= n - 1 - index:
                    break
                t_index += 1
            if t_index == n:
                return -1
            for i in range(t_index, index, -1):
                end_zeros[i], end_zeros[i-1] = end_zeros[i-1], end_zeros[i]
            res += t_index - index
            index += 1
        return res

S = Solution()
grid = [[0,0,1],[1,1,0],[1,0,0]]
print(S.minSwaps(grid))
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
print(S.minSwaps(grid))
grid = [[1,0,0],[1,1,0],[1,1,1]]
print(S.minSwaps(grid))
grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
print(S.minSwaps(grid))
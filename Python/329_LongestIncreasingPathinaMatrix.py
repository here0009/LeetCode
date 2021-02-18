"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


from typing import List
from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inRange(i, j):
            return 0 <= i < R and 0 <= j < C

        @lru_cache(None)
        def dp(i, j):
            res = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if inRange(ni, nj) and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, dp(ni, nj))
            return 1 + res

        if not matrix:
            return 0
        R, C = len(matrix), len(matrix[0])
        res = 0
        for i in range(R):
            for j in range(C):
                res = max(res, dp(i, j))
        return res

S = Solution()
nums = [[9,9,4],[6,6,8],[2,1,1]] 
print(S.longestIncreasingPath(nums))
nums = [[3,4,5],[3,2,6],[2,2,1]] 
print(S.longestIncreasingPath(nums))

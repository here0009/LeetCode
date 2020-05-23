"""
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
from functools import lru_cache
class Solution:
    def ways(self, pizza, k: int) -> int:
        @lru_cache(None)
        def dp(i, j, num):
            """
            stands for the ways to cut pizza(left corner at pizza[i][j] , right corner at pizza[-1][-1]) into num pieces
            """
            if preSum[i][j] == 0:
                return 0
            if num == 0:
                return 1
            res = 0
            for cut_i in range(i+1, rows):
                if preSum[i][j] - preSum[cut_i][j] > 0:
                    res += dp(cut_i, j, num - 1)
            for cut_j in range(j + 1, cols):
                if preSum[i][j] - preSum[i][cut_j] > 0:
                    res += dp(i, cut_j, num - 1)
            return res % M


        M = 10**9 + 7
        rows = len(pizza)
        cols = len(pizza[0])

        preSum = [[0] * (cols + 1) for _ in range(rows+1)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                preSum[i][j] = preSum[i + 1][j] + preSum[i][j + 1] - preSum[i + 1][j + 1] + (pizza[i][j] == 'A')
        return dp(0, 0, k - 1)


S = Solution()
pizza = ["A..","AAA","..."]
k = 3
print(S.ways(pizza, k))
pizza = ["A..","AA.","..."]
k = 3
print(S.ways(pizza, k))
pizza = ["A..","A..","..."]
k = 1
print(S.ways(pizza, k))

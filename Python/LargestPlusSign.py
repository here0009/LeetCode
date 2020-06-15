"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines) -> int:
        dp = [[[0]*4 for _ in range(N)] for _ in range(N)]
        # up, left, down, right, the sum of 1s from the 4 directions
        res = 0
        mines_set = set((i,j) for i,j in mines)
        for i in range(N):
            for j in range(N):
                if (i,j) not in mines_set:
                    if i == 0:
                        dp[i][j][0] = 1
                    else:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    if j == 0:
                        dp[i][j][1] = 1
                    else:
                        dp[i][j][1] = dp[i][j-1][1] + 1

        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if (i,j) not in mines_set:
                    if i == N-1:
                        dp[i][j][2] = 1
                    else:
                        dp[i][j][2] = dp[i+1][j][2] + 1
                    if j == N-1:
                        dp[i][j][3] = 1
                    else:
                        dp[i][j][3] = dp[i][j+1][3] + 1
                    res = max(res, min(dp[i][j]))
        # for row in dp:
        #     print(row)
        return res


# https://leetcode.com/problems/largest-plus-sign/discuss/143607/Python-straightforward-simple-self-explanatory-AC-solution
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        #up, left, down, right
        dp, res, mines = [[[0, 0, 0, 0] for j in range(N)] for i in range(N)], 0, {(i, j) for i, j in mines}
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    try:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    except:
                        dp[i][j][0] = 1
                    try:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    except:
                        dp[i][j][1] = 1
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if (i, j) not in mines:
                    try:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    except:
                        dp[i][j][2] = 1
                    try:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    except:
                        dp[i][j][3] = 1
                    res = max(res, min(dp[i][j]))
        return res
S = Solution()
N = 5
mines = [[4, 2]]
print(S.orderOfLargestPlusSign(N, mines))

N = 2
mines = []
print(S.orderOfLargestPlusSign(N, mines))

N = 1
mines = [[0, 0]]
print(S.orderOfLargestPlusSign(N, mines))


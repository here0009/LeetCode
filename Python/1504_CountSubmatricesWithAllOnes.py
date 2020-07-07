"""
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5

提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""


class Solution:
    def numSubmat(self, mat) -> int:
        """
        wrong answer
        """
        m, n = len(mat), len(mat[0])
        for row in mat:
            print(row)
        print('++++++++++++')
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = max(0, dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) + 1
        for row in dp:
            print(row)
        # print([])
        print('++++++++++++')
        return sum(sum(row) for row in dp)


class Solution:
    def numSubmat(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        hist = [0]*n
        res = 0
        for row in mat:
            stack = [] #  (index, the number of submat right corner lies at mat[i][index]), non decreasing
            for j in range(n):
                hist[j] = (row[j] == 1) *(hist[j] + 1)
                while stack and hist[stack[-1][0]] > hist[j]:
                    stack.pop()
                submat = hist[j]*(j - stack[-1][0]) + stack[-1][1] if stack else hist[j]*(j+1)
                stack.append((j, submat))
                res += submat
        return res


S = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(S.numSubmat(mat))
# # 输出：13
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(S.numSubmat(mat))
# # 输出：24
mat = [[1,1,1,1,1,1]]
print(S.numSubmat(mat))
# # 输出：21
# # 示例 4：
mat = [[1,0,1],[0,1,0],[1,0,1]]
print(S.numSubmat(mat))
mat = [[0,0,0],[0,0,0],[0,1,1],[1,1,0],[0,1,1]]
print(S.numSubmat(mat))
# 输出：
# 11
# 预期：
# 12
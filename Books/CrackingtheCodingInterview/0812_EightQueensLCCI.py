"""
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/eight-queens-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def genGrid(col_idx):
            grid = [["."] * n for _ in range(n)]
            for i, j in enumerate(col_idx):
                grid[i][j] = "Q"
            return [''.join(row) for row in grid]

        def solve(col_idx):
            if len(col_idx) == n:
                self.res.append(genGrid(col_idx))
                return
            forbid = set(col_idx)
            r = len(col_idx)
            for i, j in enumerate(col_idx):
                forbid.add(i + j - r)  # antidiagnol.add(i + j)
                forbid.add(r - (i - j))  # diagnol.add(i - j)
            for c in range(n):
                if c not in forbid:
                    solve(col_idx + [c])

        self.res = []
        solve([])
        return self.res


# 作者：zhoudaxia
# 链接：https://leetcode-cn.com/problems/eight-queens-lcci/solution/python-zui-sheng-nei-cun-de-xie-fa-by-zhoudaxia/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(cols, x_d, y_d):
            j = len(cols)
            if len(cols) == n:
                res.append([''.join(row) for row in st])
            for i in range(n):
                if i not in cols and i + j not in x_d and i - j not in y_d:
                    st[j][i] = 'Q'
                    x_d.add(i + j)
                    y_d.add(i - j)
                    cols.add(i)
                    dfs(cols, x_d, y_d)
                    x_d.remove(i + j)
                    y_d.remove(i - j)
                    cols.remove(i)
                    st[j][i] = '.'
        st = [['.' for i in range(n)] for j in range(n)]
        res = []

        dfs(set(), set(), set())
        return res



S = Solution()
print(S.solveNQueens(4))



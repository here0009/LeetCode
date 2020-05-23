"""
你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。

 

输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。

输出：一个整数，代表最多能在棋盘上放的骨牌数。

 

示例 1：

输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
输出：2
解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）


 

示例 2：

输入：n = 3, m = 3, broken = []
输出：4
解释：下图是其中一种可行的摆放方式


 

限制：

1 <= n <= 8
1 <= m <= 8
0 <= b <= n * m
"""
class Solution:
    def domino(self, n: int, m: int, broken):
        """
        Thoughts: use the left corner index to represent the square
        use dp to find the max number of dominos can be placed on board
        Wrong Solution
        """
        #place an extra row and col, the extrat row and col is unaccessable, set their value to -1
        matrix = [[0]*(m+1) for _ in range (n+1)]
        for row in matrix:
            print(row)
        for i in range(n+1):
            matrix[i][0] = -1 #1st col
        for j in range(m+1):
            matrix[0][j] = -1 #1st row
        for i,j in broken:
            matrix[i+1][j+1] = -1
        for row in matrix:
            print(row)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i][j] != -1:
                    if matrix[i-1][j] == -1:
                        tmp_i = 0
                    elif i > 1: #i = 1, tmp_i = 0
                        tmp_i = matrix[i-2][j] + 1
                    if matrix[i][j-1] == -1:
                        tmp_j = 0
                    elif j > 1:
                        tmp_j = matrix[i][j-2] + 1
                    matrix[i][j] = max(tmp_i, tmp_j)
        for row in matrix:
            print(row)
        return

s = Solution()
n = 2
m = 3
broken = [[1, 0], [1, 1]]
print(s.domino(n,m,broken))

n = 3
m = 3
broken = []
print(s.domino(n,m,broken))
"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""
class Solution:
    """
    flip row to make col[0] to 1
    flip col 1~n to make sum(row[i]) max
    """
    def matrixScore(self, A) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                A[i] = [1-A[i][j] for j in range(n)]
        # for row in A:
        #     print(row)
        # print("============")
        for j in range(1,n):
            k = sum(A[i][j] for i in range(m))
            # print(k,m/2)
            if k < m/2:
                for i in range(m):
                    A[i][j] = 1-A[i][j]
        # for row in A:
        #     print(row)
        res = 0
        for row in A:
            # print(int(''.join([str(i) for i in row]),2))
            res += int(('0b'+''.join([str(i) for i in row])),2)
        # print(res)
        return res

s = Solution()
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(s.matrixScore(A))

A = [[0,1],[0,1],[0,1],[0,0]]
print(s.matrixScore(A))


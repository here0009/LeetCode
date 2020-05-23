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
    def matrixScore(self, A) -> int:
        """
        Thoughts:
        flip the row if col 1 is 0
        flip the col if more 1 than 1 in the col
        """
        M,N = len(A), len(A[0])

        res = 0
        for i in range(M): #row i
            if A[i][0] == 0:
                for j in range(N):
                    A[i][j] = 1 - A[i][j]
        # print(A)
        for j in range(1,N): #col j
            if sum(row[j] for row in A) <= M //2:
                for i in range(M):
                    A[i][j] = 1 - A[i][j]
        # print(A)
        for i in range(M):
            b = int(''.join([str(s) for s in A[i]]),2)
            res += b
        return res

s = Solution()
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(s.matrixScore(A))

A = [[0,1],[0,1],[0,1],[0,0]]
print(s.matrixScore(A))
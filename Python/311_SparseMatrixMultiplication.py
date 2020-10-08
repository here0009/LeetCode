"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sparse-matrix-multiplication
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def multiply(self, A, B):
        R_a, C_a = len(A), len(A[0])
        R_b, C_b = len(B), len(B[0])
        if C_a != R_b:
            return None
        matrix = [[0]*C_b for _ in range(R_a)]

        for k in range(R_b):
            for i in range(R_a):
                if A[i][k] != 0:
                    for j in range(C_b):
                        if B[k][j] != 0:
                            matrix[i][j] += A[i][k]*B[k][j]
        # for row in matrix:
        #     print(row)
        return matrix

S = Solution()
A = [[ 1, 0, 0],[-1, 0, 3]] 
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]
print(S.multiply(A, B))
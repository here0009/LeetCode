"""You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
"""


from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        for i in range(1, R):
            matrix[i][0] = matrix[i][0] ^ matrix[i - 1][0]
        for j in range(1, C):
            matrix[0][j] = matrix[0][j] ^ matrix[0][j - 1]
        for i in range(1, R):
            for j in range(1, C):
                matrix[i][j] = matrix[i][j] ^ matrix[i - 1][j] ^ matrix[i][j - 1] ^ matrix[i - 1][j -1]
        vals = []
        for row in matrix:
            vals.extend(row)
        vals.sort()
        return vals[-k]

S = Solution()
matrix = [[5,2],[1,6]]
k = 1
print(S.kthLargestValue(matrix, k))

matrix = [[5,2],[1,6]]
k = 2
print(S.kthLargestValue(matrix, k))

matrix = [[5,2],[1,6]]
k = 3
print(S.kthLargestValue(matrix, k))

matrix = [[5,2],[1,6]]
k = 4

print(S.kthLargestValue(matrix, k))

matrix = [[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]]
k = 2
print(S.kthLargestValue(matrix, k))
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""


from typing import List
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)
        res = []
        for i in range(R):
            for j in range(C):
                diagonals[i + j].append(matrix[i][j])
        # print(diagonals)
        for key in sorted(diagonals.keys()):
            if key % 2 == 1:
                res.extend(diagonals[key])
            else:
                res.extend(diagonals[key][::-1])
        return res

S  = Solution()
matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print(S.findDiagonalOrder(matrix))

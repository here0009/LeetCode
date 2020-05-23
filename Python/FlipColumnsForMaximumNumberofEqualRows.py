"""
Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
All matrix[i].length's are equal
matrix[i][j] is 0 or 1
"""
class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        counts = {}
        for row in matrix:
            row_str = ''.join([str(i) for i in row])
            rev_row_str = ''.join([str(1-i) for i in row])
            counts[row_str] = counts.get(row_str,0)+1
            counts[rev_row_str] = counts.get(rev_row_str,0)+1
        return max(counts.values())


class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        counts = {}
        for row in matrix:
            row_str = str([i^row[0] for i in row])  #if row[0] is 1, flip the row, if row[0] is 0, stay the same
            counts[row_str] = counts.get(row_str,0)+1
        # print(counts)
        return max(counts.values())

s = Solution()
# matrix =[[0,1],[1,1]]
# print(s.maxEqualRowsAfterFlips(matrix))
matrix = [[0,0,0],[0,0,1],[1,1,0]]
print(s.maxEqualRowsAfterFlips(matrix))

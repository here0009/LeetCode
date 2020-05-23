"""
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

 

Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:

Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
Example 3:

Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 

Constraints:

1 <= colsum.length <= 10^5
0 <= upper, lower <= colsum.length
0 <= colsum[i] <= 2
"""
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum):
        if upper + lower != sum(colsum):
            return []
        len_c = len(colsum)
        res = [[0]*len_c for _ in range(2)]
        counts_2 = sum([n==2 for n in colsum])
        upper -= counts_2
        lower -= counts_2
        if upper < 0 or lower < 0:
            return []
        for index in range(len_c):
            c = colsum[index]
            if c == 2:
                res[0][index] = 1
                res[1][index] = 1
            elif c == 1:
                if upper > 0:
                    res[0][index] = 1
                    upper -= 1
                elif lower > 0:
                    res[1][index] = 1
                    lower -= 1
                else:
                    return []
        return res

s = Solution()
upper = 2
lower = 1
colsum = [1,1,1]
print(s.reconstructMatrix(upper, lower, colsum))

upper = 2
lower = 3
colsum = [2,2,1,1]
print(s.reconstructMatrix(upper, lower, colsum))

upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]
print(s.reconstructMatrix(upper, lower, colsum))
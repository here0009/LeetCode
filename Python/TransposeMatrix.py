"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        # if row == 1 and col == 1:
        #     return A

        transpose_A = []
        for k in range(col):
            transpose_A.append([0] * row)

        # print(transpose_A)
        # transpose_A = [[0] * row] * col
        # the second multiply is shallow copy, so  can not use it to initilise transpose_A,  use double for loop or single for loop for 0 assignment
        for i in range(row):
            for j in range(col):
                transpose_A[j][i] = A[i][j]

        return transpose_A


"""
Recommended solution 1
"""
class Solution_1:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return list(zip(*A))

"""
Recommended solution 2
"""
class Solution_2:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


# s = Solution()

# s = Solution_1()
s = Solution_2()

test = [[1,2,3],[4,5,6],[7,8,9]]
print(s.transpose(test))

test = [[1,2,3],[4,5,6]]
print(s.transpose(test))

test = [[1],[2],[3]]
print(s.transpose(test))

test = [[1,2,3]]
print(s.transpose(test))

test = [[3]]
print(s.transpose(test))
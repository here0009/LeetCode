"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j], and the line we draw does not intersect any other connecting (non-horizontal) line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
"""
class Solution:
    """
    It is the same question to find the maximum equal subarray in A&B
    """
    def maxUncrossedLines(self, A, B) -> int:
        len_A = len(A)
        len_B = len(B)
        score_matrix = [[0]*len_B for _ in range(len_A)]
        for i in range(len_A):
            if A[i] == B[0]:
                score_matrix[i][0] = 1
        for j in range(len_B):
            if A[0] == B[j]:
                score_matrix[0][j] = 1
        # print(score_matrix)
        for i in range(1,len_A):
            for j in range(1,len_B):
                if A[i] == B[j]:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1]+1)
                else:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1])
        # print(score_matrix)

        return max([max(row) for row in score_matrix])

class Solution:
    """
    It is the same question to find the maximum equal subarray in A&B
    """
    def maxUncrossedLines(self, A, B) -> int:
        len_A = len(A)+1
        len_B = len(B)+1
        score_matrix = [[0]*len_B for _ in range(len_A)]
        # print(score_matrix)
        for i in range(1,len_A):
            for j in range(1,len_B):
                if A[i-1] == B[j-1]:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1]+1)
                else:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1])
        # print(score_matrix)

        # return max([max(row) for row in score_matrix])
        return score_matrix[len_A-1][len_B-1]

class Solution:
    """
    It is the same question to find the maximum equal subarray in A&B
    """
    def maxUncrossedLines(self, A, B) -> int:
        len_A = len(A)
        len_B = len(B)
        score_matrix = [[0]*len_B for _ in range(len_A)]
        # print(score_matrix)
        for i in range(len_A):
            for j in range(len_B):
                if A[i] == B[j]:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1]+1)
                else:
                    score_matrix[i][j] = max(score_matrix[i-1][j],score_matrix[i][j-1],score_matrix[i-1][j-1])
        # print(score_matrix)

        # return max([max(row) for row in score_matrix])
        return score_matrix[len_A-1][len_B-1]

s = Solution()
A = [1,4,2]
B = [1,2,4]
print(s.maxUncrossedLines(A,B))

A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
print(s.maxUncrossedLines(A,B))

A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
print(s.maxUncrossedLines(A,B))

A = [1]
B = [1,3]
print(s.maxUncrossedLines(A,B))

A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
print(s.maxUncrossedLines(A,B))

A = [3,2]
B = [2,2,2,3]
print(s.maxUncrossedLines(A,B))


"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index, l in enumerate(A):
            l = l[::-1]
            # print(l)
            l = self.invert_list(l)
            # print(l)
            A[index] = l
        return A
        
    def invert_list(self, l):
        """
        : type l : list
        : rtype list
        : change the element in l, from 0 to 1, from 1 to 0
        """
        for index, num in enumerate(l):
            if num == 0:
                l[index] = 1
            else:
                l[index] = 0
        return l


s = Solution()

A = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(A))
# print(s.invert_list([1,1,0]))

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(A))
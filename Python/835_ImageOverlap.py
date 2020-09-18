"""
You are given two images img1 and img2 both of size n x n, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We slide img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3. (Shown in red)

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
 

Constraints:

n == img1.length
n == img1[i].length
n == img2.length
n == img2[i].length
1 <= n <= 30
img1[i][j] is 0 or 1.
img2[i][j] is 0 or 1.
"""


class Solution:
    def largestOverlap(self, A, B) -> int:
        """
        thought: brute force, slide A and calculate the overlap with B, slide B and calculate the overlap with A. (only right down)
        """
        def overlap(m1, m2, r, c):
            """
            the left top of m1 is r, c
            """
            res = 0
            for i in range(n-r):
                for j in range(n-c):
                    if m1[i+r][j+c] == m2[i][j] == 1:
                        res += 1
            return res

        totalB = sum(sum(row) for row in B)
        res = 0
        n = len(A)
        for r in range(n):
            for c in range(n):
                tmp = 1
                if (n-r)*(n-c) <= res:
                    break
                res = max(res, overlap(A, B, r, c), overlap(B, A, r, c))
        return res
# https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward
from collections import Counter
class Solution:
    def largestOverlap(self, A, B) -> int:
        """
        calculate the relative position of A and B
        """
        n = len(A)
        LA = [(i,j) for i in range(n) for j in range(n) if A[i][j]==1]
        LB = [(i,j) for i in range(n) for j in range(n) if B[i][j]==1]
        counter = Counter()
        for ia, ja in LA:
            for ib, jb in LB:
                counter[(ia-ib, ja-jb)] += 1
        return max(counter.values()) if counter else 0

from scipy.ndimage import convolve
import numpy as np

class Solution:
    def largestOverlap(self, A, B):
        B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
        return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))

class Solution:
    def largestOverlap(self, A, B) -> int:

        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps

class Solution:
    def largestOverlap(self, A, B) -> int:

        dim = len(A)
        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == R[r_row][r_col] == 1:
                        left_shift_count += 1
                    if M[m_row][r_col] == R[r_row][m_col] == 1:
                        right_shift_count += 1
            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B), shift_and_count(x_shift, y_shift, B, A))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions 
                # max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps
S = Solution()
A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]
print(S.largestOverlap(A, B))
A = [[1]]
B = [[1]]
print(S.largestOverlap(A, B))
A = [[0]]
B = [[0]]
print(S.largestOverlap(A, B))
A = [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
B = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]
print(S.largestOverlap(A, B))

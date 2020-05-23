"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
class Solution_1:
    def kthSmallest(self, matrix, k: int) -> int:
        """
        wrong answer
        """
        row,col = len(matrix), len(matrix[0])
        r,c = divmod(k,col)
        if c == 0:
            r -= 1
        return matrix[r][c-1]

from math import sqrt
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        len_m = len(matrix)
        sqrt_k = int(sqrt(k))
        if k == sqrt_k**2:
            return matrix[sqrt_k-1][sqrt_k-1]
        row,j = sqrt_k, 0
        col,i = sqrt_k, 0     
        k -= sqrt_k**2
        print(row,col)
        while k > 0:
            if j < len_m and matrix[row][j] <= matrix[i][col]:
                res= matrix[row][j]
                j += 1
            else:
                res =  matrix[i][col]
                i += 1
            k -= 1
        return res

import heapq
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        def push(i,j):
            if i < n and j < n:
                heapq.heappush(queue, (matrix[i][j],i,j))

        n = len(matrix)
        counts = 0
        queue = []
        push(0,0)
        while counts < k:
            res, i,j = heapq.heappop(queue)
            push(i,j+1)
            if j == 0:
                push(i+1,j)
            counts += 1
        return res

from bisect import bisect_right
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        lo,hi = matrix[0][0], matrix[-1][-1]
        while True:
            mid = (lo + hi) //2
            counts = sum(bisect_right(row, mid) for row in matrix)
            if counts <  k:
                lo = mid + 1
            elif counts > k:
                hi = mid - 1
            else:
                return mid
        return None


from bisect import bisect_right
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        lo,hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) //2
            counts = sum(bisect_right(row, mid) for row in matrix)
            if counts <  k:
                lo = mid + 1
            else:
                hi = mid
        return lo #return lower bound, which is  in matrix, the previous soltion may return a value not in the matrix

S = Solution()
matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k = 8
print(S.kthSmallest(matrix,k))

matrix = [[0]]
k = 1
print(S.kthSmallest(matrix,k))

matrix = [[1,2],[1,3]]
k = 2
print(S.kthSmallest(matrix,k))
"""
Output
2
Expected
1
"""

matrix =[[1,3,5],[6,7,12],[11,14,14]]
k = 3
print(S.kthSmallest(matrix,k))
# Output
# 6
# Expected
# 5
"""
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

 

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
 

Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
"""

import heapq
from collections import deque
class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        R, C = len(mat), len(mat[0])
        diff_mat = [deque([0]*C) for _ in range(R)] #record the diff value of 2 adjecent elment in a row
        for i in range(R): 
            for j in range(C-1):
                diff_mat[i][j] = mat[i][j+1] - mat[i][j]

        for row in diff_mat:
            print(row)
        res = sum(mat[i][0] for i in range(R))
        pq = []
        heapq.heapify(pq)
        for i in range(R): #reverse the list, so pop small element first, the last one is 'inf', so it won't be poped
            diff_mat[i][-1] = float('inf') 
            # print(i, diff_mat[i])
            heapq.heappush(pq, (diff_mat[i].popleft(), i))

        for row in diff_mat:
            print(row)
        print(pq)
        while k > 1:
            val, index = heapq.heappop(pq)
            res += val
            print('v,i,r', val, index, res,pq)
            heapq.heappush(pq, (diff_mat[index].popleft(), index))

        return res


import heapq
class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        # print("++++++++++")
        # for row in mat:
        #     print(row)
        # print("++++++++++")
        R, C = len(mat), len(mat[0])
        visited = set()
        res = sum(mat[i][0] for i in range(R))
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (res, [0]*R))
        visited.add(tuple([0]*R))
        while k > 0 and pq:
            res, lst = heapq.heappop(pq)
            for i, j in enumerate(lst):
                if j+1 < C:
                    lst2 = lst[:i]+[j+1]+lst[i+1:]
                    if tuple(lst2) not in visited:
                        visited.add(tuple(lst2))
                        heapq.heappush(pq, (res+mat[i][j+1]-mat[i][j], lst2))
            k -= 1
        return res


class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
            # print(h)
        return h[k-1]
S = Solution()
mat = [[1,3,11],[2,4,6]]
k = 5
print(S.kthSmallest(mat, k))
mat = [[1,3,11],[2,4,6]]
k = 9
print(S.kthSmallest(mat, k))
mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7
print(S.kthSmallest(mat, k))
mat = [[1,1,10],[2,2,9]]
k = 7
print(S.kthSmallest(mat, k))
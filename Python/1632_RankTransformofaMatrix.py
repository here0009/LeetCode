"""
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

If an element is the smallest element in its row and column, then its rank is 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.

 

Example 1:


Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
Example 2:


Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]
Example 3:


Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
Example 4:


Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-109 <= matrix[row][col] <= 109
"""


import heapq
class Solution:
    def matrixRankTransform(self, matrix):
        """
        priority queue store the elements of matrix
        dict to store the rank information
        got wrong answer for some test cases, when elemnts got the same values
        """
        for _row in matrix:
            print(_row)

        R, C = len(matrix), len(matrix[0])
        pq = []
        res = [[0]*C for _ in range(R)]
        c_rank, r_rank = dict(), dict()
        for i in range(R):
            for j in range(C):
                v = matrix[i][j]
                heapq.heappush(pq, (v, i, j))
                if i not in r_rank or v < r_rank[i][0]:
                    r_rank[i] = (v, 1)
                if j not in c_rank or v < c_rank[j][0]:
                    c_rank[j] = (v, 1)

        while pq:
            v, i, j = heapq.heappop(pq)
            rv, rr = r_rank[i]
            cv, cr = c_rank[j]
            rr += rv < v
            cr += cv < v
            rank = max(rr, cr)
            res[i][j] = rank
            r_rank[i] = (v, rank)
            c_rank[j] = (v, rank)

        for _row in res:
            print(_row)


        return res


import heapq
class Solution:
    def matrixRankTransform(self, matrix):
        """
        priority queue store the elements of matrix
        dict to store the rank information
        for the elements that got the same value, we need to store their rank information
        still wrong
        """
        R, C = len(matrix), len(matrix[0])
        total_rank = [[0]*C for _ in range(R)]
        for (i, lst) in enumerate(matrix):
            lst = sorted(zip(lst, range(C)))
            rank = 0
            pre_v, pre_j = lst[0]
            total_rank[i][pre_j] += rank
            for v, j in lst[1:]:
                rank += v != pre_v
                total_rank[i][j] += rank
                pre_v = v

        for _row in matrix:
            print(_row)
        print('+++++++++++++++++++')
        trans_matrix = [list(lst) for lst in zip(*matrix)]
        for _row in trans_matrix:
            print(_row)
        print('+++++++++++++++++++')
        for (j, lst) in enumerate(trans_matrix):
            lst = sorted(zip(lst, range(R)))
            rank = 0
            pre_v, pre_i = lst[0]
            total_rank[pre_i][j] += rank
            for v, i in lst[1:]:
                rank += v != pre_v
                total_rank[i][j] += rank
                pre_v = v

        for _row in total_rank:
            print(_row)
        print('+++++++++++++++++++')
        pq = []
        res = [[0]*C for _ in range(R)]
        c_rank, r_rank = dict(), dict()
        for i in range(R):
            for j in range(C):
                v = matrix[i][j]
                heapq.heappush(pq, (v, -total_rank[i][j], i, j))
                if i not in r_rank or v < r_rank[i][0]:
                    r_rank[i] = (v, 1)
                if j not in c_rank or v < c_rank[j][0]:
                    c_rank[j] = (v, 1)

        # print(pq)
        while pq:
            
            v, _, i, j = heapq.heappop(pq)
            print(v, _, i,j)
            rv, rr = r_rank[i]
            cv, cr = c_rank[j]
            rr += rv < v
            cr += cv < v
            tmp = max(rr, cr)
            res[i][j] = tmp
            r_rank[i] = (v, tmp)
            c_rank[j] = (v, tmp)

        for _row in res:
            print(_row)
        print('+++++++++++++++++++')

        return res


import heapq
class Solution:
    def matrixRankTransform(self, matrix):
        """
        priority queue store the elements of matrix
        dict to store the rank information
        got wrong answer for some test cases, when elemnts got the same values
        """

        R, C = len(matrix), len(matrix[0])
        pq = []
        res = [[0]*C for _ in range(R)]
        c_rank, r_rank = dict(), dict()
        for i in range(R):
            for j in range(C):
                v = matrix[i][j]
                heapq.heappush(pq, (v, i, j))
                if i not in r_rank or v < r_rank[i][0]:
                    r_rank[i] = (v, 1)
                if j not in c_rank or v < c_rank[j][0]:
                    c_rank[j] = (v, 1)

        while pq:
            v, i, j = heapq.heappop(pq)
            rv, rr = r_rank[i]
            cv, cr = c_rank[j]
            rr += rv < v
            cr += cv < v
            rank = max(rr, cr)
            res[i][j] = rank
            r_rank[i] = (v, rank)
            c_rank[j] = (v, rank)

        for _row in res:
            print(_row)


        return res


# https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/909142/Python-Union-Find
from collections import defaultdict
class Solution:
    def matrixRankTransform(self, A):
        m, n = len(A), len(A[0])
        rank = [0] * (m + n)
        res = [[0]*n for _ in range(m)]
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[A[i][j]].append([i, j])

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        for a in sorted(d):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j + m)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                v = rank2[find(i)] + 1
                res[i][j] = v
                rank[i] = rank[j + m] = v 
        return res


from collections import defaultdict
class Solution:
    def matrixRankTransform(self, A):
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        def union(i,j,lst):
            ri, rj = find(i), find(j)
            if ri != rj:
                p[ri] = rj
            lst[rj] = max(lst[ri], lst[rj])

        m, n = len(A), len(A[0])
        rank = [0] * (m + n)
        res = [[0]*n for _ in range(m)]
        vals_dict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                vals_dict[A[i][j]].append([i, j])

        for val in sorted(vals_dict):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in vals_dict[val]:
                union(i, j+m, rank2)
            for i, j in vals_dict[val]:
                v = rank2[find(i)] + 1
                res[i][j] = v
                rank[i] = rank[j + m] = v
        return res

S = Solution()
matrix = [[1,2],[3,4]]
print(S.matrixRankTransform(matrix))
matrix = [[7,7],[7,7]]
print(S.matrixRankTransform(matrix))
matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
print(S.matrixRankTransform(matrix))
matrix = [[7,3,6],[1,4,5],[9,8,2]]
print(S.matrixRankTransform(matrix))
matrix = [[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]
print(S.matrixRankTransform(matrix))

# 输出：
# [[2,1,3,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]
# 预期：
# [[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]

matrix =[[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
print(S.matrixRankTransform(matrix))

matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
print(S.matrixRankTransform(matrix))

# 输出：
# [[5,2,3],[1,3,4],[6,1,7],[1,3,4]]
# 预期结果：
# [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
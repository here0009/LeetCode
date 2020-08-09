"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
"""


from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths):
        res = [0] * (1 + N)
        edges = defaultdict(list)
        for i, j in paths:
            edges[i].append(j)
            edges[j].append(i)

        for i in range(1, 1+N):
            colors = set(range(1,5))
            adj_color = set(res[j] for j in edges[i])
            rmd_color = colors - adj_color
            res[i] = rmd_color.pop()
        return res[1:]

S = Solution()
N = 3
paths = [[1,2],[2,3],[3,1]]
print(S.gardenNoAdj(N, paths))
N = 4
paths = [[1,2],[3,4]]
print(S.gardenNoAdj(N, paths))
N = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(S.gardenNoAdj(N, paths))
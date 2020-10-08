"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countComponents(self, n: int, edges) -> int:
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i,j):
            ri,rj = find(i), find(j)
            if ri == rj:
                return False
            root[ri] = rj
            return True

        root = dict()
        for i in range(n):
            root[i] = i
        res = n
        for i, j in edges:
            if union(i,j):
                res -= 1
        return res


S = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(S.countComponents(n, edges))
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(S.countComponents(n, edges))

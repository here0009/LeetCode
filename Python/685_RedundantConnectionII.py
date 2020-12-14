"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""


from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        wrong answer
        """
        def dfs(i):
            visited[i] = 1
            for j in edges_dict[i]:
                if not visited[j]:
                    dfs(j)

        res = None
        edges_dict = defaultdict(set)
        for u,v in edges:
            visited = defaultdict(int)
            dfs(u)
            if visited[v] == 1:
                res = [u,v]
            edges_dict[u].add(v)
        return res


from typing import List
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        wrong answer, it is a directed graph
        try to record the indegree and outdegree, find the nodes that got indegree > 1 or outdegree > 2
        """
        def find(i):
            if root[i] != i:
                ri = find(root[i])
                root[i] = ri
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            if ri != rj:
                root[rj] = ri
            return True

        res = None
        N = len(edges)
        root = list(range(N + 1))
        for i, j in edges:
            if find(i) == find(j):
                return [i, j]
            else:
                union(i, j)
        return res
        
s = Solution()
edges = [[1,2], [1,3], [2,3]]
print(s.findRedundantDirectedConnection(edges))


edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(s.findRedundantDirectedConnection(edges))

# edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]
# print(s.findRedundantDirectedConnection(edges))

edges = [[2,1],[3,1],[4,2],[1,4]]
print(s.findRedundantDirectedConnection(edges))
# Output
# [1,4]
# Expected
# [2,1]
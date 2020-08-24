"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:



Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
 

Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
"""


from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        def dfs(node):
            visited[node] = 1
            for j in edges_dict[node]:
                if j in res:
                    res.remove(j)
                if not visited[j]:
                    dfs(j)
        
        visited = [0]*n
        res = set()
        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
        for i in range(n):
            if visited[i] == 0:
                res.add(i)
                dfs(i)
        return list(res)

# Nodes with no In-Degree
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        return list(set(range(n)) - set(j for i,j in edges))

S = Solution()
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(S.findSmallestSetOfVertices(n, edges))
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(S.findSmallestSetOfVertices(n, edges))
n = 3
edges = [[1,2],[1,0],[0,2]]
print(S.findSmallestSetOfVertices(n, edges))
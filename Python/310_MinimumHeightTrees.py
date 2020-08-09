"""
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \\ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""


from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        """
        TLE
        """
        def dfs(node):
            visited[node] = 1
            res = 0
            for next_node in edges_dict[node]:
                if not visited[next_node]:
                    res = max(res, dfs(next_node)+1)
            return res

        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
        
        self.min_height = n + 1
        self.res = []
        for i in range(n):
            visited = [0] * n
            h = dfs(i)
            if h == self.min_height:
                self.res.append(i)
            elif h < self.min_height:
                self.min_height = h
                self.res = [i]
        return self.res



from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        """
        TLE
        """
        def dfs(node):
            visited[node] = 1
            res = 0
            for next_node in edges_dict[node]:
                if not visited[next_node]:
                    res = max(res, dfs(next_node)+1)
                    if res > self.min_height:
                        return float('inf')
            return res

        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
        
        self.min_height = n + 1
        self.res = []
        for i in range(n):
            visited = [0] * n
            h = dfs(i)
            if h == self.min_height:
                self.res.append(i)
            elif h < self.min_height:
                self.min_height = h
                self.res = [i]
        return self.res

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        def dfs(node):
            visited[node] = 1
            res = 0
            for next_node in edges_dict[node]:
                if not visited[next_node] and matrix[node][next_node] == 0:
                    tmp = dfs(next_node) + 1
                    matrix[node][next_node] = tmp
                    matrix[next_node][node] = tmp
                    res = max(res, tmp)
            return res

        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
        
        self.res = []
        self.max_height = n + 1
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            visited = [0] * n
            dfs(i)
            print(i)
            for row in matrix:
                print(row)

        for i in range(n):
            tmp = max(matrix[i])
            if tmp == self.max_height:
                self.res.append(i)
            elif tmp < self.max_height:
                self.max_height = tmp
                self.res = [i]

        return self.res


from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        edges_dict = defaultdict(set)
        for i, j in edges:
            edges_dict[i].add(j)
            edges_dict[j].add(i)
        nodes = set(range(n))
        while len(nodes) > 2:
            leaves = set(i for i in nodes if len(edges_dict[i]) == 1)
            nodes -= leaves
            for i in leaves:
                for j in edges_dict[i]:
                    edges_dict[j].remove(i)
        return list(nodes)

# https://leetcode.com/problems/minimum-height-trees/discuss/269060/Python-Topological
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        edges_dict = defaultdict(set)
        for i, j in edges:
            edges_dict[i].add(j)
            edges_dict[j].add(i)
        q = [i for i in range(n) if len(edges_dict[i]) < 2]
        next_q = []
        while True:
            for i in q:
                for j in edges_dict[i]:
                    edges_dict[j].remove(i)
                    if len(edges_dict[j]) == 1:
                        next_q.append(j)
            if not next_q:
                break
            q, next_q = next_q, []
        return q

S = Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
print(S.findMinHeightTrees(n, edges))
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(S.findMinHeightTrees(n, edges))
"""
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
Example 2:


Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.
 

Constraints:

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.
"""


from typing import List
from itertools import combinations
from collections import Counter
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        """
        TLE 67 / 68
        """
        edges_dict = Counter()
        edges_set = set()
        nodes = list(range(1, n + 1))
        for p, q in edges:
            edges_dict[p] += 1
            edges_dict[q] += 1
            edges_set.add((p, q))
            edges_set.add((q, p))

        res = float('inf')
        # print(edges_dict)
        # print(nodes)

        for comb in combinations(nodes, 3):
            p, q, r = comb
            # print(p, q, r)
            if (p, q) in edges_set and (p, r) in edges_set and (q, r) in edges_set:
                res = min(res, sum([edges_dict[p] + edges_dict[q] + edges_dict[r]]) - 6) 
        return res if res != float('inf') else -1



from collections import Counter
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = Counter()
        edges_set = set()
        nodes = list(range(1, n + 1))
        for p, q in edges:
            edges_dict[p] += 1
            edges_dict[q] += 1
            edges_set.add((p, q))
            edges_set.add((q, p))

        res = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in edges_set:
                    for k in range(j + 1, n):
                        if (i, k) in edges_set and (j, k) in edges_set:
                            res = min(res, sum([edges_dict[i] + edges_dict[j] + edges_dict[k]]) - 6)
        return res if res != float('inf') else -1


from collections import Counter
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = Counter()
        edges_set = set()
        for p, q in edges:
            edges_dict[p] += 1
            edges_dict[q] += 1
            edges_set.add((p, q))
            edges_set.add((q, p))

        n += 1
        res = float('inf')
        for i in range(1, n):
            for j in range(i + 1, n):
                if (i, j) in edges_set:
                    for k in range(j + 1, n):
                        if (i, k) in edges_set and (j, k) in edges_set:
                            res = min(res, sum([edges_dict[i] + edges_dict[j] + edges_dict[k]]) - 6)
        return res if res != float('inf') else -1


from collections import defaultdict, Counter
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = defaultdict(set)
        counts = Counter()
        for p, q in edges:
            counts[p] += 1
            counts[q] += 1
            if p > q:
                edges_dict[p].add(q)
            else:
                edges_dict[q].add(p)

        res = float('inf')
        for i in range(1, n + 1):
            for j in edges_dict[i]:
                ks = edges_dict[i] & edges_dict[j]
                for k in ks:
                    res = min(res, sum(counts[_node] for _node in [i, j, k]) - 6)
                    if res == 0:
                        break
        return res if res != float('inf') else -1


from collections import defaultdict, Counter
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        matrix = [[0] * (n + 1) for _ in range(n + 1)]
        counts = Counter()
        for p, q in edges:
            counts[p] += 1
            counts[q] += 1
            matrix[p][q] = 1
            matrix[q][p] = 1

        res = float('inf')
        for i in range(1, n + 1):
            if res == 0:
                break
            for j in range(i + 1, n + 1):
                if matrix[i][j] == 1:
                    for k in range(j + 1, n + 1):
                        if matrix[i][k] == matrix[j][k] == 1:
                            res = min(res, sum(counts[_node] for _node in [i, j, k]) - 6)
        return res if res != float('inf') else -1


S = Solution()
n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
print(S.minTrioDegree(n, edges))
n = 7
edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
print(S.minTrioDegree(n, edges))

n = 4
edges = [[1,2],[4,1],[4,2]]
print(S.minTrioDegree(n, edges))
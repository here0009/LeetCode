"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000
"""


from typing import List
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        TLE
        """
        dist = [[float('inf')] * N for _ in range(N)]
        for i, j in edges:
            dist[i][j] = 1
            dist[j][i] = 1
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N - 1):
                for j in range(i + 1, N):
                    m = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[i][j] = dist[j][i] = m
        # for row in dist:
        #     print(row)
        return [sum(row) for row in dist]


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        Thoughts:
        we can calulate from root to leaves
        calculate the children number under a node and total distance of it's root
        then dist[node] = dist[root] - children[node] + (N - 2 -children[node])
        2 for the node itself and its root
        wrong answer, works for directed graph, but the given graph is undirected
        the caluclation of dist in function dfs is wrong
        dist shoud equal to c + d(that is previous dist + number of nodes in subtree), not 2*d + 1
        """
        def dfs(node):
            """
            return the children number and total distance under node
            """
            # if node   0, 0
            
            chd_num, dist = 1, 0
            for nxt in edges_list[node]:
                c, d = dfs(nxt)
                chd_num += c
                dist += 2 * d + 1
            children[node] = chd_num - 1
            # print(node, chd_num, dist)
            return chd_num, dist

        def dist(node, pre):
            res[node] = pre
            for nxt in edges_list[node]:
                dist(nxt, pre - children[nxt] + (N - 2 - children[nxt]))


        edges_list = defaultdict(list)
        nodes = set()
        for i, j in edges:
            edges_list[i].append(j)
            nodes.add(j)
        root = (set(range(N)) - nodes).pop()
        # print(root, edges_list)
        children = [0] * N
        total = dfs(root)[1]
        # print(children, total)
        res = [0] * N
        dist(root, total)
        # print(res)
        return res

from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        Thoughts:
        we can calulate from root to leaves
        calculate the children number under a node and total distance of it's root
        then dist[node] = dist[root] - children[node] + (N - 1 -children[node])
        2 for the node itself and its root
        """
        def dfs(node):
            """
            return the children number and total distance under node
            """
            visited.add(node)
            chd_num, dist = 1, 0
            for nxt in edges_list[node]:
                if nxt not in visited:
                    c, d = dfs(nxt)
                    chd_num += c
                    dist += c + d
            children[node] = chd_num - 1
            return chd_num, dist

        def dist(node, pre):
            res[node] = pre
            visited.add(node)
            for nxt in edges_list[node]:
                if nxt not in visited:
                    dist(nxt, pre - children[nxt] + (N - 2 - children[nxt]))

        edges_list = defaultdict(list)
        for i, j in edges:
            edges_list[i].append(j)
            edges_list[j].append(i)

        children = [0] * N
        visited = set()
        total = dfs(0)[1]
        res = [0] * N
        visited = set()
        dist(0, total)
        return res

# https://leetcode.com/problems/sum-of-distances-in-tree/solution/
"""
take the node itself in its subtree, then compared to node with its parent
node is also one step closer(1 -> 0), parent was one step away(0 -> 1)
"""
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        dfs(0, None)
        dfs2(0, None)
        return ans


S = Solution()
N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(S.sumOfDistancesInTree(N, edges))
N = 2
edges = [[0,1]]
print(S.sumOfDistancesInTree(N, edges))
N = 1
edges = []
print(S.sumOfDistancesInTree(N, edges))
N = 3
edges = [[2,0],[1,0]]
# """
# undirecte graph, how to find root, 
# any node can be root, we choose 0, do not influence the results
# use bidirection edges and visited set
# """
print(S.sumOfDistancesInTree(N, edges))

N = 4
edges = [[1,2],[3,2],[3,0]]
print(S.sumOfDistancesInTree(N, edges))
"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""


from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        edges_prob = defaultdict(list)
        max_prob_dict = dict() #  store the max probability from start to n
        for i in range(len(edges)):
            s, e = edges[i]
            p = succProb[i]
            edges_prob[s].append((-p, e))
            edges_prob[e].append((-p, s))
        # print(edges_prob)
        visited = set()

        heapq.heapify(edges_prob[start])
        hp = edges_prob[start]
        # print(edges_prob[start])
        # print(hp)
        while hp:
            # print(hp)
            prob, node = heapq.heappop(hp)
            if node not in visited:
                visited.add(node)
                if node == end:
                    return -prob

            for p, e in edges_prob[node]:
                if e not in visited:
                    pre = max_prob_dict.get(e, float('-inf'))
                    nxt = prob * p
                    if nxt > pre:
                        max_prob_dict[e] = nxt
                        heapq.heappush(hp, (-nxt, e))
        return 0

# https://leetcode.com/problems/path-with-maximum-probability/discuss/731538/Python-O(len(edges)-*-log(n))-Dijkstra's-Algorithm-with-explanations.
from heapq import heappush, heappop
from math import log2
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        AdjList = [set() for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            AdjList[u].add((v, log2(1/p)))
            AdjList[v].add((u, log2(1/p)))
        dist = [float('inf') for _ in range(n)]
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, u = heappop(h)
            if d == dist[u]:
                for (v, p) in AdjList[u]:
                    if dist[u] + p < dist[v]:
                        dist[v] = dist[u] + p
                        heappush(h, (dist[v], v))
        return 1 / (2 ** dist[end])

        
S = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(S.maxProbability(n, edges, succProb, start, end))
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2
print(S.maxProbability(n, edges, succProb, start, end))
n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2
print(S.maxProbability(n, edges, succProb, start, end))

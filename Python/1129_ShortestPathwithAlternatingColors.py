"""
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
 

Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""


from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        res = [-1]*n
        red = [0]
        blue = [0]
        red_dict = defaultdict(list)
        blue_dict = defaultdict(list)
        for u,v in red_edges:
            red_dict[u].append(v)
        for u,v in blue_edges:
            blue_dict[u].append(v)
        distance = 0
        visited_red = [1] + [0]*(n-1)
        visited_blue = [1] + [0]*(n-1)
        while red or blue:
            # print(red, blue)
            blue2 = []
            red2 = []
            for node in red:
                visited_red[node] = 1
                if res[node] == -1:
                    res[node] = distance
                for next_node in blue_dict[node]:
                    if visited_blue[next_node] == 0:
                        blue2.append(next_node)
            for node in blue:
                visited_blue[node] = 1
                if res[node] == -1:
                    res[node] = distance
                for next_node in red_dict[node]:
                    if visited_red[next_node] == 0:
                        red2.append(next_node)
            red, blue = red2, blue2
            distance += 1
        return res

from collections import defaultdict
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        graph = [defaultdict(set), defaultdict(set)]
        for i,j in red_edges:
            graph[0][i].add(j)
        for i,j in blue_edges:
            graph[1][i].add(j)
        res = [float('inf')] * n
        dq = deque([(0,0,0), (1,0,0)])
        while dq:
            color, node, dist = dq.popleft()
            res[node] = min(res[node], dist)
            neighbors = list(graph[color][node])
            for nei in neighbors:
                graph[color][node].remove(nei)
                dq.append((1-color, nei, dist+1))
        return [-1 if x == float('inf') else x for x in res]


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        graph = defaultdict(lambda : defaultdict(set))
        red, blue = 0, 1
        for st, end in red_edges:
            graph[st][red].add(end)
        for st, end in blue_edges:
            graph[st][blue].add(end)
        res = [float('inf')] * n
        q = deque([(0,red), (0,blue)])
        level = -1
        while q:
            level += 1
            size = len(q)
            for i in range(size):
                node, color = q.popleft()
                opp_color = color^1
                res[node] = min(level, res[node])
                neighbors = graph[node][opp_color]
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        return [r if r != float('inf') else -1 for r in res]
        
S = Solution()
# n = 3
# red_edges = [[0,1],[1,2]]
# blue_edges = []
# print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
# n = 3
# red_edges = [[0,1]]
# blue_edges = [[2,1]]
# print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
# n = 3
# red_edges = [[1,0]]
# blue_edges = [[2,1]]
# print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
# n = 3
# red_edges = [[0,1]]
# blue_edges = [[1,2]]
# print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
# n = 3
# red_edges = [[0,1],[0,2]]
# blue_edges = [[1,0]]
# print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
n = 5
red_edges = [[0,1],[1,2],[2,3],[3,4]]
blue_edges =[[1,2],[2,3],[3,1]]
print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
# Output
# [0,1,2,3,-1]
# Expected
# [0,1,2,3,7]
n = 5
red_edges = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
blue_edges = [[1,3],[0,0],[0,3],[4,2],[1,0]]
print(S.shortestAlternatingPaths(n, red_edges, blue_edges))
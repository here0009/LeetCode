"""
Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge. 

Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge. 

Return how many nodes you can reach in at most M moves.

 

Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output: 13
Explanation: 
The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output: 23
 

Note:

0 <= edges.length <= 10000
0 <= edges[i][0] < edges[i][1] < N
There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
The original graph has no parallel edges.
0 <= edges[i][2] <= 10000
0 <= M <= 10^9
1 <= N <= 3000
A reachable node is a node that can be travelled to using at most M moves starting from node 0.
"""
"""
类似于树的遍历, 但是是图,可能更加复杂
尝试采用递归的方法, 从0开始先到一个节点, 再从这个节点开始, 直到末尾或者到M
"""


from typing import List
from collections import defaultdict
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        """
        dfs can not get optimal solution, may not travel to furthest point we can get, try bfs
        we should let the point got the larger weight traverse 1st
        """
        def dfs(i, d):
            res = 0
            if i not in visited:
                visited.add(i)
                res = 1
            if d == 0:
                return res
            for j in dist[i]:
                if dist[i][j] > 0:
                    v = min(d, dist[i][j])
                    dist[i][j] -= v
                    dist[j][i] -= v
                    res += v - (dist[i][j] == 0) + dfs(j, d - v)  # we count the node only when it is not visited, in the next dfs
            # print(i, d, dist, visited)
            return res

        dist = defaultdict(dict)
        for i, j, d in edges:
            dist[i][j] = d + 1
            dist[j][i] = d + 1
        # print(dist)
        visited = set()
        return dfs(0, M)

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        """
        the new added nodes can be reached from both ends of the old nodes.
        to avoid overlap and missing calculation.
        we use a dict visited {node : steps} to record the max step can be taken from the specific node. so the total node can be reached in one edge is min(edge, visited[i] + visited[j])
        we calculate all edges, plus all old nodes that can be reached
        to avoid repeat calculation, we store [(steps, node)] in a priority queue, and visit next node if it have not been visited yet.
        """
        edges_dict = defaultdict(list)
        for p, q, e in edges:
            edges_dict[p].append((q, e))
            edges_dict[q].append((p, e))

        pq = [(-M, 0)]
        visited = {0: M}
        while pq:
            # print(pq)
            steps, node = heapq.heappop(pq)
            for nxt, dist in edges_dict[node]:
                steps2 = -steps - dist - 1
                if steps2 >= 0:
                    if nxt not in visited or visited[nxt] < steps2:
                        visited[nxt] = steps2
                        heapq.heappush(pq, (-steps2, nxt))

        res = len(visited.keys())
        for p, q, e in edges:
            res += min(e, visited.get(p, 0) + visited.get(q, 0))
        return res

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        edges_dict = defaultdict(list)
        for p, q, e in edges:
            edges_dict[p].append((q, e))
            edges_dict[q].append((p, e))

        pq = [(-M, 0)]
        visited = {}
        while pq:
            steps, node = heapq.heappop(pq)
            if node not in visited:
                visited[node] = -steps
                for nxt, dist in edges_dict[node]:  # add nxt in this step and check node in the 1st step, the node poped by heap got the max distance.
                    steps2 = -steps - dist - 1
                    if steps2 >= 0:
                        heapq.heappush(pq, (-steps2, nxt))

        res = len(visited.keys())
        for p, q, e in edges:
            res += min(e, visited.get(p, 0) + visited.get(q, 0))
        return res


s = Solution()
edges = [[0,1,10],[0,2,1],[1,2,2]]
M = 6
N = 3
print(s.reachableNodes(edges, M, N))
edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
M = 10
N = 4
print(s.reachableNodes(edges, M, N))

edges = [[2,4,2],[3,4,5],[2,3,1],[0,2,1],[0,3,5]]
M = 14
N = 5
print(s.reachableNodes(edges, M, N))
# Output
# 20
# Expected
# 18
edges =[[1,2,5],[0,3,3],[1,3,2],[2,3,4],[0,4,1]]
M = 7
N = 5
print(s.reachableNodes(edges, M, N))
# Output
# 14
# Expected
# 13
edges = [[0,3,8],[0,1,4],[2,4,3],[1,2,0],[1,3,9],[0,4,7],[3,4,9],[1,4,4],[0,2,7],[2,3,1]]
M = 8
N = 5
print(s.reachableNodes(edges, M, N))
# Output
# 36
# Expected
# 40
"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""


class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        # times = sorted(times, key=lambda x: x[2])
        time_matrix = [[0] * (N + 1) for _ in range(N + 1)]
        for start, end, time in times:
            time_matrix[start][end] = time

        for start in range(1, N + 1):
            for end in range(1, N + 1):
                for mid in range(1, N + 1):
                    if start == end or start == mid or end == mid:
                        continue
                    if time_matrix[start][mid] != 0 and time_matrix[mid][end] != 0:
                        time = time_matrix[start][mid] + time_matrix[mid][end]
                        if time_matrix[start][end] == 0 or time < time_matrix[start][end]:
                            time_matrix[start][end] = time

        res = 0
        # for row in time_matrix:
        #     print(row)

        for i in range(1, N +1):
            if i == K:
                continue
            if time_matrix[K][i] == 0:
                return -1
            res = max(res, time_matrix[K][i])
        return res

# Dijstra
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        graph = defaultdict(list)
        for s, e, t in times:
            graph[s].append((e, t))
        pq = [(0, K)]
        dist_dict = dict()
        # print(graph)

        while pq:
            dist, node = heapq.heappop(pq)
            if node in dist_dict:
                continue
            dist_dict[node] = dist
            for next_node, dist2 in graph[node]:
                # print(next_node, dist2)
                if next_node not in dist_dict:
                    heapq.heappush(pq, (dist + dist2, next_node))
        # print(dist_dict)
        return max(dist_dict.values()) if len(dist_dict) == N else -1

#https://leetcode.com/problems/network-delay-time/discuss/283711/Python-Bellman-Ford-SPFA-Dijkstra-Floyd-clean-and-easy-to-understand
# Bellman-Ford
class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        dist = [float('inf')] * (N + 1)
        dist[0] = 0
        dist[K] = 0
        for _ in range(N - 1):
            for start, end, time in times:
                if dist[start] + time < dist[end]:
                    dist[end] = dist[start] + time
        # print(dist)
        res = max(dist)
        return res if res != float('inf') else -1


#Floyd-Warshall
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1

S = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(S.networkDelayTime(times, N, K))


times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
N = 5
K = 5
print(S.networkDelayTime(times, N, K))

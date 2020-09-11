"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:



Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:



Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""




class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        for s, e, d in edges:
            matrix[s][e] = d
            matrix[e][s] = d
        for i in range(n):
            matrix[i][i] = 0
        for k in range(n): # k at the outmost loop, this is important, we need to use k to short all the distance between nodes that pass k
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        res, count = 0, n
        for i in range(n):
            tmp = sum(matrix[i][j] <= distanceThreshold for j in range(n))
            if tmp <= count:
                count = tmp
                res = i
        return res


import heapq
from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        graph = defaultdict(list)
        for s, e, d in edges:
            matrix[s][e] = d
            matrix[e][s] = d
            graph[s].append(e)
            graph[e].append(s)
        # print(graph)
        # print(matrix)

        def dijkstra(source):
            dist = [float('inf')]*n
            dist[source] = 0
            pq = [(0, source)]
            heapq.heapify(pq)
            while pq:
                # print(pq)
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for next_node in graph[node]:
                    tmp = d + matrix[node][next_node]
                    if tmp < dist[next_node]:
                        dist[next_node] = tmp
                        heapq.heappush(pq, (tmp, next_node))
            # print(source, dist)
            return sum(d <= distanceThreshold for d in dist) - 1

        res, counts = 0, n
        for i in range(n):
            tmp = dijkstra(i)
            # print(tmp, i)
            if tmp <= counts:
                counts = tmp
                res = i
        return res

S = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(S.findTheCity(n, edges, distanceThreshold))

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
print(S.findTheCity(n, edges, distanceThreshold))
"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
class Solution_1:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        def dfs(node, cost, stops):
            # print('test',node, cost, stops)
            if node == dst:
                self.res = min(self.res, cost)
                return
            if stops > K or cost >= self.res:
                return
            for i in range(n):
                if not visited[i] and matrix[node][i] > 0:
                    visited[i] = 1
                    dfs(i, cost+matrix[node][i], stops+1)
                    visited[i] = 0


        matrix = [[0]*n for _ in range(n)]
        visited = [0]*n
        self.res = float('inf')
        for s,d,c in flights:
            matrix[s][d] = c

        visited[src] = 1
        dfs(src, 0, 0)
        if self.res != float('inf'):
            return  self.res
        else:
            return -1
        
import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        matrix = defaultdict(dict)
        for s,d,c in flights:
            matrix[s][d] = c
        q = [(0,0,src)]
        while q:
            cost, k, node = heapq.heappop(q)
            if node == dst:
                return cost
            if k < K+1:
                for next_node in matrix[node]:
                    heapq.heappush(q,(cost+matrix[node][next_node], k+1, next_node))
        return -1
            

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
S = Solution()
print(S.findCheapestPrice(n, edges, src, dst, k))


n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(S.findCheapestPrice(n, edges, src, dst, k))

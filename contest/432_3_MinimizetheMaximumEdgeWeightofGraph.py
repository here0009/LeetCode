from typing import List
import heapq
from collections import defaultdict
from math import inf
from bisect import bisect_left

class Solution_1:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        edges_dict = defaultdict(list)
        for source, dest, weight in edges:
            edges_dict[dest].append((weight, source))
        # print(edges_dict)
        if len(edges_dict[0]) == 0:
            return -1
        dist = [inf] * n
        dist[0] = 0
        pq = [(0,0)]
        while pq:
            # print(pq)
            # print(dist)
            # print('='*10)
            weight, source = pq.pop()
            # print(f'weight:{weight},source:{source}')
            if weight > dist[source]:
                continue
            for w2, dest in edges_dict[source]:
                # if w2 < dist[dest]: # wrong because of test case 5
                #     dist[dest] = w2
                #     heapq.heappush(pq, (w2, dest))
                d2 = max(weight, w2)
                if d2 < dist[dest]:
                    dist[dest] = d2
                    heapq.heappush(pq, (d2, dest))
        
        res = max(dist)
        # print(dist)
        return -1 if res == inf else res

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        
        def check(weight:int):
            
            def dfs(node:int):
                visited[node] = weight
                cnt = 1
                for w, dest in edges_dict[node]:
                    if w <= weight and visited[dest] != weight:
                        cnt += dfs(dest)
                return cnt
            return dfs(0) == n

        edges_dict = defaultdict(list)
        for source, dest, weight in edges:
            edges_dict[dest].append((weight, source))
        
        # print(edges_dict)
        # weight_lst = sorted(set([w for _, _, w in edges]))
        max_w = max(e[2] for e in edges)
        visited = [0]*n      
        ans = bisect_left(range(max_w + 1), True, key=check)
        return -1 if ans > max_w else ans

        
            
        
        

s = Solution()
n = 5
edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]]
threshold = 2
print(s.minMaxWeight(n, edges, threshold))
n = 5
edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]]
threshold = 1
print(s.minMaxWeight(n, edges, threshold))
n = 5
edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]]
threshold = 1
print(s.minMaxWeight(n, edges, threshold))
n = 5
edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]]
threshold = 1
print(s.minMaxWeight(n, edges, threshold))
# test case 5
n = 4
edges = [[3,2,24],[3,0,92],[2,1,8],[3,2,87],[1,3,20]]
threshold = 3
print(s.minMaxWeight(n, edges, threshold))
n = 3
edges = [[0,1,26],[1,0,35],[1,2,94]]
threshold = 2
print(s.minMaxWeight(n, edges, threshold))
"""
We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai with city bi. Each city has a name consisting of exactly 3 upper-case English letters given in the string array names. Starting at any city x, you can reach any city y where y != x (i.e. the cities and the roads are forming an undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph of the same length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance, The path should be of the same length of targetPath and should be valid (i.e. there should be a direct road between ans[i] and ans[i + 1]). If there are multiple answers return any one of them.

The edit distance is defined as follows:



Follow-up: If each node can be visited only once in the path, What should you change in your solution?

 

Example 1:


Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
Output: [0,2,4,2]
Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
[0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
[0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
[0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
Example 2:


Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
Output: [0,1,0,1,0,1,0,1]
Explanation: Any path in this graph has edit distance = 8 with targetPath.
Example 3:



Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
Output: [3,4,5,4,3,2,1]
Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
 

Constraints:

2 <= n <= 100
m == roads.length
n - 1 <= m <= (n * (n - 1) / 2)
0 <= ai, bi <= n - 1
ai != bi 
The graph is guaranteed to be connected and each pair of nodes may have at most one direct road.
names.length == n
names[i].length == 3
names[i] consists of upper-case English letters.
There can be two cities with the same name.
1 <= targetPath.length <= 100
targetPath[i].length == 3
targetPath[i] consists of upper-case English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-most-similar-path-in-a-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import defaultdict
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        def dfs(i, t, cost, path):
            if t == len_t: # because the edges are bidirection, if we got a way to j, we must got a way from j. so we can check at t == len_t
                if cost < self.min_cost:
                    self.res = path
                    self.min_cost = cost
                return
            cost += targetPath[t] != names[i]
            path = path + [i]
            if cost >= self.min_cost:
                return
            for j in edges[i]: 
                dfs(j, t+1, cost, path)


        # name_index = dict(zip(names, list(range(n))))
        edges = defaultdict(list)
        for i, j in roads:
            edges[i].append(j)
            edges[j].append(i)

        # targetPath_id = [name_index[name] for name in targetPath]
        len_t = len(targetPath)
        self.min_cost = float('inf')
        self.res = None
        for i in range(n):
            dfs(i, 0, 0, [])
        return self.res


from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        @lru_cache(None)
        def dfs(i, t):
            if t == len_t: # because the edges are bidirection, if we got a way to j, we must got a way from j. so we can check at t == len_t
                return 0, []
            # path = path + tuple(i)
            res = float('inf')
            path = []
            for j in edges[i]:
                tmp, tmp_path = dfs(j, t+1)
                if tmp < res:
                    res = tmp
                    path = tmp_path
            return res + (targetPath[t] != names[i]), [i] + path


        # name_index = dict(zip(names, list(range(n))))
        edges = defaultdict(list)
        for i, j in roads:
            edges[i].append(j)
            edges[j].append(i)

        # targetPath_id = [name_index[name] for name in targetPath]
        len_t = len(targetPath)
        res = float('inf')
        path = []
        for i in range(n):
            tmp, tmp_path = dfs(i, 0)
            if tmp < res:
                res = tmp
                path = tmp_path
        return path


# 作者：yuan-zhi-b
# 链接：https://leetcode-cn.com/problems/the-most-similar-path-in-a-graph/solution/python3-dp-10xing-by-yuan-zhi-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        d=defaultdict(list)
        for a,b in roads:
            d[a].append(b)
            d[b].append(a)
            
        @functools.lru_cache(None)
        def dp(roadIdx,targetIdx):
            if targetIdx>=len(targetPath): return 0,[]
            mincost,minpath=min([dp(nxt,targetIdx+1) for nxt in d[roadIdx]],key=lambda x:x[0])
            return mincost+(names[roadIdx]!=targetPath[targetIdx]),[roadIdx]+minpath
        return min([dp(i,0) for i in range(n)],key=lambda x:x[0])[1]



S = Solution()
n = 5
roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
names = ["ATL","PEK","LAX","DXB","HND"]
targetPath = ["ATL","DXB","HND","LAX"]
print(S.mostSimilar(n, roads, names, targetPath))
n = 4
roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]]
names = ["ATL","PEK","LAX","DXB"]
targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
print(S.mostSimilar(n, roads, names, targetPath))
n = 6
roads = [[0,1],[1,2],[2,3],[3,4],[4,5]]
names = ["ATL","PEK","LAX","ATL","DXB","HND"]
targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
print(S.mostSimilar(n, roads, names, targetPath))


n = 5
roads = [[1,2],[2,4],[4,1],[4,0],[3,0]]
names = ["CBB","ERF","CBB","RSC","CBB"]
targetPath = ["CBB","RSC","RSC","CBB","ERF","CBB","RSC","RSC","CBB","CBB","CBB","ERF","ERF","CBB","CBB","ERF","CBB","CBB","RSC","CBB","CBB","CBB","RSC","ERF","ERF","CBB","CBB","CBB","RSC","ERF","CBB","RSC","ERF","RSC","CBB","ERF","RSC","RSC","CBB","RSC","CBB","CBB","RSC","CBB","ERF","CBB","RSC"]
print(S.mostSimilar(n, roads, names, targetPath))

"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-color-value-in-a-directed-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import defaultdict, Counter, deque
from functools import lru_cache
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        # 邻接表
        g = defaultdict(list)
        # 节点的入度统计，用于找出拓扑排序中最开始的节点
        indeg = [0] * n

        for x, y in edges:
            indeg[y] += 1
            g[x].append(y)
        
        # 记录拓扑排序过程中遇到的节点个数
        # 如果最终 found 的值不为 n，说明图中存在环
        found = 0
        f = [[0] * 26 for _ in range(n)]
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
    
        while q:
            found += 1
            u = q.popleft()
            # 将节点 u 对应的颜色增加 1
            f[u][ord(colors[u]) - ord("a")] += 1
            # 枚举 u 的后继节点 v
            for v in g[u]:
                indeg[v] -= 1
                # 将 f(v,c) 更新为其与 f(u,c) 的较大值
                for c in range(26):
                    f[v][c] = max(f[v][c], f[u][c])
                if indeg[v] == 0:
                    q.append(v)
        
        if found != n:
            return -1
        
        ans = 0
        for i in range(n):
            ans = max(ans, max(f[i]))
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/largest-color-value-in-a-directed-graph/solution/you-xiang-tu-zhong-zui-da-yan-se-zhi-by-dmtaa/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        TLE
        there could be cycles in edges
        """

        def dfs(node):
            # print(node)
            # print(node, visited)
            if self.isCycle:
                return
            if visited[node] == 1:
                self.isCycle = True
                return
            visited[node] = 1
            counts = Counter(''.join(colors[i] for i in range(length) if visited[i]))
            if not edges_dict[node]:
                self.res = max(self.res, max(counts.values()))
            for nxt_node in edges_dict[node]:
                dfs(nxt_node)
            visited[node] = 0


        length= len(colors)
        edges_dict = defaultdict(list)
        for _p, _q in edges:
            edges_dict[_p].append(_q)

        start = set(list(range(length))) - set([_edge[1] for _edge in edges])
        # print(edges_dict)
        # print(start)
        visited = [0] * length
        if not start:
            return -1
        self.res = 0
        self.isCycle = False
        for node in start:
            dfs(node)
        return self.res if not self.isCycle else -1


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        def get_start():
            start = [i for i in range(length) if indegree[i] == 0]
            nodes = deque(start[:])
            counts = 0
            while nodes:
                p = nodes.popleft()
                counts += 1
                for q in edges_dict[p]:
                    indegree[q] -= 1
                    if indegree[q] == 0:
                        nodes.append(q)
            if counts == length:
                return start
            else:
                return None

        @lru_cache(None)
        def dfs(node):
            res = [0] * 26
            for nxt_node in edges_dict[node]:
                nxt_res = dfs(nxt_node)
                for i in range(26):
                    res[i] = max(nxt_res[i], res[i])
            res[ord(colors[node]) - ord('a')] += 1
            return res


        length = len(colors)
        indegree = [0] * length
        edges_dict = defaultdict(list)
        for _p, _q in edges:
            edges_dict[_p].append(_q)
            indegree[_q] += 1

        start = get_start()
        if not start:
            return -1
        res = 0
        for node in start:
            node_counts = dfs(node)
            res = max(res, max(node_counts))
        return res


S = Solution()
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
print(S.largestPathValue(colors, edges))
colors = "a"
edges = [[0,0]]
print(S.largestPathValue(colors, edges))
colors = "qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq"
edges =[[0,1],[1,2],[2,3],[3,4],[3,5],[4,5],[3,6],[5,6],[6,7],[5,7],[3,7],[6,8],[5,8],[4,8],[8,9],[9,10],[10,11],[9,11],[9,12],[11,12],[6,12],[11,13],[9,13],[13,14],[12,14],[10,14],[11,14],[13,15],[14,15],[12,16],[9,16],[7,16],[15,17],[13,17],[17,18],[11,18],[17,19],[18,19],[13,19],[17,20],[18,20],[19,21],[17,21],[12,22],[21,22],[16,22],[22,23],[21,23],[16,24],[22,24],[15,25],[24,25],[20,25],[12,25],[23,26],[26,27],[13,27],[27,28],[21,28],[26,28],[28,29],[15,30],[27,30],[24,30],[21,30],[27,31],[30,31],[25,32],[29,32],[17,33],[31,33],[32,33],[25,34],[33,35],[31,35],[34,35],[30,36],[35,37],[36,37],[26,38],[36,38],[34,38],[37,38],[38,39],[22,39],[39,40],[40,41],[38,41],[20,41],[41,42],[37,42],[40,43],[42,43],[43,44],[41,44],[32,44],[38,44],[39,44],[43,45],[44,45],[44,46],[45,46],[45,47],[42,47],[43,48],[45,49],[45,50],[48,51],[30,51],[46,52],[48,52],[38,52],[51,52],[47,53],[45,53],[53,54],[48,54],[30,54],[50,55],[30,55],[36,55],[55,56],[39,56],[54,56],[50,57],[56,58],[32,58],[57,59],[49,59],[38,60],[60,61],[35,61],[54,61],[53,61],[54,62],[58,62],[62,63],[40,63],[58,63],[49,64],[63,64],[47,64],[39,64],[45,64],[62,65],[64,65],[54,65],[52,66],[61,66],[60,66],[55,67],[65,67],[45,68],[56,68],[36,68],[67,69],[66,69],[27,70],[60,70],[67,70],[48,71],[70,71],[53,71],[62,72],[72,73],[73,74]]
print(S.largestPathValue(colors, edges))
colors = "hhqhuqhqff"
edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
print(S.largestPathValue(colors, edges))
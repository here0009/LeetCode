"""
小明的电动车电量充满时可行驶距离为 cnt，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间。小明想选择电动车作为代步工具。地图上共有 N 个景点，景点编号为 0 ~ N-1。他将地图信息以 [城市 A 编号,城市 B 编号,两城市间距离] 格式整理在在二维数组 paths，表示城市 A、B 间存在双向通路。初始状态，电动车电量为 0。每个城市都设有充电桩，charge[i] 表示第 i 个城市每充 1 单位电量需要花费的单位时间。请返回小明最少需要花费多少单位时间从起点城市 start 抵达终点城市 end。

示例 1：

输入：paths = [[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]], cnt = 6, start = 1, end = 0, charge = [2,10,4,1]

输出：43

解释：最佳路线为：1->3->0。
在城市 1 仅充 3 单位电至城市 3，然后在城市 3 充 5 单位电，行驶至城市 5。
充电用时共 3*10 + 5*1= 35
行驶用时 3 + 5 = 8，此时总用时最短 43。
image.png

示例 2：

输入：paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], cnt = 8, start = 0, end = 2, charge = [4,1,1,3,2]

输出：38

解释：最佳路线为：0->4->3->2。
城市 0 充电 2 单位，行驶至城市 4 充电 8 单位，行驶至城市 3 充电 1 单位，最终行驶至城市 2。
充电用时 4*2+2*8+3*1 = 27
行驶用时 2+5+4 = 11，总用时最短 38。

提示：

1 <= paths.length <= 200
paths[i].length == 3
2 <= charge.length == n <= 100
0 <= path[i][0],path[i][1],start,end < n
1 <= cnt <= 100
1 <= path[i][2] <= cnt
1 <= charge[i] <= 100
题目保证所有城市相互可以到达
"""


from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:

        # @lru_cache(None)
        def dp(idx, battery):
            if idx == end:
                return 0
            visited.add(idx)
            res = float('inf')
            for e, d in edges[idx]:
                if e not in visited:
                    for b in range(max(battery, d), cnt + 1):
                        res = min(res, d + charge[idx] * (b - battery) + dp(e, b - d))
            return res


        edges = defaultdict(list)
        for s, e, d in paths:
            edges[s].append((e, d))
            edges[e].append((s, d))
        visited = set()
        return dp(start, 0)


from typing import List
from collections import defaultdict
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:

        n = len(charge)
        cost = [[float('inf')] * (cnt + 1) for _ in range(n)]
        for i in range(cnt + 1):
            cost[start][i] = i * charge[start]
        edges = defaultdict(list)
        for s, e, d in paths:
            edges[s].append((e, d))
            edges[e].append((s, d))
        for b in range(cnt + 1):
            for s in range(n):
                for e, d in edges[s]:
                    if b >= d:
                        cost[e][b] = min(cost[e][b], d + d * charge[s] + cost[s][b - d])

        for row in cost:
            print(row)
        return min(cost[end])

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:

        edges = defaultdict(list)
        for s, e, d in paths:
            edges[s].append((e, d))
            edges[e].append((s, d))
        pq = [(0, start, 0)]
        memo = dict()
        memo[(start, 0)] = 0
        while pq:
            # print(pq)
            cost, idx, battery = heapq.heappop(pq)
            if idx == end:
                return cost
            for e, d in edges[idx]:
                for b in range(max(battery, d), cnt + 1):
                    tmp = cost + d + charge[idx] * (b - battery)
                    if (e, b - d) not in memo or memo[(e, b - d)] > tmp:
                        memo[(e, b - d)] = tmp
                        heapq.heappush(pq, (tmp, e, b - d))
        return None


from typing import List
from collections import defaultdict
import heapq
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:

        edges = defaultdict(list)
        for s, e, d in paths:
            edges[s].append((d, e))
            edges[e].append((d, s))

        pq = [(0, start, 0)]
        memo = dict()
        memo[(start, 0)] = 0
        while pq:
            cost, idx, battery = heapq.heappop(pq)
            if idx == end:
                return cost
            if battery < cnt:
                heapq.heappush(pq, (cost + charge[idx], idx, battery + 1))
            for d, e in edges[idx]:
                b = max(battery, d)
                tmp = cost + d + charge[idx] * (b - battery)
                if (e, b - d) not in memo or memo[(e, b - d)] > tmp:
                    memo[(e, b - d)] = tmp
                    heapq.heappush(pq, (tmp, e, b - d))
        return None

S = Solution()

paths = [[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]]
cnt = 6
start = 1
end = 0
charge = [2,10,4,1]
print(S.electricCarPlan(paths, cnt, start, end, charge))
paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]]
cnt = 8
start = 0
end = 2
charge = [4,1,1,3,2]
print(S.electricCarPlan(paths, cnt, start, end, charge))
paths = [[3,7,32],[0,6,46],[1,0,47],[0,6,8],[0,3,30],[1,5,34],[1,2,9],[1,4,29],[0,1,6]]
cnt =52
start =4
end = 5
charge =[90,57,24,52,75,61,39,20]
print(S.electricCarPlan(paths, cnt, start, end, charge))

"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""


from typing import List
from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        def dp(b):
            """
            min bus need to take to get T
            """
            # print(b)
            if b in stations[T]:
                return 1
            visited[b] = 1
            res = float('inf')
            for next_b in edeges[b]:
                if visited[next_b] == 0:
                    res = min(res, 1 + dp(next_b))
            return res

        if S == T:
            return 0
        stations = defaultdict(set)
        for bus, route in enumerate(routes):
            for s in set(route):
                stations[s].add(bus)
        edeges = defaultdict(set)  # if two buses both stop at a station, make an edge between them
        for s, buses in stations.items():
            lst = list(buses)
            for i in range(len(lst) - 1):
                for j in range(i + 1, len(lst)):
                    edeges[lst[i]].add(lst[j])
                    edeges[lst[j]].add(lst[i])

        res = float('inf')
        visited = [0] * len(routes)
        # print(stations)
        # print(edeges)
        for b in stations[S]:
            # visited[b] = 1
            res = min(res, dp(b))
        return res if res != float('inf') else -1

Slt = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
print(Slt.numBusesToDestination(routes, S, T))

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
S = 15
T = 12
print(Slt.numBusesToDestination(routes, S, T))

routes = [[1,7],[3,5]]
S = 5
T = 5
print(Slt.numBusesToDestination(routes, S, T))
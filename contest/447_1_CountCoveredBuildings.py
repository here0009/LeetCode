from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_min = dict()
        x_max = dict()
        y_min = dict()
        y_max = dict()
        res = 0
        for x, y in buildings:
            x_min[y] = min(x, x_min.get(y, x))
            x_max[y] = max(x, x_max.get(y, x))
            y_min[x] = min(y, y_min.get(x, y))
            y_max[x] = max(y, y_max.get(x, y))
        for x, y in buildings:
            if x < x_max[y] and x > x_min[y] and y < y_max[x] and y > y_min[x]:
                res += 1
        return res

sol = Solution()
n = 3
buildings = [[2,3],[3,3],[1,3]]
print(sol.countCoveredBuildings(n, buildings))
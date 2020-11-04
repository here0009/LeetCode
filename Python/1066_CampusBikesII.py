"""
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 

Example 1:


Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
Example 2:


Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
Example 3:

Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
Output: 4995
 

Constraints:

N == workers.length
M == bikes.length
1 <= N <= M <= 10
workers[i].length == 2
bikes[i].length == 2
0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All the workers and the bikes locations are unique.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/campus-bikes-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def assignBikes(self, workers, bikes) -> int:
        """
        TLE, try bit mask
        """
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        def dfs(i, res):
            if i == len_w:
                self.res = min(self.res, res)
                return
            if res > self.res:
                return
            for j in range(len_b):
                if visited[j] == 0:
                    visited[j] = 1
                    dfs(i+1, res + distances[i][j])
                    visited[j] = 0

        len_w = len(workers)
        len_b = len(bikes)
        distances = [[0]*len_b for _ in range(len_w)]
        visited = [0]*len_b
        for iw, w in enumerate(workers):
            for ib, b in enumerate(bikes):
                distances[iw][ib] = dist(w, b)
        self.res = float('inf')
        dfs(0, 0)
        return self.res


from functools import lru_cache
class Solution:
    def assignBikes(self, workers, bikes) -> int:
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        @lru_cache(None)
        def dfs(i, bitmask):
            if i == len_w:
                return 0
            res = float('inf')
            for j in range(len_b):
                if bitmask >> j & 1 == 0:
                    res = min(res, distances[i][j] + dfs(i+1, bitmask ^ (1 << j)))
            return res

        len_w = len(workers)
        len_b = len(bikes)
        distances = [[0]*len_b for _ in range(len_w)]
        for iw, w in enumerate(workers):
            for ib, b in enumerate(bikes):
                distances[iw][ib] = dist(w, b)
        return dfs(0, 0)


from functools import lru_cache
class Solution:
    def assignBikes(self, workers, bikes) -> int:
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        @lru_cache(None)
        def dfs(i, bitmask):
            if i == len_w:
                return 0
            res = min((distances[i][j] + dfs(i+1, bitmask ^ (1 << j)) for j in range(len_b) if (bitmask >> j) & 1 == 0))
            return res

        len_w = len(workers)
        len_b = len(bikes)
        distances = [[0]*len_b for _ in range(len_w)]
        for iw, w in enumerate(workers):
            for ib, b in enumerate(bikes):
                distances[iw][ib] = dist(w, b)
        return dfs(0, 0)

S = Solution()
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
print(S.assignBikes(workers, bikes))
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
print(S.assignBikes(workers, bikes))
workers = [[0,0],[1,0],[2,0],[3,0],[4,0]]
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
print(S.assignBikes(workers, bikes))
workers = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999],[9,999]]
print(S.assignBikes(workers, bikes))
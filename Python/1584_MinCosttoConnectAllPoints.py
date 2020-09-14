"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:



Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""


class Solution:
    def minCostConnectPoints(self, points) -> int:
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return True
            else:
                root[ri] = rj
                return False


        length = len(points)
        if length == 1:
            return 0
        dist = [[0]*length for _ in range(length)]
        dist_list = []
        root = list(range(length))
        for i in range(length-1):
            for j in range(i+1, length):
                dist[i][j] = dist[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist_list.append((dist[i][j], i, j))
        dist_list = sorted(dist_list)
        res = 0
        for d, i, j in dist_list:
            if not union(i,j):
                res += d
        return res


class Solution:
    def minCostConnectPoints(self, points) -> int:
        length = len(points)
        if length == 1:
            return 0
        res = 0
        curr = 0 # start point
        visited = set()
        dis = [float('inf')]*length
        for i in range(length-1): #number of edges
            x0, y0 = points[curr]
            visited.add(curr)
            for j, (x1, y1) in enumerate(points):
                if j not in visited:
                    dis[j] = min(dis[j], abs(x1-x0)+abs(y1-y0))
            delta, curr = min((d,j) for j,d in enumerate(dis))
            dis[curr] = float('inf')
            res += delta
        return res

S = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(S.minCostConnectPoints(points))
points = [[3,12],[-2,5],[-4,1]]
print(S.minCostConnectPoints(points))
points = [[0,0],[1,1],[1,0],[-1,1]]
print(S.minCostConnectPoints(points))
points = [[-1000000,-1000000],[1000000,1000000]]
print(S.minCostConnectPoints(points))
points = [[0,0]]
print(S.minCostConnectPoints(points))
points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
print(S.minCostConnectPoints(points))
# Output:
# 29
# Expected:
# 53
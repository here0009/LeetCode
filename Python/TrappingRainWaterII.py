"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
"""

class Solution:
    """
    wrong anwser
    """
    def trapRainWater(self, heightMap) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        leftBoundary = [row[:] for row in heightMap]
        rightBoundary = [row[:] for row in heightMap]
        upBoundary = [row[:] for row in heightMap]
        downBoundary = [row[:] for row in heightMap]
        minMap = [row[:] for row in heightMap]
        for i in range(m):
            leftMax = float('-inf')
            for j in range(n):
                leftMax = max(leftMax, leftBoundary[i][j])
                leftBoundary[i][j] = leftMax
            rightMax = float('-inf')
            for j in range(n-1, -1, -1):
                rightMax = max(rightMax, rightBoundary[i][j])
                rightBoundary[i][j] = rightMax
        
        for row in heightMap:
            print(row)
        print('++++++++++++')

        # for row in leftBoundary:
        #     print(row)
        # print('++++++++++++')
        # for row in rightBoundary:
        #     print(row)
        # print('++++++++++++')
        for j in range(n):
            upMax = float('-inf')
            for i in range(m):
                upMax = max(upMax, upBoundary[i][j])
                upBoundary[i][j] = upMax
            downMax = float('-inf')
            for i in range(m-1, -1, -1):
                downMax = max(downMax, downBoundary[i][j])
                downBoundary[i][j] = downMax

        # for row in upBoundary:
        #     print(row)
        # print('++++++++++++')
        # for rown in downBoundary:
        #     print(row)
        # print('++++++++++++')
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                minMap[i][j] = min(leftBoundary[i][j], rightBoundary[i][j], upBoundary[i][j], downBoundary[i][j])

        for row in minMap:
            print(row)
        print('++++++++++++')
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                res += min(minMap[i][j], minMap[i-1][j], minMap[i+1][j], minMap[i][j-1], minMap[i][j+1]) - heightMap[i][j]

        return res

# https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
# https://leetcode.com/problems/trapping-rain-water-ii/discuss/89495/How-to-get-the-solution-to-2-D-%22Trapping-Rain-Water%22-problem-from-1-D-case
import heapq
class Solution:
    def trapRainWater(self, heightMap) -> int:
        def inRange(i,j):
            return 0 <= i < m and 0 <= j < n

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[0]*n for _ in range(m)]
        hp = []
        # for row in heightMap:
        #     print(row)
        for i in range(m):
            for j in range(n):
                if i in {0, m-1} or j in {0, n-1}:
                    heapq.heappush(hp, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        # print(hp)
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while hp:
            # print(hp, res)
            height, i, j = heapq.heappop(hp)
            for di, dj in directions:
                ti, tj = i + di, j + dj
                if inRange(ti, tj) and not visited[ti][tj]:
                    res += max(0, height - heightMap[ti][tj])
                    heapq.heappush(hp, (max(height, heightMap[ti][tj]), ti, tj))
                    visited[ti][tj] = 1
        return res



        

S = Solution()
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(S.trapRainWater(heightMap))

heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(S.trapRainWater(heightMap))
# Output
# 15
# Expected
# 14
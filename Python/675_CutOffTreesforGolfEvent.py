"""
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

 

Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:


Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.
 

Constraints:

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
"""


from typing import List
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        record the height of forest, and walk through min to max?
        use bfs to calculate the distance
        """
        def neighbors(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] > 0:
                    yield ni, nj

        def bfs(start, target):
            i, j = start
            lst = [(i, j)]
            steps = 0
            if start == target:
                return 0
            visited = set(lst)
            while lst:
                lst2 = []
                steps += 1
                for i, j in lst:
                    for ni, nj in neighbors(i, j):
                        if (ni, nj) not in visited:
                            if (ni, nj) == target:
                                return steps
                            visited.add((ni, nj))
                            lst2.append((ni, nj))
                lst = lst2
            return None

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])
        trees.sort()
        res = 0
        pre = (0, 0)
        # print(trees)
        for h, i, j in trees:
            tmp = bfs(pre, (i, j))
            # print(pre, (i, j), tmp)
            if tmp is None:
                return -1
            res += tmp
            pre = (i, j)
        return res


from typing import List
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        there are repeat calculation in bfs, may be we can try to memorize the calculation results and make it faster
        got TLE, we only use start for once
        """
        def neighbors(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] > 0:
                    yield ni, nj

        def bfs(start, target):
            if (start, target) in memo:
                return memo[(start, target)]
            i, j = start
            lst = [(i, j)]
            steps = 0
            if start == target:
                return 0
            visited = set(lst)
            while lst:
                lst2 = []
                steps += 1
                for i, j in lst:
                    for ni, nj in neighbors(i, j):
                        if (ni, nj) not in visited:
                            memo[start, (ni, nj)] = steps
                            memo[(ni, nj), start] = steps
                            if (ni, nj) == target:
                                return steps
                            visited.add((ni, nj))
                            lst2.append((ni, nj))
                lst = lst2
            return None

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])
        trees.sort()
        res = 0
        pre = (0, 0)
        memo = dict()
        # print(trees)
        for h, i, j in trees:
            tmp = bfs(pre, (i, j))
            # print(pre, (i, j), tmp)
            if tmp is None:
                return -1
            res += tmp
            pre = (i, j)
        return res


from typing import List
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        use matrix instead of set to store the visited information, may make if faster
        """
        def neighbors(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] > 0:
                    yield ni, nj

        def bfs(start, target):
            i, j = start
            lst = [(i, j)]
            steps = 0
            if start == target:
                return 0
            visited = [[0] * n for _ in range(m)]
            visited[i][j] = 1
            while lst:
                lst2 = []
                steps += 1
                for i, j in lst:
                    for ni, nj in neighbors(i, j):
                        if visited[ni][nj] == 0:
                            if (ni, nj) == target:
                                return steps
                            visited[ni][nj] = 1
                            lst2.append((ni, nj))
                lst = lst2
            return None

        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])
        trees.sort()
        res = 0
        pre = (0, 0)
        for h, i, j in trees:
            tmp = bfs(pre, (i, j))
            if tmp is None:
                return -1
            res += tmp
            pre = (i, j)
        return res

# https://leetcode.com/problems/cut-off-trees-for-golf-event/solution/
from typing import List
import heapq
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        use astar to calculate the distance, it seems great and faster
        """
        def neighbors(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] > 0:
                    yield ni, nj

        def astar(start, target):
            si, sj = start
            pq = [(0, 0, si, sj)]  # heuristic + steps, steps, i, j
            if start == target:
                return 0
            cost = {(start): 0}
            while pq:
                # print(pq)
                f, g, i, j = heapq.heappop(pq)

                for ni, nj in neighbors(i, j):
                    f2 = g + 1 + abs(i - ni) + abs(j - nj)
                    if (ni, nj) == target:
                        return g + 1
                    if f2 < cost.get((ni, nj), float('inf')):
                        cost[(ni, nj)] = f2
                        heapq.heappush(pq, (f2, g + 1, ni, nj))
            return None

        m, n = len(forest), len(forest[0])

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])

        trees.sort()
        res = 0
        pre = (0, 0)
        for h, i, j in trees:
            tmp = astar(pre, (i, j))
            if tmp is None:
                return -1
            res += tmp
            pre = (i, j)
        return res


S = Solution()
forest = [[1,2,3],[0,0,4],[7,6,5]]
print(S.cutOffTree(forest))
forest = [[1,2,3],[0,0,0],[7,6,5]]
print(S.cutOffTree(forest))
forest = [[2,3,4],[0,0,5],[8,7,6]]
print(S.cutOffTree(forest))
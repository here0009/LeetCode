"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
class Solution:
    def removeStones(self, stones) -> int:
        """
        不是一笔画，有相同行或列的都可以移去
        backtrack
        """
        def backtrack(n,counts):
            print(n,counts)
            x,y = stones[n]
            for i in range(len_s):
                if visited[i] == 0 and (x == stones[i][0] or y == stones[i][1]):
                    visited[i] = 1
                    counts += 1
                    self.res = max(self.res, counts)
                    backtrack(i,counts)
                    counts -= 1
                    visited[i] = 0


        len_s = len(stones)
        visited = [0]*len_s
        self.res = 0
        counts = 0
        for i in range(len_s):
            visited[i] = 1
            backtrack(i,counts)
            visited[i] = 0
        return self.res

from collections import Counter
import heapq
class Solution:
    def removeStones(self, stones) -> int:
        """
        wrong answer
        """
        def printStones(stones_set):
            matrix = [[0] * N for _ in range(N)]
            for i, j in stones_set:
                matrix[i][j] = 1
            for row in matrix:
                print(row)

        r_counts, c_counts, vals = Counter(), Counter(), Counter()
        stones_set = set(tuple(lst) for lst in stones)
        pq = []
        N = 0
        for i, j in stones:
            r_counts[i] += 1
            c_counts[j] += 1
            N = max([N, i + 1, j + 1])
        for i, j in stones:
            vals[(i, j)] = r_counts[i] + c_counts[j] - 1
            heapq.heappush(pq, (vals[(i,j)], i, j))
        res = 0
        # print('pq, res', pq, res)
        # print('stones_set', stones_set)
        # print('vals', vals)
        while pq and stones_set:
            printStones(stones_set)
            print('======================')
            v, i, j = heapq.heappop(pq)
            if (i, j) not in stones_set:
                continue
            res += (v > 1)

            stones_set.remove((i, j))
            for ni, nj in stones_set:
                if ni == i or nj == j:
                    vals[(ni, nj)] -= 1
                    heapq.heappush(pq, (vals[(ni, nj)], ni, nj))
            # print('pq, res', pq, res)
            # print('stones_set', stones_set)
            # print('vals', vals)
        return res


from collections import defaultdict
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        the max step we can take to reomove stones is the len(stones) - n(connected_component)
        if two component can be connected, we add one to res.
        if they are already connected, do nothing
        """

        def find(i):
            if i not in root:
                root[i] = i
            else:
                if root[i] != i:
                    ri = find(root[i])
                    root[i] = ri
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[rj] = ri
            return True

        r_keys = defaultdict(list)
        c_keys = defaultdict(list)
        root = dict()
        res = 0
        for i, j in stones:
            r_keys[i].append(j)
            c_keys[j].append(i)

        for i, lst in r_keys.items():
            node = (i, lst[0])
            for j in lst[1:]:
                if union(node, (i, j)):
                    res += 1
        for j, lst in c_keys.items():
            node = (lst[0], j)
            for i in lst[1:]:
                if union(node, (i, j)):
                    res += 1
        # print(root)
        return res



s = Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(s.removeStones(stones))

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(s.removeStones(stones))

stones = [[0,0]]
print(s.removeStones(stones))

stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(s.removeStones(stones))
# Output
# 5
# Expected
# 4
stones = [[5,9],[9,0],[0,0],[7,0],[4,3],[8,5],[5,8],[1,1],[0,6],[7,5],[1,6],[1,9],[9,4],[2,8],[1,3],[4,2],[2,5],[4,1],[0,2],[6,5]]
print(s.removeStones(stones))
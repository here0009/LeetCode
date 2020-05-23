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

s = Solution()
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# print(s.removeStones(stones))

# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# print(s.removeStones(stones))

# stones = [[0,0]]
# print(s.removeStones(stones))

stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(s.removeStones(stones))

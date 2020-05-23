"""
In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

 

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.
 

Note:

0 <= blocked.length <= 200
blocked[i].length == 2
0 <= blocked[i][j] < 10^6
source.length == target.length == 2
0 <= source[i][j], target[i][j] < 10^6
source != target
"""
"""
Thoughts:
the maximum area blocked is 1+2+3+....+199 = (199+1)*199/2 = 19900
so search 19900 area, if we did not get to the target, return false
"""
import sys
sys.setrecursionlimit(20001)
class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:

        # print(blocked_set)
        def valid(point):
            i,j = point
            return i >= 0 and i < 1e6 and j >= 0 and j < 1e6

        def dfs(start,step):
            

            if not valid(start) or (start in blocked_set) or (start in seen):
                return False
            seen.add(start)
            if start == tuple(target) or step > max_search:
                return True
            
            step += 1
            i,j = start[0],start[1]
            return dfs((i+1,j),step) or dfs((i-1,j),step) or dfs((i,j-1),step) or dfs((i,j+1),step)
        
        max_search = 20000
        blocked_set = set()
        seen = set()
        for i,j in blocked:
            blocked_set.add((i,j))
        return dfs(tuple(source),0)


class Solution_1:
    def isEscapePossible(self, blocked, source, target):
        blocked = set(map(tuple, blocked))
        seen = set()

        def dfs(x, y, target, step=0):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
            seen.add((x, y))
            if step > 20000 or [x, y] == target: return True
            return dfs(x + 1, y, target, step + 1) or \
                dfs(x - 1, y, target, step + 1) or \
                dfs(x, y + 1, target, step + 1) or \
                dfs(x, y - 1, target, step + 1)
        return dfs(source[0], source[1], target) and dfs(target[0], target[1], source)

s = Solution()
blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]
print(s.isEscapePossible(blocked,source,target))

blocked = []
source = [0,0]
target = [999999,999999]
print(s.isEscapePossible(blocked,source,target))


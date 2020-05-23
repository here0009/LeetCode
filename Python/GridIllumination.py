"""
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

 

Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: 
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
 

Note:

1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2
"""
from collections import Counter
class Solution:
    def gridIllumination(self, N: int, lamps, queries):
        rows,cols,diagonals,anti_diagonals = Counter(),Counter(),Counter(),Counter()
        lamps_set = set()
        for i,j in lamps:
            rows[i] += 1
            cols[j] += 1
            diagonals[i-j] += 1
            anti_diagonals[i+j] += 1
            lamps_set.add((i,j))

        directions = [(0,1),(1,0), (-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1),(0,0)]
        res = []
        for i,j in queries:
            if rows[i] > 0 or cols[j] > 0 or diagonals[i-j] > 0 or anti_diagonals[i+j] > 0:
                res.append(1)
            else:
                res.append(0)
            for di,dj in directions:
                tmpi,tmpj = i+di, j+dj
                if (tmpi,tmpj) in lamps_set :
                    lamps_set.remove((tmpi,tmpj))
                    rows[tmpi] -= 1
                    cols[tmpj] -= 1
                    diagonals[tmpi-tmpj] -= 1
                    anti_diagonals[tmpi+tmpj] -= 1
        return res


S = Solution()
N = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]
print(S.gridIllumination(N,lamps, queries))
N = 5
lamps = [[0,0],[0,1],[0,4]]
queries = [[0,0],[0,1],[0,2]]
print(S.gridIllumination(N,lamps, queries))
# Output
# [1,1,0]
# Expected
# [1,1,1]
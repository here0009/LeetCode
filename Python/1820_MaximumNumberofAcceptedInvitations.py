"""
There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

 

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
 

Constraints:

grid.length == m
grid[i].length == n
1 <= m, n <= 200
grid[i][j] is either 0 or 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-accepted-invitations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
        TLE
        """

        def dfs(idx, invitations):
            # print(idx, invitations, self.res)
            if idx == m:
                self.res = max(self.res, invitations)
            if idx == m or m - idx + invitations <= self.res:
                return
            dfs(idx + 1, invitations)
            for j in range(n):
                if grid[idx][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(idx + 1, invitations + 1)
                    visited[j] = 0

        self.res = 0
        m, n = len(grid), len(grid[0])
        # print(m, n)
        visited = [0] * n
        dfs(0, 0)
        return self.res


from typing import List
from functools import lru_cache
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(idx, visited):
            # print(idx, visited)
            if idx == m:
                return 0
            res = dfs(idx + 1, visited)
            for j in range(n):
                if grid[idx][j] == 1 and visited[j] == 0:
                    lst = list(visited)
                    lst[j] = 1
                    res = max(res, 1 + dfs(idx + 1, tuple(lst)))
            return res

        m, n = len(grid), len(grid[0])
        # print(m, n)
        res = dfs(0, tuple([0] * n))
        return res

S = Solution()
grid = [[1,1,1],[1,0,1],[0,0,1]]
print(S.maximumInvitations(grid))
grid = [[1,0,1,0],[1,0,0,0],[0,0,1,0],[1,1,1,0]]
print(S.maximumInvitations(grid))

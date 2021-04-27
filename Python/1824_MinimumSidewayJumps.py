"""
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.

 

Example 1:


Input: obstacles = [0,1,2,3,0]
Output: 2 
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).
Example 2:


Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.
Example 3:


Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.
 

Constraints:

obstacles.length == n + 1
1 <= n <= 5 * 105
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0
"""


from typing import List
from functools import lru_cache
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:

        @lru_cache(None)
        def dp(idx, lane):

            if idx == n:
                print(idx, lane, 0)
                return 0
            if obstacles[idx] == lane:
                return float('inf')
            res = dp(idx + 1, lane)
            for j in range(1, 4):
                if j != lane:
                    res = min(res, 1 + dp(idx, j))
            print(idx, lane, res)
            return res

        n = len(obstacles) - 1
        return dp(0, 2)


from typing import List
from functools import lru_cache
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:

        n = len(obstacles) - 1
        a, b, c = 1, 0, 1
        for i in range(len(obstacles)):
            ob = obstacles[i]
           
            if ob == 1:
                a = float('inf')
            elif ob == 2:
                b = float('inf')
            elif ob == 3:
                c = float('inf')
            a, b, c = min(b + 1, c + 1, a), min(a + 1, c + 1, b), min(a + 1, b + 1, c)
            print(i, ob, '\t', a, b, c)
        return min(a, b, c)

from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[float('inf')] * (n + 1) for _ in range(3)]
        dp[1][0] = 0
        dp[0][0] = 1
        dp[2][0] = 1
        for i in range(1, n + 1):
            ob = obstacles[i]
            for j in range(3):
                if ob - 1 == j:
                    continue
                for k in range(3):
                    if ob - 1 != k:  # if dp[k][i] is an obstacle, frog can not jump from dp[k][i-1] to dp[j][i]
                        dp[j][i] = min(dp[j][i], dp[k][i - 1] + int(j != k))

        # for row in dp:
        #     print(row)
        return min([dp[i][-1] for i in range(3)])


S = Solution()
obstacles = [0,1,2,3,0]
print(S.minSideJumps(obstacles))
obstacles = [0,1,1,3,3,0]
print(S.minSideJumps(obstacles))
obstacles = [0,2,1,0,3,0]
print(S.minSideJumps(obstacles))
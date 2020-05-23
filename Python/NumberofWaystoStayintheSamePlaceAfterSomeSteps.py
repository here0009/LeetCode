"""
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        Thoughts: the most further way you can go is steps//2+1 or arrLen
        """
        M = 10**9+7
        length = min(steps//2+1, arrLen)
        dp = [0]*length
        dp[0] = 1
        while steps > 0:
            dp2 = [0]*length
            for i in range(length):
                left = max(0,i-1)
                right = min(length,i+2)
                dp2[i] = sum(dp[left:right]) % M
            steps -= 1
            dp = dp2
        return dp[0]

from functools import lru_cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dfs(index, step):
            if step == 0:
                return index == 0
            res = 0
            for i in range(max(0, index-1), min(length,index+2)):
                res += dfs(i, step-1)
            # print(index, step, res)
            return res
        
        length = min(steps//2+1, arrLen)
        M = 10**9+7
        return dfs(0,steps) % M

        


S = Solution()
steps = 3
arrLen = 2
print(S.numWays(steps, arrLen))

steps = 2
arrLen = 4
print(S.numWays(steps, arrLen))

steps = 4
arrLen = 2
print(S.numWays(steps, arrLen))

steps = 27
arrLen = 7
print(S.numWays(steps, arrLen))
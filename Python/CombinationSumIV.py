"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""
from functools import lru_cache
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        @lru_cache(None)
        def dfs(t):
            counts = 0
            for num in nums:
                if num > t:
                    break
                elif num == t:
                    counts += 1
                    break
                else:
                    counts += dfs(t-num)
            return counts

        nums = sorted(nums)
        return dfs(target)

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        nums = sorted(nums)
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[target]

S = Solution()

nums = [1, 2, 3]
target = 4
print(S.combinationSum4(nums, target))


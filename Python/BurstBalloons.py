"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


from functools import lru_cache
class Solution:
    def maxCoins(self, nums) -> int:
        """
        wrong answer
        """
        n = len(nums)
        @lru_cache(None)
        def dp(i,j):
            if i == j:
                return nums[i]
            if j-i == 1:
                return nums[i]*nums[j]
            res = max(dp(i,k)+dp(k,j)+nums[i]*nums[j]*nums[k] for k in range(i+1,j))
            print(i,j,res)
            return res

        return dp(0,n-1)


from functools import lru_cache
class Solution:
    def maxCoins(self, nums) -> int:
        nums = nums +[1,1] #append last 2, because they are 1, so did not influence the result
        n = len(nums)
        @lru_cache(None)
        def dp(i,j):
            if j-i < 2:
                return 0
            res = max(dp(i,k)+dp(k,j)+nums[i]*nums[j]*nums[k] for k in range(i+1,j))
            # print(i,j,res)
            return res
        return dp(0,n-1)

class Solution:
    def maxCoins(self, nums) -> int:
        nums = nums + [1,1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        #dp[i][j] represents the max score we can got from i to j
        for size in range(2, n):
            for left in range(n-size):
                right = left+size
                dp[left][right] = max(dp[left][k]+dp[k][right]+nums[left]*nums[k]*nums[right] for k in range(left+1, right))

        # print(dp)
        return dp[0][n-1]

S = Solution()
nums = [3,1,5,8]
print(S.maxCoins(nums))
nums = [8]
print(S.maxCoins(nums))
nums = [3,8]
print(S.maxCoins(nums))


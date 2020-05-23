"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from collections import Counter
class Solution_1:
    def findTargetSumWays(self, nums, S: int) -> int:
        """
        Thoughts: divide nums to two groups, one it positive, the other is negative, return the combinations that makes positive - negative == S
        """
        if nums[0] == 0:
            res = {0:2}
        else:
            res = {nums[0]:1,-1*nums[0]:1}
        for num in nums[1:]:
            next_res = dict()
            for key in res.keys():
                next_res[key-num] = next_res.get(key-num,0)+res[key]
                next_res[key+num] = next_res.get(key+num,0)+res[key]
            res = next_res
            # print(res)
        return res.get(S,0)
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        Explanation:
        We have nums=[1,2,3,4,5] and S=3 for example. There is a solution 1-2+3-4+5=3. After moving nums in negative to the right side, it becomes 1+3+5=3+2+4. Each side is half of sum(nums)+S. This means we can turn this into a knapsack problem with sacks=nums and target_sum=(sum(nums)+S)/2. In this example sacks=[1,2,3,4,5] and target_sum=9. [1,3,5] is one of the solutions.
        """
        nums_sum = sum(nums)
        if (nums_sum + S) % 2 == 1 or abs(S) > nums_sum:
            return 0
        target_sum = (nums_sum + S) //2
        dp = [1] + [0] * target_sum #dp[k] stores the number of sums equal to k, so if we add can num it should add dp[k-num], the larger ones is based on smaller ones.
        for num in nums:
            for s in range(target_sum, num - 1, -1):
                dp[s] += dp[s - num]
            # print(dp, num, target_sum)
        return dp[target_sum]


s = Solution()
# nums = [1, 1, 1, 1, 1]
# S = 3
# print(s.findTargetSumWays(nums, S))

nums = [1,2,3,4,5]
S = 9
print(s.findTargetSumWays(nums, S))
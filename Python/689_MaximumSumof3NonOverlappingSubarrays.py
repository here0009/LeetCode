"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""


from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        preSum = [0]
        part = 3
        for num in nums:
            preSum.append(preSum[-1] + num)
        len_n = len(nums)
        dp = [[0] * (len_n + 1) for _ in range(part + 1)]
        for i in range(1, part + 1):
            dp[i][k] = preSum[k]
            for j in range(k + 1, len_n + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + preSum[j] - preSum[j - k])
        # print(list(range(len_n + 1)))
        # print([0] + nums)
        for row in dp:
            print(row)
        res = []
        pre_index = len_n + 1
        for i in range(part, 0, -1):
            lst = dp[i][:pre_index]
            max_v = max(lst)
            pre_index = lst.index(max_v) - k + 1
            res.append(pre_index - 1)
        return res[::-1]



S = Solution()
nums = [1,2,1,2,6,7,5,1]
k = 2
print(S.maxSumOfThreeSubarrays(nums, k))

nums = [4,3,2,1]
k = 1
print(S.maxSumOfThreeSubarrays(nums, k))

nums = [4,5,10,6,11,17,4,11,1,3]
k = 1
print(S.maxSumOfThreeSubarrays(nums, k))
# Output
# [2,4,5]
# Expected
# [4,5,7]
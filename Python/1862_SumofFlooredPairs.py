"""
Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

 

Example 1:

Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
Example 2:

Input: nums = [7,7,7,7,7,7,7]
Output: 49
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""


from typing import List
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:

        """
        Thoughts: use preSum to record the counts of num at each position.
        calculate pairs for each num in nums
        """

        M = 10**9 + 7
        max_num = max(nums)
        counts = [0] * (max_num + 1)
        for num in nums:
            counts[num] += 1
        preSum = [0] * (max_num + 1)
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i - 1] + counts[i]

        res = 0
        # print(preSum)
        # print(counts)
        for num, count in enumerate(counts):
            if count > 0:
                k = 1
                while num * k <= max_num:
                    res += count * k * (preSum[min(num * (k + 1) - 1, max_num)] - preSum[num * k - 1])
                    res = res % M
                    k += 1

        return res


S = Solution()
nums = [2,5,9]
print(S.sumOfFlooredPairs(nums))
nums = [7,7,7,7,7,7,7]
print(S.sumOfFlooredPairs(nums))
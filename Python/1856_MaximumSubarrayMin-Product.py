"""
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 107
"""


from typing import List
from functools import lru_cache
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        @lru_cache(None)
        def calc(i, j):
            if i > j:
                return 0
            if i == j:
                return nums[i] ** 2
            min_val = min(nums[i: j + 1])
            res = (preSum[j + 1] - preSum[i]) * min_val
            pre, latter = i, i
            while pre <= j:
                while pre <= j and nums[pre] == min_val:
                    pre += 1
                latter = pre
                while latter <= j and nums[latter] != min_val:
                    latter += 1
                if pre >= latter:
                    break
                res = max(res, calc(pre, latter - 1))
                pre = latter + 1
            return res

        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        M = 10**9 + 7
        return calc(0, len(nums) - 1) % M


from typing import List
from functools import lru_cache
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

S = Solution()
nums = [1,2,3,2]
print(S.maxSumMinProduct(nums))
nums = [2,3,3,1,2]
print(S.maxSumMinProduct(nums))
nums = [3,1,5,6,4,2]
print(S.maxSumMinProduct(nums))
# nums = 
# 631781618
# 951004314
# 999995547
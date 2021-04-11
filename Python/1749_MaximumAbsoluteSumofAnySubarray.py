"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""


from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_val, min_val = -float('inf'), float('inf')
        tmp_max, tmp_min = 0, 0
        # print(nums)
        for num in nums:
            tmp_max = max(tmp_max + num, 0)
            max_val = max(max_val, tmp_max)

            tmp_min = min(tmp_min + num, 0)
            min_val = min(min_val, tmp_min)
            # print(num, tmp_max, tmp_min)
        return max(abs(max_val), abs(min_val))


S = Solution()
nums = [1,-3,2,3,-4]
print(S.maxAbsoluteSum(nums))
nums = [2,-5,1,-4,3,-2]
print(S.maxAbsoluteSum(nums))
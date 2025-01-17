from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        pre_sum = 0
        res = 0
        for i in range(0, len(nums) - 1):
            pre_sum += nums[i]
            if pre_sum >= total - pre_sum:
                res += 1
        return res
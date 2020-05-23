"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target :
                    l += 1
                elif total > target :
                    r -= 1
                else:
                    return target
        return res

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))

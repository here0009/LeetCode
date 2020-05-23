"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        nums = [0]+nums
        len_nums = len(nums)
        for i in range(3,len_nums-1):
            nums[i] += max(nums[i-2],nums[i-3])
        tmp = nums[len_nums-4]
        if len_nums-4 == 1:
            tmp -= nums[1]
        nums[len_nums-1] += max(nums[len_nums-3], tmp)
        print(nums)
        return max(nums)

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        nums_a = [0] + nums[1:] #remove 1st
        nums_b = [0] + nums[:-1] #remove last
        res = 0
        for i in range(3,len(nums)):
            nums_a[i] += max(nums_a[i-2],nums_a[i-3]) 
            nums_b[i] += max(nums_b[i-2],nums_b[i-3])
            res  = max(nums_a[i], nums_b[i], res)
        # print(nums_a)
        # print(nums_b)
        return res


s = Solution()
nums = [2,3,2]
print(s.rob(nums))
nums = [1,2,3,1]
print(s.rob(nums))
nums = [1,2]
print(s.rob(nums))
nums = []
print(s.rob(nums))
nums = [1,2,1,1]
print(s.rob(nums))
nums = [2,7,9,3,1]
print(s.rob(nums))
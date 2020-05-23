"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution_1:
    def threeSum(self, nums):
        res_set = set()
        nums = sorted(nums)
        # print(nums)
        len_nums = len(nums)
        for i in range(len_nums):
            l,r = i+1, len_nums-1
            while l < r:
                sum_3 = nums[i] + nums[l] + nums[r]
                if sum_3 > 0:
                    r-=1
                elif sum_3 < 0:
                    l+=1
                else:
                    res_set.add((nums[i],nums[l],nums[r]))
                    l += 1
        res = []
        for i,j,k in res_set:
            res.append([i,j,k])
        return res


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        len_nums = len(nums)
        res = []
        for i in range(len_nums-2):
            if nums[i] > 0 : 
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len_nums-1
            while l < r:
                sum_3 = nums[i] + nums[l] + nums[r]
                if sum_3 > 0:
                    r -= 1
                elif sum_3 < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res
                

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))

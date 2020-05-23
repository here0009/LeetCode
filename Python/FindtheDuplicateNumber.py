"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution_1:
    def findDuplicate(self, nums):
        nums = sorted(nums)
        pre = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == pre:
                return pre
            pre = nums[i]

class Solution:
    def findDuplicate(self, nums):
        sum_nums = sum(nums)
        set_nums = set(nums)
        sum_set_nums = sum(set_nums)
        length = len(nums) - len(set_nums)
        return int((sum_nums - sum_set_nums)/length) 

s = Solution()
l = [1,3,4,2,2]
print(s.findDuplicate(l))
l = [3,1,3,4,2]
print(s.findDuplicate(l))
l = [1,4,4,2,4]
print(s.findDuplicate(l))

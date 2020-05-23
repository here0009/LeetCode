"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
class Solution:
    def checkPossibility(self, nums) -> bool:
        small = set()
        large = set()
        len_num = len(nums)
        for i in range(len_num):
            for j in range(i+1, len_num):
                if nums[i] > nums[j]:
                    small.add(i)
                    large.add(j)
            if len(small) > 1 and len(large) > 1:
                return False
        return True

class Solution:
    def checkPossibility(self, nums) -> bool:
        counts = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counts += 1
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
            if counts > 1:
                return False
        return True

s = Solution()
nums = [4,2,3]
print(s.checkPossibility(nums))
nums = [4,2,1]
print(s.checkPossibility(nums))
nums = [1]
print(s.checkPossibility(nums))
nums = [2,3,3,2,4]
print(s.checkPossibility(nums))
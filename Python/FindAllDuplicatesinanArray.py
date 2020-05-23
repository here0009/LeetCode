"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
import pysnooper
class Solution_1:
    # @pysnooper.snoop('./pysnooper.log')
    def findDuplicates(self, nums):
        index = 0
        res = []
        nums = [0, *nums]
        # return nums
        while index < len(nums):
            print(nums)
            if nums[index] <= 0:
                index += 1
            else:
                change_index = nums[index]
                while change_index > 0:
                    tmp_index = nums[change_index]
                    if nums[change_index] == 0:
                        nums[change_index] -= 1
                    else:
                        nums[change_index] = 0
                    change_index = tmp_index
                index += 1
        
        for i in range(len(nums)):
            if nums[i] <= -1:
                res.append(i)
        return res

class Solution:
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                res.append(index+1)
        return res



s = Solution_1()
nums = [4,3,2,7,8,2,3,1]
print(s.findDuplicates(nums))


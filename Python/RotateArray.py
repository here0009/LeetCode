"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution_1:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        nums_copy = nums[:]
        for i in range(len_nums):
            nums[(i+k)%len_nums] = nums_copy[i]
        print(nums)

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = 0
        len_nums = len(nums)
        k = k % len_nums
        index = 0
        while counts < len_nums:
            pre = index
            tmp = nums[pre]
            while True:
                next_index = (index+k) % len_nums
                next_tmp = nums[next_index]
                nums[next_index] = tmp
                tmp = next_tmp
                index = next_index
                counts += 1
                if index == pre:
                    break
            index += 1
        print(nums)
            
             

s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
s.rotate(nums,k)

nums = [-1,-100,3,99] 
k = 2
s.rotate(nums,k)
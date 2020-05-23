"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
"""
Thoughts 1:
use two lists to store the positon information of zeros and n non-zero elments in the array, then change the zero and non-zero elements.
It is wrong.
"""

# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """

#         zero_positon = []
#         for index, num in enumerate(nums):
#             if num == 0:
#                 zero_positon.append(index)

#         len_zero = len(zero_positon)
#         if len_zero == 0 or len_zero == 1:
#             print (nums)
#             return

#         non_zero_position = []
#         for index, num in enumerate(nums[::-1]):
#             if num != 0:
#                 non_zero_position.append(len(nums) - index)
#                 if len(non_zero_position) == len_zero:
#                     break

#         print(non_zero_position)
#         non_zero_position = non_zero_position[::-1]

#         for i in range(len_zero):
#             nums[zero_positon[i]],nums[non_zero_position[i]] = nums[non_zero_position[i]], nums[zero_positon[i]]

#         print(zero_positon)
#         print(non_zero_position)
#         print (nums)
#         return


"""
Thoughts 2:
Use the method like bubble sort, move zero to the end of the array.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        while index < len(nums)-1:
            num = nums[index]
            if num == 0:
                tmp_index = index + 1
                while (tmp_index < len(nums)):
                    if nums[tmp_index] != 0:
                        tmp_num = nums[index]
                        nums[index] = nums[tmp_index]
                        nums[tmp_index] = tmp_num
                        break
                    else:
                        tmp_index += 1
            index += 1
        # print(nums)
        return


s = Solution()
test = [0,1,0,3,12]
print(s.moveZeroes(test))

test = [0]
print(s.moveZeroes(test))

test = [0,1,3,5,0,0,9,99,0,365,0]
print(s.moveZeroes(test))

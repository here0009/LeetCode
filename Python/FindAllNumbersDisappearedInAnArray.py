"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]

#         """
#         n = len(nums)
#         print(n)
#         if n == 0 or n == 1:
#             return []
#         index = nums[0]
#         start = 0
        
#         ans = list()
#         while start < n - 1:
#             if nums[index-1] != -1:
#                 # print(index)
#                 tmp = nums[index-1]
#                 nums[index-1] = -1
#                 index = tmp
#             else:
#                 start += 1
#                 index = nums[start]
#         if index != -1:
#             nums[index-1] = -1
#         for i, num in enumerate(nums):
#             if num != -1:
#                 ans.append(i+1)
#         return ans

"""
My submission can not pass the last test, and it is really ugly.
Looks for the discussion board, one genious way to do the job is use the absolute value to store the indext information while set the index of the exsiting number as negative number.
The code is crystal clear.
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        for i, num in enumerate(nums):
            if num > 0 :
                ans.append(i+1)
        return ans


s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))

nums = [1,2]
print(s.findDisappearedNumbers(nums))

nums = [2,2]
print(s.findDisappearedNumbers(nums))

nums = [3,11,8,16,4,15,4,17,14,14,6,6,2,8,3,12,15,20,20,5]
# expected = [1,7,9,10,13,18,19]
print(s.findDisappearedNumbers(nums))
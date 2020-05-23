"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
class Solution:
    def dominantIndex(self, nums) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 0
        max_index = -1
        max_num = nums[0]
        for index,num in enumerate(nums):
            if num > max_num:
                pre_max, max_num = max_num, num
                if pre_max and max_num / pre_max >= 2:
                    max_index = index
                else:
                    max_index = -1
            else:
                if num and max_num / num < 2:
                    max_index = -1
        return max_index

s = Solution()
nums = [3, 6, 1, 0]
print(s.dominantIndex(nums))

nums = [1, 2, 3, 4]
print(s.dominantIndex(nums))


nums = [3]
print(s.dominantIndex(nums))

nums = [1, 2, 3, 6, 36, 12]
print(s.dominantIndex(nums))
        

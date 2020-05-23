"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
"""
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        res = 1
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                tmp += 1
                if tmp > res:
                    res = tmp
            else:
                tmp = 1
        return res

s = Solution()
nums = [1,3,5,4,7]
print(s.findLengthOfLCIS(nums))

nums = [2,2,2,2,2]
print(s.findLengthOfLCIS(nums))

nums = []
print(s.findLengthOfLCIS(nums))

nums = [1,3,5,4,2,3,4,5]
print(s.findLengthOfLCIS(nums))
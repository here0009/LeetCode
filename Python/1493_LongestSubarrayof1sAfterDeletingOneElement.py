"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""


class Solution:
    def longestSubarray(self, nums) -> int:
        gap, nogap = 0, 0
        res = 0
        for num in nums:
            if num == 0:
                gap = nogap
                nogap = 0
            else:
                gap += 1
                nogap += 1
            res = max(res, gap)
        if res == len(nums):
            res -= 1
        return res

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/708112/JavaC%2B%2BPython-Sliding-Window-at-most-one-0
class Solution:
    def longestSubarray(self, nums) -> int:
        gap = 1
        left = 0
        for right in range(len(nums)):
            gap -= nums[right] == 0
            if gap < 0:
                gap += nums[left] == 0
                left += 1
        return right - left

S = Solution()
nums = [1,1,0,1]
print(S.longestSubarray(nums))
nums = [0,1,1,1,0,1,1,0,1]
print(S.longestSubarray(nums))
nums = [1,1,1]
print(S.longestSubarray(nums))
nums = [1,1,0,0,1,1,1,0,1]
print(S.longestSubarray(nums))
nums = [0,0,0]
print(S.longestSubarray(nums))

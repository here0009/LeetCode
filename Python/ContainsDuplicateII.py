"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        gap_dict = dict()
        for index, num in enumerate(nums):
            if num not in gap_dict:
                gap_dict[num] = index
            else:
                if index - gap_dict[num] <= k:
                    return True
                else:
                    gap_dict[num] = index
        return False

s = Solution()
nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))
nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(nums, k))
nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))
nums = []
k = 1
print(s.containsNearbyDuplicate(nums, k))
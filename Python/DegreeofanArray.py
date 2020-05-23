"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from collections import defaultdict
from math import inf
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = defaultdict(list)
        min_interval = inf
        max_len = 0
        for index, num in enumerate(nums):
            nums_dict[num].append(index)
            max_len = max(max_len, len(nums_dict[num]))
        for key, value in nums_dict.items():
            if len(value) == max_len:
                min_interval = min(min_interval, value[-1]-value[0]+1)
        return min_interval

s = Solution()
test = [1, 2, 2, 3, 1]
print(s.findShortestSubArray(test))
test = [1,2,2,3,1,4,2]
print(s.findShortestSubArray(test))
test = [1]
print(s.findShortestSubArray(test))
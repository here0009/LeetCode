"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""


from typing import List
from collections import Counter

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, left, right, counts = 0, 0, 0, 0
        max_val = max(nums)
        length = len(nums)
        while right < length:
            counts += nums[right] == max_val
            while counts >= k:
                if nums[left] == max_val:
                    counts -= 1
                left += 1
            res += left
            right +=1
        return res

sol = Solution()
nums = [1,3,2,3,3]
k = 2
print(sol.countSubarrays(nums, k))
nums = [1,4,2,1]
k = 3
print(sol.countSubarrays(nums, k))
nums = [3,1,1]
k = 1
print(sol.countSubarrays(nums, k))
nums = [28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49]
k = 1
print(sol.countSubarrays(nums, k))
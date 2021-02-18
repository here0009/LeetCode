"""
An array A is larger than some array B if for the first index i where A[i] != B[i], A[i] > B[i].

For example, consider 0-indexing:

[1,3,2,4] > [1,2,2,4], since at index 1, 3 > 2.
[1,4,4,4] < [2,1,1,1], since at index 0, 1 < 2.
A subarray is a contiguous subsequence of the array.

Given an integer array nums of distinct integers, return the largest subarray of nums of length k.

 

Example 1:

Input: nums = [1,4,5,2,3], k = 3
Output: [5,2,3]
Explanation: The subarrays of size 3 are: [1,4,5], [4,5,2], and [5,2,3].
Of these, [5,2,3] is the largest.
Example 2:

Input: nums = [1,4,5,2,3], k = 4
Output: [4,5,2,3]
Explanation: The subarrays of size 4 are: [1,4,5,2], and [4,5,2,3].
Of these, [4,5,2,3] is the largest.
Example 3:

Input: nums = [1,4,5,2,3], k = 1
Output: [5]
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-subarray-length-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        """
        TLE
        """
        res = nums[:k]
        for i in range(1, len(nums) - k + 1):
            res = max(res, nums[i : i + k])
        return res

from typing import List
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            max_val = max(nums)
        else:
            max_val = max(nums[:-(k - 1)])
        res = nums[:k]
        for i in range(1, len(nums) - k + 1):
            if nums[i] < max_val:
                continue
            res = max(res, nums[i : i + k])
        return res

S = Solution()
nums = [1,4,5,2,3]
k = 3
print(S.largestSubarray(nums, k))
nums = [1,4,5,2,3]
k = 4
print(S.largestSubarray(nums, k))
nums = [1,4,5,2,3]
k = 1
print(S.largestSubarray(nums, k))
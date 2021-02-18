"""
You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3*10^4
-10^5 <= nums[i] <= 10^5
"""


# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489882/O(n)-Solution-with-explanation
from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """
        there are 4 values will be influenced by the reverse, let's denote them as a,b,c,d and a <= b <= c <= d
        at the beigining the pair is a-b, c-d
        the sign of max(a, b, c, d) won't change, the sign of min(a, b, c, d) won't change.
        b will be -b and c will be -c
        so the max diff we can get is (2*(b - c))
        """
        base, diff = 0, 0
        max_v, min_v = -float('inf'), float('inf')
        for i in range(1, len(nums)):
            a, b = nums[i - 1], nums[i]
            base += abs(a - b)
            max_v = max(max_v, min(a, b))
            min_v = min(min_v, max(a, b))
            diff = max(diff, max(abs(b - nums[0]), abs(a - nums[-1])) - abs(a - b))  # reverse A[:i] and A[i:]
        return base + max([0, diff, 2 * (max_v - min_v)])


S = Solution()
nums = [2,3,1,5,4]
print(S.maxValueAfterReverse(nums))
nums = [2,4,9,24,2,1,10]
print(S.maxValueAfterReverse(nums))
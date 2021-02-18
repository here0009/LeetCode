"""
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 104
"""


from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        def split2(min_val, min_idx):
            half = (total - min_val) // 2
            if half < min_val:
                return 0
            res = 0
            lidx = min(len_p - 1, bisect_left(preSum, min_val * 2, lo=min_idx))
            ridx = min(len_p - 1, bisect_right(preSum, min_val + half, lo=lidx))
            res = max(0, ridx - lidx)
            return res


        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        M = 10**9 + 7
        len_p = len(preSum)
        total = preSum[-1]
        onethird = total // 3
        res = 0
        for i in range(1, len_p):
            if preSum[i] > onethird:
                break
            res = (res + split2(preSum[i], i + 1)) % M
        return res

S = Solution()
nums = [1,1,1]
print(S.waysToSplit(nums))
nums = [1,2,2,2,5,0]
print(S.waysToSplit(nums))
nums = [3,2,1]
print(S.waysToSplit(nums))
nums = [0,3,3]
print(S.waysToSplit(nums))
# 输出：
# 3
# 预期：
# 1
nums = [7,2,5,5,6,2,10,9]
print(S.waysToSplit(nums))
# 输出：
# 7
# 预期：
# 6
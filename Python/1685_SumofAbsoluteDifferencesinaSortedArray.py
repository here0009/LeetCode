"""
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
"""


from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        nums2 = sorted((v, i) for i, v in enumerate(nums))
        preSum = [0]
        for v, _ in nums2:
            preSum.append(preSum[-1] + v)
        # print(nums2)
        # print(preSum)
        res = [0] * len_n
        for i in range(len_n):
            v, j = nums2[i]
            res[j] = preSum[-1] - 2 * preSum[i] - (len_n - 2 * i) * v
        return res

S = Solution()
nums = [2,3,5]
print(S.getSumAbsoluteDifferences(nums))

nums = [1,4,6,8,10]
print(S.getSumAbsoluteDifferences(nums))
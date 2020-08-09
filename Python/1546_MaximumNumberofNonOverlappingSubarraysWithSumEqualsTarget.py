"""
Given an array nums and an integer target.

Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
Example 3:

Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3
Example 4:

Input: nums = [0,0,0], target = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
"""


from functools import lru_cache
class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        """
        TLE
        """
        preSum = [0]
        # length = len(nums)
        tmp = 0
        length = len(nums)+1
        for num in nums:
            tmp += num
            preSum.append(tmp)
        # print(preSum)
        pos_list = []
        for i in range(length):
            for j in range(i+1, length):
                if preSum[j] - preSum[i] == target:
                    pos_list.append((i,j))
        # print(pos_list)
        pos_list.sort(key = lambda x:(x[0], x[1]))
        res, end = 0, 0
        for i, j in pos_list:
            if i >= end:
                res += 1
                end = j
            else:
                end = min(end, j)
        return res


class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        """
        TLE
        """
        preSum = [0]
        # length = len(nums)
        tmp = 0
        length = len(nums)+1
        for num in nums:
            tmp += num
            preSum.append(tmp)
        # print(preSum)
        pos_list = []
        for i in range(length):
            for j in range(i+1, length):
                if preSum[j] - preSum[i] == target:
                    pos_list.append((i,j))
        # print(pos_list)
        pos_list.sort(key = lambda x:(x[0], x[1]))
        res, end = 0, 0
        for i, j in pos_list:
            if i >= end:
                res += 1
                end = j
            else:
                end = min(end, j)
        return res


class Solution:
    def maxNonOverlapping(self, nums, target: int) -> int:
        seen = set([0])
        res = 0
        curr = 0
        for num in nums:
            curr += num
            if curr - target in seen:
                res += 1
                seen = set()
            seen.add(curr)
        return res


S = Solution()
nums = [1,1,1,1,1]
target = 2
print(S.maxNonOverlapping(nums, target))
nums = [-1,3,5,1,4,2,-9]
target = 6
print(S.maxNonOverlapping(nums, target))
nums = [-2,6,6,3,5,4,1,2,8]
target = 10
print(S.maxNonOverlapping(nums, target))
nums = [0,0,0]
target = 0
print(S.maxNonOverlapping(nums, target))

"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        tmp = sum(nums[:k])
        res = tmp
        for i in range(k,len(nums)):
            tmp = tmp+nums[i]-nums[i-k]
            res = max(res, tmp)
        return res/k

S = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(S.findMaxAverage(nums,k))

nums = [0,4,0,3,2]
k = 1
print(S.findMaxAverage(nums,k))
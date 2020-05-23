"""
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:
        """
        dp[i] represents the max sum start with i
        so dp[i] = max(dp[i+j] for j in range(1,k+1)) + nums[i]
        TLE
        if k is very large, find the max value of k may cost lots of time, try to use a heap to store the max values
        """
        length = len(nums)
        dp = [0]*length
        for i in range(length-1, -1, -1):
            tmp = 0
            for j in range(1,k+1):
                if i+j >= length:
                    break
                tmp = max(tmp, dp[i+j])
            dp[i] = tmp + nums[i]
            # print(dp)
        return max(dp)

import heapq
class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:
        length = len(nums)
        res = -float('inf')
        max_vals = [(0,-float('inf'))]
        heapq.heapify(max_vals)
        for i in range(length-1, -1, -1):
            while max_vals[0][1] > i+k: #out of range
                heapq.heappop(max_vals)
            # print(max_vals)
            tmp = -max_vals[0][0] + nums[i]
            res = max(res, tmp)
            heapq.heappush(max_vals, (-tmp,i))
        return res

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:
        """
        use a decreasing deque to store the values of the last k elements
        """
        dq = deque()
        res = -float('inf')
        for i,v in enumerate(nums):
            while dq and dq[0][1] < i-k:
                dq.popleft()
            tmp = nums[i]
            if dq:
                tmp += dq[0][0]
            while dq and tmp >= dq[-1][0]:
                dq.pop()
            if tmp > 0:
                dq.append((tmp,i))
            res = max(res, tmp)
        return res



        

S = Solution()
nums = [10,2,-10,5,20]
k = 2
print(S.constrainedSubsetSum(nums, k))
nums = [-1,-2,-3]
k = 1
print(S.constrainedSubsetSum(nums, k))
nums = [10,-2,-10,-5,20]
k = 2
print(S.constrainedSubsetSum(nums, k))

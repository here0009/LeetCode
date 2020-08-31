"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i-1] == 0 and nums[i] == 0:
                    return True
            return False

        mod_nums = [num % k for num in nums]
        preSum = [0]
        for i in range(len(mod_nums)):
            preSum.append(preSum[-1] + mod_nums[i])
        for i in range(len(preSum)-2):
            for j in range(i+2, len(preSum)):
                if (preSum[j] - preSum[i]) % k == 0:
                    # print(i,j)
                    return True
        return False
# # https://leetcode.com/problems/continuous-subarray-sum/discuss/236976/Python-solution
# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
class Solution():
    def checkSubarraySum(self, nums, k):
        maps = {0:-1}
        tmp = 0
        for i, num in enumerate(nums):
            if k != 0:
                tmp = (tmp + num) % k
            else: 
                tmp += num
            if tmp not in maps:
                maps[tmp] = i
            else:
                if i - maps[tmp] > 1:
                    return True 
        return False



S = Solution()
nums = [23, 2, 4, 6, 7]
k=6
print(S.checkSubarraySum(nums, k))
nums = [23, 2, 6]
k=6
print(S.checkSubarraySum(nums, k))
nums = [23,2,6,4,7]
k = 0
print(S.checkSubarraySum(nums, k))
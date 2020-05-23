"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution_1:
    def minSubArrayLen(self, s: int, nums) -> int:
        #Memory Limit Exceeded
        if not nums:
            return 0
        v_dict = {0:0} #value:index
        pre_sum = [0] + nums
        for i in range(1,len(pre_sum)):
            pre_sum[i] += pre_sum[i-1]
            for v in range(pre_sum[i-1]+1, pre_sum[i]+1):
                v_dict[v] = i
        # print(pre_sum)
        # print(v_dict)
        res = float('inf')
        for i in range(len(nums)-1):
            if pre_sum[i]+s not in v_dict:
                break
            else:
                res = min(res, v_dict[pre_sum[i]+s]-i)
        if res == float('inf'):
            return 0
        else:
            return res

from bisect import bisect_left
class Solution_2:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        v_dict = {0:0} #value:index
        pre_sum = [0] + nums
        length = len(pre_sum)
        for i in range(1,length):
            pre_sum[i] += pre_sum[i-1]
        # print(pre_sum)
        res = float('inf')
        for i in range(len(nums)-1):
            k = bisect_left(pre_sum, pre_sum[i]+s)
            # print(k,)
            if k == length:
                break
            else:
                res = min(res, k-i)
        if res == float('inf'):
            return 0
        else:
            return res



class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        left_index,total = 0,0
        res = float('inf')
        for i in range(len(nums)):
            total += nums[i]
            while total >= s: 
                res = min(res, i-left_index+1) 
                total -= nums[left_index] #i will plus 1 next round, so left_index should go as far as it can
                left_index += 1
        if res == float('inf'):
            return 0
        else:
            return res



S = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(S.minSubArrayLen(s,nums))

s = 100
nums = []
print(S.minSubArrayLen(s,nums))

s = 15
nums = [1,2,3,4,5]
print(S.minSubArrayLen(s,nums))


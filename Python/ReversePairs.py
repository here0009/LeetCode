"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
from bisect import bisect_left
class Solution:
    def reversePairs(self, nums) -> int:
        """
        TLE
        """
        sort_n = sorted((v,i) for i,v in enumerate(nums))
        res = 0
        # print(sort_n)
        for i,n in enumerate(nums):
            start = bisect_left(sort_n, (2*n+1,0))
            # print(i,n,start)
            res += sum([1 for v,j in sort_n[start:] if j<i])
        return res

from collections import Counter
from bisect import bisect_left
class Solution:
    """
    TLE
    """
    def reversePairs(self, nums) -> int:
        n_counter = Counter(nums)
        n_counter_keys = sorted(list(n_counter.keys()))
        # print(n_counter_keys)
        res = 0
        for n in nums[::-1]:
            n_counter[n] -= 1
            # if n_counter[n] == 0:
            #     n_counter_keys.remove(n)
            index = bisect_left(n_counter_keys, 2*n+1)
            res += sum([n_counter[key] for key in n_counter_keys[index:]])
            # print(res)
        return res

S = Solution()
nums = [1,3,2,3,1]
print(S.reversePairs(nums))
nums = [2,4,3,5,1]
print(S.reversePairs(nums))

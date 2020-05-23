"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        counter_nums = Counter(nums)
        min_counts = len(nums)//3
        # print(min_counts)
        res = [k for k,v in counter_nums.items() if v>min_counts]
        return res

class Solution:      
    def majorityElement(self, nums):
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            # print('pre_ctr:', ctr)
            if len(ctr) == 3:
                ctr -= Counter(set(ctr))
            # print('aft_ctr:', ctr)
        return [n for n in ctr if nums.count(n) > len(nums)/3]


S = Solution()
nums = [3,2,3]
print(S.majorityElement(nums))
nums = [1,1,1,3,3,2,2,2]            
print(S.majorityElement(nums))
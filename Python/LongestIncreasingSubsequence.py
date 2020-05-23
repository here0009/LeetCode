"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    def lengthOfLIS(self, nums) -> int:
        stack = []
        res = 0
        storage = dict()
        for num in nums:
            print(stack)
            len_stack = len(stack)
            while len_stack > 0 and stack[-1] >= num:
                k = stack.pop()
                storage[k] = max(storage.get(k,0), len_stack)
                len_stack -= 1

            for n,v in storage.items():
                if num > n and v <= res:
                    res = max(res,v + 1)

            stack.append(num)
            # print(storage)
            res = max(res, len(stack))
        return res

import bisect
class Solution:
    def lengthOfLIS(self, nums) -> int:
        """
        keep an increasing list, bisect_left to find the insert point of num in nums return the length of the increasing list
        """
        incrs = []
        res = 0
        for i in range(len(nums)):
            # print(incrs)
            k = bisect.bisect_left(incrs,nums[i])
            if k >= len(incrs):
                incrs.append(nums[i])
            else:
                incrs[k] = nums[i]
        return len(incrs)


s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))

nums = []
print(s.lengthOfLIS(nums))

nums = [2]
print(s.lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(s.lengthOfLIS(nums))

nums = [3,5,6,2,5,4,19,5,6,7,12]
print(s.lengthOfLIS(nums))
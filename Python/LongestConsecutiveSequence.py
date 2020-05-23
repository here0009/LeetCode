"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums) -> int:
        res = 0
        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set: #the key step, start the counting
                i,counts = n,1
                while i+1 in nums_set:
                    i+= 1
                    counts += 1
                res = max(res, counts)
        return res

S = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(S.longestConsecutive(nums))

nums = [0,-1]
print(S.longestConsecutive(nums))
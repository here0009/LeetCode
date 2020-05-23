"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
        
        res_set = set()
        if len(nums) == 1:
            return nums[0]
        for i,n in enumerate(nums):
            tmp = [(n,p) for p in self.permuteUnique(nums[:i]+nums[i+1:])]
            for k in tmp:
                tuple_k = tuple(k)
                if tuple_k not in res_set:
                    res += tmp
                res_set.add(tuple_k)
        print(res_set)
        res = []
        return res

from collections import Counter
class Solution:
    def permuteUnique(self, nums):
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums_counter:
                if nums_counter[n] >0:
                    nums_counter[n] -= 1
                    path.append(n)
                    backtrack(path)
                    path.pop()
                    nums_counter[n] += 1

        res = []
        nums_counter = Counter(nums)
        backtrack([])
        return res

s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))
"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        nums_set = set(nums)
        tmp = [[num] for num in nums]
        res = []
        for _ in range(len(nums)-1):
            for l in tmp:
                for num in nums_set:
                    if num not in set(l):
                        tmp.append(l+[num])
        return res

class Solution_1:
    def permute(self, nums):
        def backtrack(res,curr):
            # print(curr)
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in nums:
                if i not in set(curr):
                    curr.append(i)
                    backtrack(res,curr)
                    curr.pop()


        nums_set = set(nums)
        res = []
        for i in nums:
            backtrack(res,[i])
        return res

class Solution_3:
    def permute(self, nums):
        def backtrack(curr):
            # print(curr)
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in nums:
                if i not in set(curr):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()


        nums_set = set(nums)
        res = []
        for i in nums:
            backtrack([i])
        return res

class Solution:
    def permute(self, nums):
        res = []
        if len(nums) == 1:
            return [[nums[0]]]
        for i,n in enumerate(nums):
            res += [[n] + p for p in self.permute(nums[:i]+nums[i+1:])]
        # print(res)
        return res

class Solution:
    def permute(self, nums):
        res = []
        for i,n in enumerate(nums):
            res += [[n] + p for p in self.permute(nums[:i]+nums[i+1:])]
        # print(res)
        return res or [[]]


s = Solution()
nums = [1,2,3]
print(s.permute(nums))


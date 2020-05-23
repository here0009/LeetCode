"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
from collections import Counter
class Solution:
    def combinationSum2(self, candidates, target: int):
        def backtrack(curr):
            total = sum(curr)
            if total  == target:
                tmp = tuple(sorted(curr))
                if tmp not in res_set:
                    res.append(curr[:])
                res_set.add(tmp)
                return
            elif total > target:
                return
            else:
                for c in candidates:
                    if c_Counter[c] > 0:
                        curr.append(c)
                        c_Counter[c] -= 1
                        backtrack(curr)
                        curr.pop()
                        c_Counter[c] += 1
        
        res = []
        res_set = set()
        c_Counter = Counter(candidates)
        # candidates = list(c_Counter.keys())
        backtrack([])
        return res

class Solution_1:
    def combinationSum2(self, candidates, target: int):
        def dfs(path,total,start):
            if total == target:
                res.append(path)
            elif total > target:
                return
            else:
                for i in range(start+1, len_c):
                    if i == start+1 or candidates[i] != candidates[i-1]: #append the 1st element
                        c = candidates[i]
                        dfs(path+[c], total+c, i)

        res = []
        len_c = len(candidates)
        candidates = sorted(candidates)
        for i,v in enumerate(candidates):
            if i == 0 or candidates[i] != candidates[i-1]:
                dfs([v],v,i)
        
        return res


class Solution_1:
    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
        
    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return
        
        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])

class Solution:
    def combinationSum2(self, candidates, target: int):
        def dfs(path,target,index):
            if target == 0:
                res.append(path)
                return
            for i in range(index, len_c):
                if i == index or candidates[i] != candidates[i-1]: #append the 1st element
                    if candidates[i] > target: #backtrack, not i itself, but i+1 and afterwards
                        break
                    dfs(path+[candidates[i]], target-candidates[i], i+1)

        res = []
        len_c = len(candidates)
        candidates = sorted(candidates)
        dfs([], target, 0)
        return res


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))

candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))
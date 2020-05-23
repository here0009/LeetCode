"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
import copy
class Solution_1:
    def combinationSum(self, candidates, target: int):
        """
        res with repeated answer
        """
        def helper(target, ex_l):
            # print(res)
            for c in candidates:
                if c == target:
                    tmp = copy.deepcopy(ex_l)
                    tmp.append(c)
                    res.append(tmp)
                elif c < target:
                    tmp = copy.deepcopy(ex_l)
                    tmp.append(c)
                    helper(target-c, tmp)

        res = []
        helper(target,[])
        return res

class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)
        tmp = [[c] for c in candidates]
        res = []
        while tmp:
            # print(tmp)
            q = tmp.pop()
            v = sum(q)
            if v < target:
                for c in candidates:
                    if c < q[-1]: #avoid repeated elements
                        continue
                    new_q = q + [c]
                    tmp.append(new_q)
            elif v == target:
                res.append(q)
        
        return res



s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates,target))

candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates,target))


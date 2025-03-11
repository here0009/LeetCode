"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


from typing import List,Dict
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(lst:List[int], rmd_counts:Dict[int, int]):
            if len(lst) == n:
                res.append(lst)
            for k, v in rmd_counts.items():
                if v > 0:
                    rmd_counts[k] = v - 1
                    dfs(lst + [k], rmd_counts)
                    rmd_counts[k] = v
        
        n = len(nums)
        res = []
        counts = Counter(nums)
        dfs([], counts)
        return res

s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))
nums = [1,2,3]
print(s.permuteUnique(nums))
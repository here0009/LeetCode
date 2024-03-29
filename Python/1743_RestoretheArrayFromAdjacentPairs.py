"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
 

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.
"""


from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(i):
            visited.add(i)
            self.res.append(i)
            for ni in edges[i]:
                if ni not in visited:
                    dfs(ni)

        edges = defaultdict(set)
        for p, q in adjacentPairs:
            edges[p].add(q)
            edges[q].add(p)
        visited = set()
        for p in edges:
            if len(edges[p]) == 1:
                start = p
                break
        visited = set()
        self.res = []
        dfs(start)
        return self.res

S = Solution()
adjacentPairs = [[2,1],[3,4],[3,2]]
print(S.restoreArray(adjacentPairs))
adjacentPairs = [[4,-2],[1,4],[-3,1]]
print(S.restoreArray(adjacentPairs))
adjacentPairs = [[100000,-100000]]
print(S.restoreArray(adjacentPairs))

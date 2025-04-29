from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = dict(zip(list(range(n)), list(range(n))))
        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                parent[i] = parent[parent[i-1]]
        res = []
        for u, v in queries:
            res.append(parent[u] == parent[v])
        return res

sol = Solution()
n = 2
nums = [1,3]
maxDiff = 1
queries = [[0,0],[0,1]]
print(sol.pathExistenceQueries(n, nums, maxDiff, queries))
n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]
print(sol.pathExistenceQueries(n, nums, maxDiff, queries))
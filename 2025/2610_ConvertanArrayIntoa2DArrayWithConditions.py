from typing import List
import heapq
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        num_counts = [(k,v) for k,v in counter.items()]
        max_v = max([v for _,v in counter.items()])
        res = [[] for _ in range(max_v)]
        for k, v in counter.items():
            for i in range(v):
                res[i].append(k)
        return res
            
s = Solution()
nums = [1,3,4,1,2,3,1]
print(s.findMatrix(nums))
nums = [1,2,3,4]
print(s.findMatrix(nums))

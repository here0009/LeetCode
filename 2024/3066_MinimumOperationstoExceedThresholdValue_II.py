from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        counts = 0
        while len(nums) > 0:
            min_val = heapq.heappop(nums)
            if min_val >= k:
                break
            if len(nums) == 0:
                break
            s_min_val = heapq.heappop(nums)
            heapq.heappush(nums, min_val * 2 + s_min_val)
            counts += 1
        return counts

s = Solution()
nums = [2,11,10,1,3]
k = 10
print(s.minOperations(nums, k))
nums = [1,1,2,4,9]
k = 20
print(s.minOperations(nums, k))
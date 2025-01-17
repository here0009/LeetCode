from typing import List
from collections import deque


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        def num2lst(num:int):
            """
            6 -> '110' -> [0, 1, 1]
            """
            return [int(i) for  i in bin(num)[2:][::-1]]
        
        def lst2num(lst:List[int]) -> int:
            """
            [0, 1, 1] -> '110' -> 6
            """
            return int(''.join(['1' if i > 0 else '0' for i in lst ])[::-1], 2)
        
        dq = deque([])
        res = len(nums) + 1
        max_length = len(bin(max(nums))) - 2
        sum_lst = [0] * max_length
        for num in nums:
            lst = num2lst(num)
            for i in range(len(lst)):
                sum_lst[i] += lst[i]
            dq.append(num)
            while lst2num(sum_lst) >= k and dq:
                res = min(res, len(dq))
                lst2 = num2lst(dq.popleft())
                for i in range(len(lst2)):
                    sum_lst[i] -= lst2[i]
        return -1 if res == len(nums) +1 else res
                    
s = Solution()
nums = [1,2,3]
k = 2
print(s.minimumSubarrayLength(nums, k))
nums = [2,1,8]
k = 10
print(s.minimumSubarrayLength(nums, k))
nums = [1,2]
k = 0
print(s.minimumSubarrayLength(nums, k))
nums = [1,12,2,5]
k = 43
print(s.minimumSubarrayLength(nums, k))
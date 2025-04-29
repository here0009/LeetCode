from typing import List
from functools import reduce

class Solution: # wrong answer, the val << k may not in max_d_nums, example: # test 3
    def maximumOr(self, nums: List[int], k: int) -> int:
        digits_tuple = [(len(bin(num)) - 2, num) for num in nums]
        max_digits = max([d for d,_ in digits_tuple])
        max_d_nums = [v for d,v in digits_tuple if d == max_digits]
        non_max_d_nums = [v for d,v in digits_tuple if d < max_digits]
        non_max_flag = len(non_max_d_nums) > 0
        if non_max_flag:
            non_max_xor = reduce(lambda x,y: x^y, non_max_d_nums)
        res = 0
        for i,v in enumerate(max_d_nums):
            max_d_nums[i] = v << k
            curr_xor = reduce(lambda x,y: x^y, max_d_nums)
            if non_max_flag:
                res = max(res, curr_xor ^ non_max_xor)
            else:
                res = max(res, curr_xor)
            max_d_nums[i] = v
        return res
    
    
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        all_xor = 0
        same_bits = 0
        for num in nums:
            same_bits |= all_xor & num
            all_xor |= num
        return max([(all_xor ^ num) | same_bits | num << k for num in nums])            

sol = Solution()
# test 1
nums = [12,9]
k = 1
print(sol.maximumOr(nums, k))
# test 2
nums = [8,1,2]
k = 2
print(sol.maximumOr(nums, k))
# test 3
nums = [98,54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,97,13,80,33,69,91,78,19,40]
k = 2
print(sol.maximumOr(nums, k))

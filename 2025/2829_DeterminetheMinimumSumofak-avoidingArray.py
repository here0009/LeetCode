from typing import List

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        avoid_nums = set()
        res_nums = []
        num = 1
        while len(res_nums) < n:
            rmd = k - num
            if num not in avoid_nums:
                res_nums.append(num)
                avoid_nums.add(rmd)
            num += 1
        return sum(res_nums)

sol = Solution()
print(sol.minimumSum(5, 4))
print(sol.minimumSum(2, 6))                

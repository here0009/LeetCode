"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""
from collections import deque
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        # min_val = abs(min(nums))
        # lower += min_val
        # upper += min_val
        # nums = [n+min_val for n in nums]
        # print(lower, upper, nums)
        dq = deque()
        tmp,res = 0,0
        for n in nums:
            tmp += n
            dq.append(n)
            print('outer',tmp,dq)
            if tmp < upper:
                continue
            while dq and tmp >= upper:
                print('inner',tmp,dq)
                tmp -= dq.popleft()
                if tmp >= lower:
                    res += 1
                else:
                    break
        return res
            
S = Solution()
nums = [-2,5,-1]
lower = -2
upper = 2
print(S.countRangeSum(nums, lower, upper))
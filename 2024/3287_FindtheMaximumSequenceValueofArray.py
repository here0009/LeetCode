"""
You are given an integer array nums and a positive integer k.

The value of a sequence seq of size 2 * x is defined as:

(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
Return the maximum value of any 
subsequence
 of nums having size 2 * k.

 
Example 1:

Input: nums = [2,6,7], k = 1

Output: 5

Explanation:

The subsequence [2, 7] has the maximum value of 2 XOR 7 = 5.

Example 2:

Input: nums = [4,2,5,6,7], k = 2

Output: 2

Explanation:

The subsequence [4, 5, 6, 7] has the maximum value of (4 OR 5) XOR (6 OR 7) = 2.

Constraints:

2 <= nums.length <= 400
1 <= nums[i] < 27
1 <= k <= nums.length / 2
"""

from typing import List
from math import inf


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        
        def get_max_min_dp(input_nums:List[int], k:int):
            length = len(input_nums)
            max_dp = input_nums[::1]
            for i in range(k-1):
                tmp = [0]*length
                for j in range(i+1, length):
                    tmp[j] = max([input_nums[j] | max_dp[m] for m in range(i, j)])
                max_dp = tmp
            min_dp = input_nums[::1]
            for i in range(k-1):
                tmp = [inf]*length
                for j in range(i+1, length):
                    tmp[j] = min([input_nums[j] | min_dp[m] for m in range(i, j)])
                min_dp = tmp
            return max_dp, min_dp
        
        length = len(nums)
        max_dp, min_dp = get_max_min_dp(nums, k)
        rev_max_dp, rev_min_dp = get_max_min_dp(nums[::-1], k)

        res = 0
        # rev_max_dp, rev_min_dp = rev_max_dp[::-1], rev_min_dp[::-1]
        print('max_dp', max_dp)
        print('min_dp', min_dp)
        print('rev_max_dp', rev_max_dp)
        print('rev_min_dp', rev_min_dp)
        for i in range(k - 1, length - k + 1):
            for j in range(length - k - i, i, -1)
                res = max(res, max_dp[i]^rev_min_dp[j], min_dp[i]^rev_max_dp[j])
        print(res)
        return res
        



s = Solution()
nums = [2,6,7]
k = 1
print(s.maxValue(nums, k))
nums = [4,2,5,6,7]
k = 2
print(s.maxValue(nums, k))
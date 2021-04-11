"""
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000
"""


from typing import List
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        TLE
        """

        @lru_cache(None)
        def dp(ni, nj, mi):
            if mi == len_m:
                return 0
            return max(nums[ni] * multipliers[mi] + dp(ni + 1, nj, mi + 1), nums[nj] * multipliers[mi] + dp(ni, nj - 1, mi + 1))

        len_m = len(multipliers)
        return dp(0, len(nums) - 1, 0)


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @lru_cache(len(multipliers))
        def dp(ni, nj, mi):
            if mi == len_m:
                return 0
            return max(nums[ni] * multipliers[mi] + dp(ni + 1, nj, mi + 1), nums[nj] * multipliers[mi] + dp(ni, nj - 1, mi + 1))

        len_m = len(multipliers)
        return dp(0, len(nums) - 1, 0)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        TLE
        """
        def dp(ni, nj, mi):
            if (ni, nj, mi) in self.memo:
                return self.memo[(ni, nj, mi)]
            if mi == len_m:
                res = 0
            else:
                res = max(nums[ni] * multipliers[mi] + dp(ni + 1, nj, mi + 1), nums[nj] * multipliers[mi] + dp(ni, nj - 1, mi + 1))
            self.memo[(ni, nj, mi)] = res
            return res

        len_m = len(multipliers)
        self.memo = dict()
        return dp(0, len(nums) - 1, 0)


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @lru_cache(len(multipliers))
        def dp(ni, nj, mi):
            if mi == len_m:
                return 0
            return max(nums[ni] * multipliers[mi] + dp(ni + 1, nj, mi + 1), nums[nj] * multipliers[mi] + dp(ni, nj - 1, mi + 1))

        len_m = len(multipliers)
        return dp(0, len(nums) - 1, 0)




class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @lru_cache(len(multipliers))
        def dp(ni, mi):
            if mi == len_m:
                return 0
            nj = len_n + ni - mi - 1
            return max(nums[ni] * multipliers[mi] + dp(ni + 1, mi + 1), nums[nj] * multipliers[mi] + dp(ni, mi + 1))

        len_n, len_m = len(nums), len(multipliers)
        return dp(0, 0)


# 作者：lin-manjia
# 链接：https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations/solution/xiao-bai-dong-tai-gui-hua-ti-jie-by-lin-q5fi5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        def dp(ni, mi):
            if memo[ni][mi] is not None:
                return memo[ni][mi]
            if mi >= len_m:
                memo[ni][mi] = 0
            else:
                nj = len_n + ni - mi - 1
                memo[ni][mi] = max(nums[ni] * multipliers[mi] + dp(ni + 1, mi + 1), nums[nj] * multipliers[mi] + dp(ni, mi + 1))
            return memo[ni][mi]

        len_n, len_m = len(nums), len(multipliers)
        memo = [[None] * (len_m + 1) for _ in range(len_n + 1)]
        dp(0, 0)
        return memo[0][0]






# 作者：ruiyuanli
# 链接：https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations/solution/er-wei-dong-tai-gui-hua-python3-jie-fa-b-csa9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
S = Solution()
nums = [1,2,3]
multipliers = [3,2,1]
print(S.maximumScore(nums, multipliers))
nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
print(S.maximumScore(nums, multipliers))
"""
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

 

Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7
 

Constraints:

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109
"""


from typing import List
from functools import lru_cache
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        wrong anwer
        """
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == length:
                self.res = min(self.res, abs(curr - goal))
                return
            dfs(idx + 1, curr)
            curr += nums[idx]
            for j in range(idx + 1, length):
                dfs(j, curr)

        nums.sort()
        self.res = abs(sum(nums) - goal)
        length = len(nums)
        dfs(0, 0)
        return self.res

from functools import lru_cache
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        wrong anwer
        """
        # @lru_cache(None)
        def dp(idx):
            if idx == length:
                return 0
            res = target - dp(idx + 1)
            target -= nums[idx]
            for j in range(idx + 1, length):
                res = min(res, abs(target - dp(j)))
            return res

        nums.sort()
        length = len(nums)
        return dp(0)


from functools import lru_cache
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        TLE for test case 5
        """
        def calc(stauts):
            return sum(nums[i] * stauts[i] for i in range(length))

        @lru_cache(None)
        def dp(idx, stauts):
            # print(idx, stauts)
            if idx == length:
                return abs(goal - calc(stauts))
            res = dp(idx + 1, stauts)
            s2 = list(stauts)
            s2[idx] = 1
            s2 = tuple(s2)
            res = min(res, dp(idx + 1, s2))
            for j in range(idx + 1, length):
                res = min(res, dp(j, s2))
            return res

        length = len(nums)
        return dp(0, tuple([0] * length))

# https://leetcode.com/problems/closest-subsequence-sum/discuss/1053522/Python-meet-in-the-middle

from bisect import bisect_left
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        Thoughts: max_len of nums is 40,  half_max_len is 20.
        there are total 2**20. 10**6 of sums.
        so we can split nums to two halves, find all possible sums in each half
        and check the closet sum to goal
        TLE for test case 6
        """
        def gen_sums(lst):
            """
            generate possible sums in lst
            """
            res = set()
            length = len(lst)
            for mask in range(1 << length):
                res.add(sum([lst[j] * bool((1 << j) & mask) for j in range(length)]))
            return res

        nums.sort()  # minimize the cominations
        # print(nums)
        # print(nums[:len(nums)//2])
        # print(nums[len(nums)//2:])
        first_half = gen_sums(nums[:len(nums)//2])
        second_half = list(gen_sums(nums[len(nums)//2:]))
        second_half.sort()
        res = float('inf')
        # print(first_half)
        # print(second_half)
        for half in first_half:
            target = goal - half
            idx = bisect_left(second_half, target)
            if idx > 0:
                res = min(res, abs(target - second_half[idx - 1]))
            if idx < len(second_half):
                res = min(res, abs(target - second_half[idx]))
        return res


from bisect import bisect_left
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        Thoughts: max_len of nums is 40,  half_max_len is 20.
        there are total 2**20. 10**6 of sums.
        so we can split nums to two halves, find all possible sums in each half
        and check the closet sum to goal
        """
        def gen_sums(lst):
            """
            generate possible sums in lst
            """
            res = set([0])
            for v in lst:
                tmp = set([v + p for p in res])
                res |= tmp
            return res

        nums.sort()  # minimize the cominations
        first_half = gen_sums(nums[:len(nums)//2])
        second_half = list(gen_sums(nums[len(nums)//2:]))
        second_half.sort()
        res = float('inf')
        for half in first_half:
            target = goal - half
            idx = bisect_left(second_half, target)
            if idx > 0:
                res = min(res, abs(target - second_half[idx - 1]))
            if idx < len(second_half):
                res = min(res, abs(target - second_half[idx]))
        return res


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        Thoughts: max_len of nums is 40,  half_max_len is 20.
        there are total 2**20. 10**6 of sums.
        so we can split nums to two halves, find all possible sums in each half
        and check the closet sum to goal
        """
        def gen_sums(lst):
            """
            generate possible sums in lst
            """
            res = set([0])
            for v in lst:
                tmp = set([v + p for p in res])
                res |= tmp
            return sorted(list(res))

        nums.sort()  #  try to minimize the cominations
        first_half = gen_sums(nums[:len(nums)//2])
        second_half = gen_sums(nums[len(nums)//2:])
        i, j = 0, len(second_half) - 1
        res = float('inf')
        while i < len(first_half) and j >= 0:
            res = min(res, abs(diff := goal - first_half[i] - second_half[j]))
            if diff > 0:
                i += 1
            elif diff < 0:
                j -= 1
            else:
                break
        return res

S = Solution()
nums = [5,-7,3,5]
goal = 6
print(S.minAbsDifference(nums, goal))
nums = [7,-9,15,-2]
goal = -5
print(S.minAbsDifference(nums, goal))
nums = [1,2,3]
goal = -7
print(S.minAbsDifference(nums, goal))
nums = [-6651,401,-8998,-9269,-9167,7741,-9699]
goal = 30536
print(S.minAbsDifference(nums, goal))
# 输出：
# 30135
# 预期：
# 22394
# Test case 5
nums = [3346,-3402,-9729,7432,2475,6852,5960,-7497,3229,6713,8949,9156,3945,-8686,1528,5022,-9791,-3782,-191,-9820,7720,-6067,-83,6793,340,7793,8742,8067]
goal = -20357
print(S.minAbsDifference(nums, goal))
# Test case 6
nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,-8192,-16384,-32768,-65536,-131072,-262144,-524288]
goal = 1048574
print(S.minAbsDifference(nums, goal))
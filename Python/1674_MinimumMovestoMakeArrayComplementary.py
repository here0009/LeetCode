"""
You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

 

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= limit <= 105
n is even.
"""


from typing import List
from collections import Counter
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        length = len(nums)
        delta = Counter()
        # from min(a,b)+1 to max(a+b)+limit(except a+b), we can reach the target in one step.
        # before min(a,b) and after max(a+b)+limit, we need 2 steps
        for i in range(length//2):
            a, b = nums[i], nums[length-1-i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
        res = float('inf')
        curr = 0
        for key in sorted(delta.keys()):
            curr += delta[key]
            res = min(res, curr)
        return res


from collections import Counter
from bisect import bisect_left
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        length = len(nums)
        half_len = length//2
        sums = Counter()
        min_vals, max_vals = [], []
        for i in range(half_len):
            a, b = nums[i], nums[length-1-i]
            sums[a+b] += 1
            min_vals.append(min(a, b))
            max_vals.append(max(a, b))

        min_vals.sort()
        max_vals.sort()
        res = float('inf')
        for t in sums.keys():
            dec = bisect_left(max_vals, t-limit)
            inc = half_len - bisect_left(min_vals, t)
            res = min(res, half_len + dec + inc - sums[t])
        return res




S = Solution()
nums = [1,2,4,3]
limit = 4
print(S.minMoves(nums, limit))
nums = [1,2,2,1]
limit = 2
print(S.minMoves(nums, limit))
nums = [1,2,1,2]
limit = 2
print(S.minMoves(nums, limit))
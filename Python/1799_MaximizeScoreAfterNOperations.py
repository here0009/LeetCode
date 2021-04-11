"""
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
"""


from typing import List
from math import gcd
from functools import lru_cache
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        use tuple to record status
        """
        @lru_cache(None)
        def calc(idx, status):
            if idx == n:
                return 0
            res = 0
            for i in range(length):
                if status[i] == 0:
                    for j in range(i + 1, length):
                        if status[j] == 0:
                            s2 = tuple(status[:i] + tuple([1]) + status[i + 1: j] + tuple([1]) + status[j + 1:])
                            res = max(res, (idx + 1) * gcd(nums[i], nums[j]) + calc(idx + 1, s2))
            return res

        length = len(nums)
        n = len(nums) // 2
        # target_status = (1 << len(nums)) - 1
        return calc(0, tuple([0] * len(nums)))


from typing import List
from math import gcd
from functools import lru_cache
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        use binary status
        """
        @lru_cache(None)
        def calc(idx, status):
            if idx == n:
                return 0
            res = 0
            for i in range(length):
                if (status >> i) & 1 == 0:
                    for j in range(i + 1, length):
                        if (status >> j) & 1 == 0:
                            s2 = status | (1 << i) | (1 << j)
                            res = max(res, (idx + 1) * gcd(nums[i], nums[j]) + calc(idx + 1, s2))
            return res

        length = len(nums)
        n = len(nums) // 2
        return calc(0, 0)

from typing import List
from math import gcd
from functools import lru_cache
from itertools import combinations
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        use binary status
        """
        @lru_cache(None)
        def calc(idx, status):
            if idx == n:
                return 0
            res = 0
            zeros = [i for i in range(length) if (status >> i) & 1 == 0]
            for i, j in combinations(zeros, 2):
                s2 = status | (1 << i) | (1 << j)
                res = max(res, (idx + 1) * gcd(nums[i], nums[j]) + calc(idx + 1, s2))
            return res

        length = len(nums)
        n = len(nums) // 2
        return calc(0, 0)

S = Solution()
nums = [1,2]
print(S.maxScore(nums))
nums = [3,4,6,8]
print(S.maxScore(nums))
nums = [1,2,3,4,5,6]
print(S.maxScore(nums))
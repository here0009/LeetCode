"""
You are given three positive integers n, index and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. There are no other valid arrays with a larger value at the given index.
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def calc(max_val):
            res = 0
            left_min = max(1, max_val - index)
            right_min = max(1, max_val - (n - 1 - index))
            ones = n - (2 * max_val - left_min - right_min + 1)  # number of 1
            res += ones
            res += (left_min + max_val) * (max_val - left_min + 1) // 2
            res += (right_min + max_val) * (max_val - right_min + 1) // 2
            res -= max_val
            # print(max_val, left_min, right_min, ones, res)
            return res

        left, right = 1, maxSum + 1
        res = 1
        while left < right:
            mid = (left + right) // 2
            # print(left, right)
            if calc(mid) <= maxSum:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid
        return res

S = Solution()
n = 4
index = 2
maxSum = 6
# print(S.maxValue(n, index, maxSum))
# n = 6
# index = 1
# maxSum = 10
# print(S.maxValue(n, index, maxSum))
n = 1
index = 0
maxSum = 24
print(S.maxValue(n, index, maxSum))
# 输出：
# 23
# 预期：
# 24
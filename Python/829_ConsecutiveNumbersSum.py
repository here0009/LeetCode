"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        left, size = 2, 2
        N = (2*left + size - 1)*size/2

# https://leetcode.com/problems/consecutive-numbers-sum/discuss/128985/Python-solution-with-simple-proof   
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        for d in range(1, N+1):
            diff = d * (d - 1)/2
            nd = N - diff
            if nd <= 0:
                break
            if nd % d == 0:
                res += 1
        return res

# https://leetcode.com/problems/consecutive-numbers-sum/discuss/128959/JavaPython-3-5-liners-O(N-0.5)-Math-method-w-explanation-and-analysis.
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res, k = 0, 1
        while N > k*(k-1)/2:
            if (N - (k-1)*k//2) % k == 0:
                res += 1
            k += 1
        return res

S = Solution()
for i in [5,9,15]:
    print(i, S.consecutiveNumbersSum(i))
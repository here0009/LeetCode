"""
Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.
 

Example 1:

Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
Example 2:

Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:

Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
 

Constraints:

1 <= k <= 10^9
"""

import bisect
class Solution:
    def __init__(self):
        self.fibs = [1,1]
        M = 10**9
        while self.fibs[-1] <= M:
            n = self.fibs[-1] + self.fibs[-2]
            self.fibs.append(n)
        # print(self.fibs)

    def findMinFibonacciNumbers(self, k: int) -> int:

        index = bisect.bisect_left(self.fibs, k)
        # print(k, index, self.fibs[index])
        if k <= 0:
            return 0
        if self.fibs[index] == k:
            return 1
        else:
            return 1 + self.findMinFibonacciNumbers(k - self.fibs[index-1])

# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1

S = Solution()
k = 7
print(S.findMinFibonacciNumbers(k))
k = 10
print(S.findMinFibonacciNumbers(k))
k = 19
print(S.findMinFibonacciNumbers(k))
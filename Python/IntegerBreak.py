"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        if the number is larger than 4, it should be breakdown to get a larger multiply,
        try to break the number into 3s, if there is a 2 left, multiply it.
        if there is a 1 left, add the 1 to a 3 and got a 4.
        3*3 > 2*2*2, so never use 2 more than twice.
        """
        if n < 4:
            return n-1
        if n == 4:
            return 4
        m, rmd = divmod(n,3)
        if rmd == 2:
            return 3**m*2
        elif rmd == 0:
            return 3**m
        else:
            return 3**(m-1)*4

s = Solution()
print(s.integerBreak(2))
print(s.integerBreak(10))
print(s.integerBreak(6))
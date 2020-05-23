"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import math
class Solution:
    """
    time limit exceed with input 102, try another method
    """
    def numSquares(self, n: int) -> int:
        cache = {0:0}

        def helper(n):
            if n in cache:
                return cache[n]
            sqrt_n = int(math.sqrt(n))
            if sqrt_n**2 == n:
                cache[n] = 1
                return 1
            half_n = n//2
            res = helper(n - half_n) + helper(half_n)
            for i in range(1,half_n):
                tmp = helper(n-i)+helper(i)
                if tmp < res:
                    cache[n] = tmp
                    res = tmp 

            return res

        return helper(n)


import math
class Solution_1:
    dp = [0]
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        squares = [i**2 for i in range(1,int(math.sqrt(n)+1))]
        # print(squares)
        for i in range(n+1):

            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)

        return dp[n]


import math
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1,int(math.sqrt(n)+1))]
        nums = [n]
        level  = 1
        while nums:
            tmp = set()
            for num in nums:
                for s in squares:
                    if num == s:
                        return level
                    elif num > s:
                        tmp.add(num-s)
            nums = list(tmp)
            level += 1
        return level




s = Solution()
n = 12
print(s.numSquares(n))
n = 13
print(s.numSquares(n))
n = 102
print(s.numSquares(n))
n = 2820
print(s.numSquares(n))

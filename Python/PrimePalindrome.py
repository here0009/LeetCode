"""
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
 

Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""
from math import sqrt
from functools import lru_cache
class Solution:
    def primePalindrome(self, N: int) -> int:
        """
        TLE
        """

        def isPalindrome(n):
            return n == int(str(n)[::-1])

        @lru_cache(None)
        def isPrime(n):
            for i in range(2, int(sqrt(n))+1):
                if isPrime(i):
                    if n % i == 0:
                        return False
            return True

        if N <= 2:
            return 2
        max_num = 2*10**8
        for i in range(N,max_num):
            if isPalindrome(i) and isPrime(i):
                return i
        return None

from math import sqrt
from functools import lru_cache
class Solution:
    def primePalindrome(self, N: int) -> int:
        @lru_cache(None)
        def isPrime(n):
            for i in range(2, int(sqrt(n))+1):
                if isPrime(i):
                    if n % i == 0:
                        return False
            return True




S = Solution()
N = 6
print(S.primePalindrome(N))
# N = 8
# print(S.primePalindrome(N))
# N = 13
# print(S.primePalindrome(N))

# for i in range(10):
#     print(i,S.primePalindrome(i))

N = 9989900
print(S.primePalindrome(N))
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
            if n == 1:
                return False
            for i in range(2, int(sqrt(n))+1):
                if isPrime(i):
                    if n % i == 0:
                        return False
            return True

        def isPalindrome(n):
            return n == int(str(n)[::-1])

        while True:
            if isPalindrome(N) and isPrime(N):
                return N
            N += 1
            length = len(str(N)) # all palindromes with even length can be divided by 11
            if length > 2 and length % 2 == 0:
                N = int('1'+'0'*(length-1) + '1')
        return None

class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True
        if 8 <= N <= 11: return 11
        for x in range(10 ** (len(str(N)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1]) #exclude str(x)[-1], so the length of y is odd, because all palindromes that got even length can be divided by 11.
            if y >= N and isPrime(y): return y


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        ndigits = len(str(N))
        while True:
            for x in self.palindromes(ndigits):
                if x >= N and self.isPrime(x):
                    return x
            ndigits += 1
    def palindromes(self, n):
        if n == 1:
            for i in range(10):
                yield i
        elif n % 2 == 0:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                s = str(i)
                yield int(s + s[::-1])
        else:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                s = str(i)
                for j in range(10):
                    yield int(s + str(j) + s[::-1])
    def isPrime(self, x):
        if x == 1:
            return False
        if x == 2:
            return True
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
        return True
S = Solution()
N = 6
print(S.primePalindrome(N))
N = 8
print(S.primePalindrome(N))
N = 13
print(S.primePalindrome(N))

# for i in range(10):
#     print(i,S.primePalindrome(i))

N = 100000
print(S.primePalindrome(N))

# N = 9989900
# print(S.primePalindrome(N))
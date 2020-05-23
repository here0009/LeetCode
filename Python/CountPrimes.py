"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import math
class Solution_1:
    """
    TLE
    """
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            # if n == 2 or n == 3:
            #     return True
            for i in range(2,int(math.sqrt(n))+2):
                if n % i == 0:
                    return False
            return True

        res = 0
        for i in range(2,n):
            if isPrime(i):
                res += 1
        return res

import math
class Solution_2:
    """
    TLE
    """
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]

        for i in range(3,n):
            j = 0
            break_flag = False

            while j < len(primes) and  primes[j] < int(math.sqrt(i))+2:
                if i % primes[j] == 0:
                    break_flag = True
                    break
                j += 1

            if not break_flag:
                primes.append(i)
        return len(primes)
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [True]*n
        isPrime[1] = False
        isPrime[0] = False
        for i in range(2, int(math.sqrt(n))+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)



class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [1]*n
        isPrime[1] = 0
        isPrime[0] = 0
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)


s = Solution()
n = 10
print(s.countPrimes(n))
n = 1
print(s.countPrimes(n))
n = 2
print(s.countPrimes(n))
n = 3
print(s.countPrimes(n))
n = 999983
print(s.countPrimes(n))
"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
"""
"""
Thoughts:
there are k primer numbers from 1~n, so the number of combinations are k!*(n-k)!
"""
from math import sqrt
class Solution_1:
    def numPrimeArrangements(self, n: int) -> int:
        N = 10**9+7
        isPrime = [True]*(n+1) #record if i is prime
        isPrime[0] = False
        isPrime[1] = False
        primeIndex = 2
        while primeIndex < n+1:
            # print(primeIndex)
            while primeIndex < n+1 and not isPrime[primeIndex]:
                primeIndex += 1
            k = primeIndex**2
            while k < n+1:
                isPrime[k] = False
                k = k+primeIndex
            primeIndex += 1
        # print(isPrime)
            

        primers = sum(isPrime)
        res = 1
        for i in range(1,primers+1):
            res = res*i % N
        for i in range(1, n-primers+1):
            res = res*i % N

        return int(res)

from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        #N = 1E9+7
        N = 10**9 + 7 #it should be int when using it for mod, N = 1E9+7 will get the wrong result
        isPrime = [True]*(n+1) #record if i is prime
        isPrime[0] = False
        isPrime[1] = False
        primeIndex = 2
        while primeIndex*primeIndex <= n:
            if isPrime[primeIndex]:
                for i in range(primeIndex*primeIndex, n+1, primeIndex):
                    isPrime[i] = False
            primeIndex += 1
        primers = sum(isPrime)
        return (factorial(primers)* factorial(n-primers)) % N

s = Solution()
n = 5
print(s.numPrimeArrangements(n))
n = 100
print(s.numPrimeArrangements(n))


s = Solution_1()
n = 5
print(s.numPrimeArrangements(n))
n = 100
print(s.numPrimeArrangements(n))
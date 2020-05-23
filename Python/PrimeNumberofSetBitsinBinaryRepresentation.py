"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""
from math import sqrt
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        global prime_set
        prime_set = set()
        res = []
        for num in range(L, R+1):
            bit_string = "{:b}".format(num)
            test_prime_num = bit_string.count("1")
            if self.isPrime(test_prime_num):
                res.append(test_prime_num)

        # print(res)
        return len(res)

    def isPrime(self, test_num):
        if test_num in prime_set:
            return True
        if test_num == 1:
            return False
        test_range = int(sqrt(test_num))
        for i in range(2,test_range+1):
            if test_num % i == 0:
                return False
        prime_set.add(test_num)
        return True

s = Solution()
print(s.countPrimeSetBits(6, 10))
print(s.countPrimeSetBits(10, 15))


def binomial(n, k, cache={}):
    if k == 0: return 1
    if (n, k) not in cache:
        cache[n, k] = binomial(n-1, k-1) * n // k
    return cache[n, k]


class Solution_1:
    def countPrimeSetBits(self, L, R):
        return self.fast_count(R+1) - self.fast_count(L)
    
    def fast_count(self, N):
        S = bin(N)
        B = [len(S) + ~i for i, b in enumerate(S) if b == '1']
        res = 0
        for p in [2, 3, 5, 7, 11, 13, 17, 19]:
            if B[0] < p: break
            for i in range(min(p+1, len(B))):
                n = B[i]; k = p-i
                if n < k: break
                res += binomial(n, k)
        return res
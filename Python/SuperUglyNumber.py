"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        nums = [1]*n
        len_primes = len(primes)
        pointers = [0]*len_primes
        for i in range(1,n):
            vals = [primes[k]*nums[pointers[k]] for k in range(len_primes)]
            # print('nums',nums)
            # print('pointers',pointers)
            # print('vals',vals)

            nums[i] = min(vals)
            for k in range(len_primes):
                if nums[i] == vals[k]:
                    pointers[k] += 1
        return nums[-1]

s = Solution()
n = 12
primes = [2,7,13,19]
print(s.nthSuperUglyNumber(n,primes))

n = 10
primes = [2]
print(s.nthSuperUglyNumber(n,primes))


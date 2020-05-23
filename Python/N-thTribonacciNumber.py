"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
class Solution:
    def tribonacci(self, n):
        t0,t1,t2 = 0,1,1
        tlist = [t0,t1,t2]
        if n < 3:
            return tlist[n]
        t = 0
        while n-3 >= 0:
            t = t0+t1+t2
            n -= 1
            t0,t1,t2 = t1,t2,t
        return t

s = Solution()
n = 4
print(s.tribonacci(n))
n = 25
print(s.tribonacci(n))
for i in range(4):
    print(i,s.tribonacci(i))
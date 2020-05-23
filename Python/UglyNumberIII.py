"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.

 

Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
 

Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]
"""
from functools import reduce
class Solution_1:
    def nthUglyNumber(self, n, a, b, c):
        """
        TLE, use binary search
        """
        def gcd(m,n):
            while n != 0:
                r = m%n
                m, n = n, r
            return m

        def lcm(m,n):
            return m*n//gcd(m,n)

        lcm_abc = reduce(lcm,[a,b,c])
        commons = {a*b, b*c, a*c, a*b*c}
        batch_number = lcm_abc//a + lcm_abc//b + lcm_abc//c - 9 + len(commons)
        print(commons)
        print(batch_number)
        factor, remain_number = divmod(n, batch_number)
        print(factor, remain_number)
        start_number = factor * lcm_abc
        counts = factor * batch_number
        ia,ib,ic = 1,1,1
        while counts < n:
            tmp_a, tmp_b, tmp_c = ia*a, ib*b, ic*c
            tmp_list = sorted([tmp_a, tmp_b, tmp_c])
            min_i,second_min = tmp_list[0],tmp_list[1]
            if min_i == tmp_a:
                ka = second_min//min_i
                ia += ka
            if min_i == tmp_b:
                kb = second_min//min_i
                ib += kb
            if min_i == tmp_c:
                kc = second_min//min_i
                ic += kc
            counts += max(ka,kb,kc)
        
        return start_number + min_i


from functools import reduce
class Solution:
    def nthUglyNumber(self, n, a, b, c):
        def gcd(m,n):
            while n != 0:
                r = m%n
                m, n = n, r
            return m

        def lcm(m,n):
            return m*n//gcd(m,n)

        def counts(num):
            return num//a + num//b + num//c - num//ab - num//ac - num//bc + num//abc

        lcm_abc = reduce(lcm,[a,b,c])
        ab = lcm(a,b)
        bc = lcm(b,c)
        ac = lcm(a,c)
        abc = lcm(ab,c)
        left = min(a,b,c)
        right = left * n
        while left < right:
            mid = (left + right)//2
            if counts(mid) >= n:
                right = mid
            else:
                left = mid+1 #lower bound
        return left

        

s = Solution()
n = 3
a = 2
b = 3
c = 5
print(s.nthUglyNumber(n,a,b,c))


n = 4
a = 2
b = 3
c = 4
print(s.nthUglyNumber(n,a,b,c))

n = 5
a = 2
b = 11
c = 13
print(s.nthUglyNumber(n,a,b,c))

n = 1000000000
a = 2
b = 217983653
c = 336916467
print(s.nthUglyNumber(n,a,b,c))
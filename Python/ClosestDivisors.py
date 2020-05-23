"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]
 

Constraints:

1 <= num <= 10^9
"""
"""
there is always an even number in num+1 or num+2, so there is always an answer
"""
from math import sqrt
class Solution:
    def closestDivisors(self, num: int):
        def div(n):
            res = [float('inf'), float('inf')]
            k = int(sqrt(n))
            for i in range(k,0,-1):
                if n % i == 0:
                    return [i,n//i]
            return res

        n1,n2 = num+1, num+2
        d1a, d1b = div(n1)
        d2a, d2b = div(n2)
        d1,d2 = abs(d1a-d1b), abs(d2a-d2b)
        if d1 > d2:
            return [d2a, d2b]
        else:
            return [d1a, d1b]


from math import sqrt
class Solution:
    def closestDivisors(self, num: int):
        n1,n2,k = num+1,num+2,int(sqrt(num+2))
        for i in range(k,0,-1):
            if n1 % i == 0:
                return [i, n1//i]
            if n2 % i == 0:
                return [i, n2//i]

S = Solution()
num = 8
print(S.closestDivisors(num))

num = 123
print(S.closestDivisors(num))

num = 999
print(S.closestDivisors(num))

num = 1
print(S.closestDivisors(num))

num = 2
print(S.closestDivisors(num))
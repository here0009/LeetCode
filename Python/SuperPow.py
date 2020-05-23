"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
"""
class Solution:
    def superPow(self, a: int, b) -> int:
        intb = int(''.join([str(s) for s in b]))
        return a**intb % 1337

class Solution:
    def superPow(self, a: int, b) -> int:
        def sp(x,n):
            if n == 0:
                return 1
            half = sp(x,n//2)
            res = half*half
            if n % 2:
                res *= x
            return res % M

        M = 1337
        intb = int(''.join([str(s) for s in b]))
        return sp(a,intb) % M


class Solution:
    def superPow(self, a: int, b) -> int:
        return pow(a,int(''.join(map(str,b))),1337)

S = Solution()
a = 2
b = [3]
print(S.superPow(a,b))
a = 2
b = [1,0]
print(S.superPow(a,b))
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        M = 2147483647
        powerOf2 = {0}
        res = m
        i = 2
        while i <= M :
            powerOf2.add(i)
            i = i*2
        for i in range(m+1, n+1):
            if res in powerOf2:
                return res
            res = res & i
            # print(res,i)
        return res

S = Solution()
print(S.rangeBitwiseAnd(5,7))

print(S.rangeBitwiseAnd(0,1))

print(S.rangeBitwiseAnd(2,4))
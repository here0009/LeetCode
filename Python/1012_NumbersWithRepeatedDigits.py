"""
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

 

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
"""


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        """
        transform N to N+1 and count non-repeated nums that smaller than N+1
        N+1 got K digits
        find all non-repeated nums that less than K digit
        and non-repeated nums that all K digit but smaller than N+1
        """
        def perm(m, n):
            """
            chose n elements out of m elements
            """
            res = 1
            for i in range(n):
                res *= (m -i)
            return res

        nums = list(map(int, str(N+1)))
        res = 0
        K = len(nums)
        for k in range(1, K):
            res += 9*perm(9, k-1) # first digit can not be zero
        seen = set()
        for i, v in enumerate(nums):
            for j in range(1 if i == 0 else 0 , v):  #1st digti can not be 0       
                if j not in seen:
                    res += perm(9-i, K-i-1) #there are i elments before, and K-i-1 elements after
            if v in seen: #there are repeated digits in N, so there are no more nums smaller than N that got non-repeated elements
                break
            seen.add(v)
        return N-res

S = Solution()
print(S.numDupDigitsAtMostN(20))
print(S.numDupDigitsAtMostN(100))
print(S.numDupDigitsAtMostN(1000))
"""
Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
"""
class Solution:
    def queryString(self, S: str, N: int) -> bool:

        for i in range(N,0,-1):
            if bin(i)[2:] not in S:
                return False
        return True

s = Solution()
S = "0110"
N = 3
print(s.queryString(S,N))

S = "0110"
N = 4
print(s.queryString(S,N))

S = bin(25)
N = 5
print(s.queryString(S,N))
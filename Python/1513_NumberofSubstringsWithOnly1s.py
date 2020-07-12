"""
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0
 

Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5
"""


class Solution:
    def numSub(self, s: str) -> int:
        length = len(s)
        dp = [0]*length
        res = 0
        M = 10**9 + 7
        if s[0] == '1':
            dp[0] = 1
        for i in range(1, length):
            dp[i] = (dp[i-1] + 1) * (s[i] == '1') % M
        return sum(dp) % M


class Solution:
    def numSub(self, s):
        print(s.split('0'))
        return sum(len(a) * (len(a) + 1) / 2 for a in s.split('0')) % (10**9 + 7)

S = Solution()
s = "0110111"
print(S.numSub(s))
s = "101"
print(S.numSub(s))
s = "111111"
print(S.numSub(s))
s = "000"
print(S.numSub(s))

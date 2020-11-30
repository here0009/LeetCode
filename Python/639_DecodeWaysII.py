"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded s can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the s: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input s will fit in range [1, 105].
The input s will only contain the character '*' and digits '0' - '9'.
"""


from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(s):
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 9 if s == '*' else 1
            res = dp(s[:1])*dp(s[1:])
            # start2 = s[:2]
            count2 = 0
            if s[:2] == '**':
                count2 = 15 # except 01~10,20
            elif s[0] == '*':
                count2 = 1 + (int(s[1]) <=6)
            elif s[1] == '*':
                if s[0] == '1':
                    count2 = 9
                elif s[0] == '2':
                    count2 = 6
                else:
                    count2 = 0
            else:
                count2 = int(10 <= int(s[:2]) <= 26)
            if len(s) > 2:
                count2 *= dp(s[2:])
            return (res + count2) % M

        M = 10**9+7
        if not s or s[0] == '0':
            return 0
        return dp(s)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        M = 10**9+7
        length = len(s)
        dp = [0]*(length + 1)
        dp[0], dp[1] = 1, 1
        if s[0] == '*':
            dp[1] = 9
        for i in range(2, length+1):
            count1, count2 = 0, 0

            if s[i-1] == '*':
                count1 = 9
            elif s[i-1] != '0':
                count1 = 1

            if s[i-2:i] == '**':
                count2 = 15 # except 01~10,20
            elif s[i-2] == '*':
                count2 = 1 + (int(s[i-1]) <=6)
            elif s[i-1] == '*':
                if s[i-2] == '1':
                    count2 = 9
                elif s[i-2] == '2':
                    count2 = 6
            elif 10 <= int(s[i-2:i]) <= 26:
                count2 = 1
            dp[i] = (count2*dp[i-2] + count1*dp[i-1]) % M
        # print(dp)
        return dp[-1]



class Solution:
    def numDecodings(self, s):
        one = {str(i): 1 for i in range(1, 10)}
        one.update({'*': 9, '0': 0})
        two = {str(i): 1 for i in range(10, 27)}
        two.update({'*' + str(i): 2 if i <= 6 else 1 for i in range(10)})
        two.update({'1*': 9, '2*': 6, '**': 15})
        dp = (1, one.get(s[:1], 0))
        M = 10**9+7
        for i in range(1, len(s)):
            dp = (dp[1], (one.get(s[i]) * dp[1] + two.get(s[i - 1: i + 1], 0) * dp[0]) % M)
        return dp[-1]
# https://leetcode.com/problems/decode-ways-ii/discuss/105274/Python-Straightforward-with-Explanation
class Solution:
    def numDecodings(self, s):
        M = 10**9+7
        e0, e1, e2 = 1, 0, 0 # stand for previous nums ends with all, ends with one and ends with 2
        for c in s:
            if c == '*':
                f0 = e0*9 + e1*9 + e2*6
                f1 = e0 # treat c as 1
                f2 = e0 # treat c as 2
            else:
                f0 = e0*(c != '0') + e1 + e2*(c<='6')
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0%M , f1, f2
        return e0

S = Solution()
# print(S.numDecodings('*'))
# print(S.numDecodings('1*'))
# print(S.numDecodings('*1'))
# print(S.numDecodings('**'))
print(S.numDecodings('*10*1'))
# Output
# 0
# Expected
# 99
# print(S.numDecodings("*********"))
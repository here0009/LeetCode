"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        re_p = ''
        for letter in p:
            if letter == '?':
                re_p += '.'
            elif letter == '*':
                re_p += '.*'
            else:
                re_p += letter
        print(re_p,s)
        return True if re.fullmatch(re_p,s) else False
        
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        re_p = r''
        for letter in p:
            if letter == '?':
                re_p += r'\w'
            elif letter == '*':
                re_p += r'\w*'
            else:
                re_p += letter
        print(re_p,s)
        return True if re.fullmatch(re_p,s) else False



# https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0]*(len(p)+1) for _ in range(len(s)+1)]
        for j in range(1, len(p)+1):
            if p[j - 1] != '*':
                break
            dp[0][j] = 1

        dp[0][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] #or dp[i-1][j-1]
        # for row in dp:
        #     print(row)

        return bool(dp[-1][-1])

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
#         dp[0][0]= True
#         for i in range(1,len(p)+1):
#             if p[i-1]=='*':
#                 dp[0][i] = dp[0][i-1]
#         for i in range(1, len(s)+1):
#             for j in range(1, len(p)+1):
#                 if s[i-1]==p[j-1] or p[j-1]=='?':
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j-1]=='*':
#                     dp[i][j] = dp[i-1][j] | dp[i][j-1]
#         return dp[-1][-1]

# https://leetcode.com/problems/wildcard-matching/discuss/17845/Python-DP-solution
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

S = Solution()
s = "aa"
p = "a"
print(S.isMatch(s,p))
s = "aa"
p = "*"
print(S.isMatch(s,p))
s = "cb"
p = "?a"
print(S.isMatch(s,p))
s = "adceb"
p = "*a*b"
print(S.isMatch(s,p))
s = "acdcb"
p = "a*c?b"
print(S.isMatch(s,p))
s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
print(S.isMatch(s,p))

s = ""
p = "*"
print(S.isMatch(s,p))
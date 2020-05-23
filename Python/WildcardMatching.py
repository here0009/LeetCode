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
        

S = Solution()
# s = "aa"
# p = "a"
# print(S.isMatch(s,p))
# s = "aa"
# p = "*"
# print(S.isMatch(s,p))
# s = "cb"
# p = "?a"
# print(S.isMatch(s,p))
# s = "adceb"
# p = "*a*b"
# print(S.isMatch(s,p))
# s = "acdcb"
# p = "a*c?b"
# print(S.isMatch(s,p))
s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
print(S.isMatch(s,p))
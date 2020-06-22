"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


from collections import deque
class Solution:
    def shortestPalindrome(self, string: str) -> str:
        """
        wrong answer
        """
        res = ''
        dq = deque(list(string))
        while len(dq) > 1:
            if dq[0] == dq[-1]:
                dq.popleft()
                dq.pop()
            else:
                res += dq.pop()
        return res + string

#https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force
class Solution:
    def shortestPalindrome(self, string: str) -> str:
        length = len(string)
        r_string = string[::-1]
        for i in range(length + 1):
            if string.startswith(r_string[i:]):  # r_string[i:] is a palindrome, add r_string[:i] in front of string, so the total string is a palindrome
                return r_string[:i] + string


class Solution:
    def shortestPalindrome(self, g: str) -> str:
        #lps[i] is defined as longest prefix which is also proper suffix, which is pattern[:i+1]
        s = g + '|' + g[::-1]
        lps = [-1] + [0] * len(s)
        l, r = -1, 0
        print('++++++++++')
        print(s)
        while r < len(s):
            while l >= 0 and s[l] != s[r]:
                l = lps[l]
            l, r = l+1, r+1
            lps[r] = l
            print(lps)
        print(lps[-1])
        print(g[lps[-1]:])
        print(g[lps[-1]:][::-1])
        return g[lps[-1]:][::-1] + g


# class Solution:
#     def shortestPalindrome(self, s):
#         def LPS(p):
#             lps = [0] * len(p)
#             l = 0
#             for i in range(1, len(p)):
#                 while l > 0 and p[i] != p[l]:
#                     l = lps[l-1]
#                 if p[i] == p[l]:
#                     l += 1
#                     lps[i] = l
#                 print(lps)
#             return lps

#         print("+++++++++++++++++++++")
#         print(s)
#         lps = LPS(s)
#         i = 0
#         j = len(s)-1
#         while i < j:
#             while i > 0 and s[i] != s[j]:
#                 i = lps[i-1]
#             if s[i] == s[j]:
#                 i += 1
#             j -= 1
#         print(s[(i+j)+1:len(s)][::-1] + s)
#         return s[(i+j)+1:len(s)][::-1] + s


S = Solution()
string = "aacecaaa"
print(S.shortestPalindrome(string))
string = "abcd"
print(S.shortestPalindrome(string))

string = "aabba"
print(S.shortestPalindrome(string))
# Output
# "bbaabba"
# Expected
# "abbaabba"
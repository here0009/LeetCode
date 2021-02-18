"""
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
"""


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        """
        wrong answer
        """
        if s2 < s1:
            return 0
        prefix = ''
        index = 0
        len_e = len(evil)
        while index < n and s1[index] == s2[index]:
            prefix += s1[index]
            index += 1
        if evil in prefix:
            return 0
        res = 1 #for s1 itself
        while index < n:
            res += 26**(n-index-1)*(ord(s2[index])-ord(s1[index]))
            index += 1

        s_index, evil_index = 0,0
        for index in range(n-len_e):
            if evil >= s1[index:index+len_e] and evil <= s2[index:index+len_e]:
                res -= 26**(n-index-1-1)
        return res

# https://leetcode.com/problems/find-all-good-strings/discuss/560841/Python-Digit-DP-%2B-KMP-(Pattern-For-Similar-Questions)
from functools import lru_cache
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def kmp(pattern):
            nxt_pos = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = nxt_pos[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                nxt_pos[i] = j  # patter[i - 1] == pattern[nxt_pos[i - 1] - 1]
            return nxt_pos

        @lru_cache(None)
        def dp(idx, preS1, preS2, e):
            if e == len_evil:
                return 0
            if idx == n:
                return 1
            start = s1[idx] if preS1 else 'a'
            end = s2[idx] if preS2 else 'z'
            res = 0
            for i in range(ord(start), ord(end) + 1):
                ch = chr(i)
                _preS1 = (preS1 and ch == s1[idx])
                _preS2 = (preS2 and ch == s2[idx])
                e2 = e
                while e2 > 0 and evil[e2] != ch:
                    e2 = nxt_pos[e2 - 1]  # patter[e2 - 1] == pattern[next_pos[e2 - 1] - 1], so e2 = nxt_pos[e2 - 1]
                if evil[e2] == ch:
                    e2 += 1
                res += dp(idx + 1, _preS1, _preS2, e2)
            res = res % M
            return res

        len_evil = len(evil)
        M = 10**9 + 7
        nxt_pos = kmp(evil)
        print(nxt_pos)
        return dp(0, True, True, 0)



S = Solution()
n = 2
s1 = "aa"
s2 = "da"
evil = "b"
print(S.findGoodStrings(n,s1,s2,evil))
n = 8
s1 = "leetcode"
s2 = "leetgoes"
evil = "leetleex"
print(S.findGoodStrings(n,s1,s2,evil))
n = 2
s1 = "gx"
s2 = "gz"
evil = "x"
print(S.findGoodStrings(n,s1,s2,evil))
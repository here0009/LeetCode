"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""

import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        @lru_cache(None)
        def dp(i1, r1, i2):
            # print()
            if r1 >= n1:
                return 0
            j1 = s1.find(s2[i2], i1)
            if j1 == -1:
                return dp(0, r1+1, i2)
            else:
                r1 += (j1 == len_s1 - 1)
                j1 = (j1 + 1) % len_s1
                return (i2 == len_s2 - 1) + dp(j1, r1, (i2 + 1) % len_s2)

        len_s1, len_s2 = len(s1), len(s2)
        return dp(0, 0, 0) // n2


from functools import lru_cache
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        @lru_cache(None)
        def dp(i1, r1, i2):
            # print()
            if r1 >= n1:
                return 0
            j1 = s1.find(s2[i2], i1)
            if j1 == -1:
                return dp(0, r1+1, i2)
            else:
                r1 += (j1 == len_s1 - 1)
                j1 = (j1 + 1) % len_s1
                return (i2 == len_s2 - 1) + dp(j1, r1, (i2 + 1) % len_s2)

        len_s1, len_s2 = len(s1), len(s2)
        q, rmd = divmod(n1, n2)
        return dp(0, q, 0) * n2 + dp(0, rmd, 0)

# https://leetcode.com/problems/count-the-repetitions/discuss/372230/Python-don't-look-at-words-look-at-chars-in-two-virtual-repeating-strings-detailed-explanation
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """
        count the repetation of s2 in s1*n1 (R)
        the res is R // n2
        thought s1, s2 as infinite lenght of string
        for a specific combination of index (i, j) for (s1, s2)
        there should be (i - pre_i) / (j - pre_j) = m / n,
        m/n should be a constant
        """
        memo = dict()
        i1, i2 = 0, 0
        len_s1, len_s2 = len(s1), len(s2)
        t1 = len(s1) * n1
        while i1 < t1:
            r1, r2 = i1 % len_s1, i2 % len_s2
            if s1[r1] == s2[r2]:
                if (r1, r2) in memo:
                    pre_i1, pre_i2 = memo[(r1, r2)]
                    gap1, gap2 = i1 - pre_i1, i2 - pre_i2
                    chunks = (t1 - i1) // gap1
                    i1 += chunks * gap1
                    i2 += chunks * gap2
                    if i1 >= t1:
                        break
                else:
                    memo[(r1, r2)] = (i1, i2)
                i2 += 1
            i1 += 1

        # print(memo)
        return i2 //(len_s2 * n2)


S = Solution()
s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2
print(S.getMaxRepetitions(s1, n1, s2, n2))

s1="abcdef"
n1=4
s2="af"
n2=2
print(S.getMaxRepetitions(s1, n1, s2, n2))

s1 = "acb"
n1 = 1
s2 = "acb"
n2 = 1
print(S.getMaxRepetitions(s1, n1, s2, n2))


s1 = "lovelive"
n1 = 100000
s2 = "lovelive"
n2 = 100000
print(S.getMaxRepetitions(s1, n1, s2, n2))


s1 = "aaa"
n1 = 3
s2 ="aa"
n2 = 1
print(S.getMaxRepetitions(s1, n1, s2, n2))
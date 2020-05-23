"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1
 

Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.
"""
from collections import Counter
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        wrong answer
        """
        s_counter = Counter(s)
        res = 0
        for v in s_counter.values():
            res += v % 2
        return res-1

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        wrong answer
        """
        skip = 0
        rev_s = s[::-1]
        len_s = len(s)
        res = float('inf')
        for skip in range(len_s):
            score = skip
            rev_score = len_s - skip
            # print('skip',skip)
            # print(s[skip:])
            # print(rev_s[:-skip])
            for i in range(skip, len_s):
                # print(s[i],rev_s[skip-i])
                if s[i] != rev_s[i-skip]:
                    score += 1
                if s[i] != rev_s[-1-(skip-i)]:
                    rev_score += 1
            # print(score)
            res = min(res, score, rev_score)
        return res

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Thougths: find the longest subsequence of s and rev_s(res), the answer is len_s - res
        """
        rev_s = s[::-1]
        len_s = len(s)
        dp = [[0]*(len_s+1) for _ in range(len_s+1)]
        for i in range(len_s):
            for j in range(len_s):
                if s[i] == rev_s[j]:
                    # print(i,j,s[i])
                    dp[i+1][j+1] = dp[i][j]+1 
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        return len_s-dp[len_s][len_s]

from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i+1,j-1)
            else:
                return min(dp(i,j-1),dp(i+1,j)) +1
        return dp(0,len(s)-1)

S = Solution()

s = "zzazz"
print(S.minInsertions(s))
s = "mbadm"
print(S.minInsertions(s))
s = "leetcode"
print(S.minInsertions(s))
s = "g"
print(S.minInsertions(s))
s = "no"
print(S.minInsertions(s))
s = "zjveiiwvc"
print(S.minInsertions(s))
# Output:
# 4
# Expected:
# 5
s = "ccewnxhytsr"
print(S.minInsertions(s))
# Output:
# 10
# Expected:
# 9
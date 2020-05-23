"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    """
    Thoughts: dp[(index_s,index_t)], represents the nums of subsequence in S that start from index_s that match index_t
    """
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        @lru_cache(None)
        def dp(index_s, index_t):
            res = 0
            if index_s >= len_s or index_t >= len_t:
                return 0
            if index_t == len_t-1:
                return int(s[index_s] == t[index_t])
            target = t[index_t+1]
            for i in pos_dict[target]:
                if i > index_s:
                    res += dp(i,index_t+1)
            # while index_s+1 < len_s:
            #     if s[index_s+1] == target:
            #         res += dp(index_s+1, index_t+1)
            #     index_s += 1
            return res
        
        pos_dict = defaultdict(list)
        for i,v in enumerate(s):
            pos_dict[v].append(i) 
        # for i in pos_dict[t[0]]:
        #     print(i,dp(i,0))     
        return sum(dp(i,0) for i in pos_dict[t[0]])

from collections import defaultdict
from functools import lru_cache
class Solution:
    """
    Thoughts: dp[(index_s,index_t)], represents the nums of subsequence in S that start from index_s that match index_t
    """
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        @lru_cache(None)
        def dp(index_s, index_t):
            res = 0
            if index_s >= len_s or index_t >= len_t:
                return 0
            if index_t == len_t-1:
                return int(s[index_s] == t[index_t])
            target = t[index_t+1]
            for i in pos_dict[target]:
                if i > index_s:
                    res += dp(i,index_t+1)
            # while index_s+1 < len_s:
            #     if s[index_s+1] == target:
            #         res += dp(index_s+1, index_t+1)
            #     index_s += 1
            return res
        
        pos_dict = defaultdict(list)
        for i,v in enumerate(s):
            pos_dict[v].append(i) 
        # for i in pos_dict[t[0]]:
        #     print(i,dp(i,0))     
        return sum(dp(i,0) for i in pos_dict[t[0]])
  

class Solution:
    """
    bottom up, dp[i][j] represents the res of t[:i] alligned with s[:j]
    dp[1][1] equals to t[0] alligned with s[0]
    so dp[0][j] = 1, for t = '' can allign to any s
    dp[i][j] = dp[i][j-1] if t[i] != s[j], its the same value as t[:i] alligned with s[:j-1]
    dp[i][j] = dp[i][j-1] + dp[i-1][j-1] if t[i] == s[j], t[:i]~s[:j-1] + t[:i-1]~s[:j-1]
    """
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(t)+1, len(s)+1
        dp = [[0]*cols for _ in range(rows)]
        for j in range(cols):
            dp[0][j] = 1
        
        for i in range(1,rows):
            for j in range(1, cols):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        # for row in dp:
        #     print(row)
        return dp[-1][-1]

"""
https://leetcode.com/problems/distinct-subsequences/discuss/37322/Python-dp-solutions-(O(m*n)-O(n)-space).
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s)+1, len(t)+1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = 1 # when t is empty, we always have 1
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
        return dp[-1][-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [1 if i == 0 else 0 for i in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                dp[j] = dp[j] + dp[j - 1]*(s[i - 1] == t[j - 1])                
        return dp[m]


import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            count = 0
            if s[i] == t[j]:
                count += dp(i+1, j+1)
            count += dp(i+1, j)
            return count
        return dp(0, 0)

slt = Solution()
S = "rabbbit"
T = "rabbit"
print(slt.numDistinct(S,T))
S = "babgbag"
T = "bag"
print(slt.numDistinct(S,T))

# S ="daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac"
# T = "ceadbaa"
# print(slt.numDistinct(S,T))
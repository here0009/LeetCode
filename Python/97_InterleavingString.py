"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lower-case English letters.
"""


from collections import Counter
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_1, len_2 = len(s1), len(s2)
        if len_1 < len_2:
            s1, s2 = s2, s1
            len_1, len_2 = len_2, len_1
        
        c1 = Counter(s1)
        c2 = Counter(s2)
        c3 = Counter(s3)
        print(c1 + c2)
        if c1 + c2 != c3:
            return False

        extra = len_1 - len_2 - 1
        if extra <= 0:
            return True

from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dfs(i1, i2, i3):
            if i1 >= len_s1:
                return s2[i2:] == s3[i3:]
            if i2 >= len_s2:
                return s1[i1:] == s3[i3:]
            if (s1[i1] == s3[i3] and dfs(i1+1, i2, i3+1)) or (s2[i2] == s3[i3] and dfs(i1, i2+1, i3+1)):
                return True
            return False

        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        return dfs(0, 0, 0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i1, i2 = 0, 0
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        stack, visited = [(0,0)], set((0,0))
        while stack:
            i1, i2 = stack.pop()
            if i1 + i2 == len_s3:
                return True
            if i1 < len_s1 and s1[i1] == s3[i1+i2] and ((i1+1, i2)) not in visited:
                stack.append((i1+1, i2))
                visited.add((i1+1, i2))
            if i2 < len_s2 and s2[i2] == s3[i1+i2] and ((i1, i2+1)) not in visited:
                stack.append((i1, i2+1))
                visited.add((i1, i2+1))
        return False

# https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        R, C, length = len(s1), len(s2), len(s3)
        if R + C != length:
            return False
        dp = [[0]*(C+1) for _ in range(R+1)]
        dp[0][0] = 1
        for i in range(1, R+1):
            dp[i][0] = dp[i-1][0]*(s1[i-1] == s3[i-1])
        for j in range(1, C+1):
            dp[0][j] = dp[0][j-1]*(s2[j-1] == s3[j-1])
        for i in range(1, R+1):
            for j in range(1, C+1):
                dp[i][j] = int(dp[i][j-1]*(s2[j-1] == s3[i+j-1]) or dp[i-1][j]*(s1[i-1] == s3[i+j-1]))
        # for row in dp:
        #     print(row)
        return bool(dp[-1][-1])



S = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(S.isInterleave(s1, s2, s3))
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(S.isInterleave(s1, s2, s3))
s1 = ""
s2 = ""
s3 = ""
print(S.isInterleave(s1, s2, s3))
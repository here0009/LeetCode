"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true
 

Constraints:

0 <= s.length <= 104
0 <= t.length <= 104
s and t consist of lower-case letters, upper-case letters and/or digits.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        TLE
        """
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j 
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] +(s[i-1] != t[j-1]))
        # for row in dp:
        #     print(row)
        return dp[-1][-1] == 1


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        TLE
        """
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        if s == t:
            return False
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] +(s[i-1] != t[j-1]))
            if min(dp[i]) > 1:
                return False
        return dp[-1][-1] == 1


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        if min(m, n) == 0 and s != t:
            return True
        i, j = 0, 0
        flag = False
        while i < m and j < n:
            # print(i,j)
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            else:
                if flag:
                    return False
                flag = True
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
        return flag or abs((m-i)-(n-j)) == 1

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1: # the length difference of s and t larger than 1
            return False
        i, j = 0, 0 #i is the index of s, j is the index of t
        dist = 0 # the distance between s and t
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            else:
                dist += 1
                if dist > 1:
                    return False
                if m > n: # the gap is s[i]
                    i += 1
                elif m < n: # the gap is t[j]
                    j += 1
                else: #the diff value if s[i] != t[j]
                    i += 1
                    j += 1
        dist += abs((m-i)-(n-j)) #check if both i and j are at the ends
        return dist == 1

S = Solution()
s = "ab"
t = "acb"
print(S.isOneEditDistance(s, t))
s = ""
t = ""
print(S.isOneEditDistance(s, t))
s = "a"
t = ""
print(S.isOneEditDistance(s, t))
s = ""
t = "A"
print(S.isOneEditDistance(s, t))
s = "teacher"
t = "acher"
print(S.isOneEditDistance(s, t))
# 输出：
# true
# 预期结果：
# false
s = "a"
t = "ac"
print(S.isOneEditDistance(s, t))
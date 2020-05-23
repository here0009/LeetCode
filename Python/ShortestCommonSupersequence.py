"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        This is superarray, not supersequence, wrong answer
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        length = len(str2)
        len_str2 = len(str2)
        len_str1 = len(str1)
        while length > 0:
            pre_s1 = str1[:length]
            suff_s1 = str1[len_str1-length:]
            pre_s2 = str2[:length]
            suff_s2 = str2[len_str2-length:]
            if pre_s1 == suff_s2:
                return str2+str1[length:]
            if suff_s1 == pre_s2:
                return str1+str2[length:]
            length -= 1
        return str1+str2

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def LCS(str1, str2):
            """
            return the longest common subsequence of str1 and str2
            """
            m, n = len(str1), len(str2)
            dp = [["" for _ in range(n+1) ] for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    if str1[i] == str2[j]:
                        dp[i+1][j+1] = dp[i][j] + str1[i]
                    else:
                        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key = len)
            # print(dp)
            return dp[-1][-1]

        lcs = LCS(str1, str2)
        res = ''
        i = 0
        j = 0
        for letter in lcs:
            while str1[i] != letter:
                res += str1[i]
                i += 1
            while str2[j] != letter:
                res += str2[j]
                j += 1
            res += letter
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]

s = Solution()
str1 = "abac"
str2 = "cab"
print(s.shortestCommonSupersequence(str1, str2))

# str1 = "a"
# str2 = "c"
# print(s.shortestCommonSupersequence(str1, str2))

# str1 = "a"
# str2 = ""
# print(s.shortestCommonSupersequence(str1, str2))

# str1 = ""
# str2 = ""
# print(s.shortestCommonSupersequence(str1, str2))

# str1 = "aaaaaaaa"
# str2 = "aaaaaaaa"
# print(s.shortestCommonSupersequence(str1, str2))

str1 = "bbbaaaba"
str2 = "bbababbb"
output = "bbababbbaaaba"
expected = "bbabaaababb"
print(s.shortestCommonSupersequence(str1, str2))
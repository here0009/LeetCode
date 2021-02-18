"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""


from functools import lru_cache
import re
# Top down
class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Thoughts: 
        min: len(set(s))
        max: len(s)
        """
        @lru_cache(None)
        def dp(i, j):
            # print(i, j)
            if i > j:
                return 0
            res = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j))
            return res

        s = re.sub(r'(.)\1+', r'\1', s)  #remove consetutive digits
        # print(s)
        return dp(0, len(s) - 1)

# Bottom up
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        len_s = len(s)
        dp = [[0] * len_s for _ in range(len_s + 1)]
        for i in range(len_s - 1, -1, -1):
            for j in range(i, len_s):
                if i == j:
                    dp[i][j] = 1
                    continue
                dp[i][j] = 1 + dp[i + 1][j]
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
        for row in dp:
            print(row)
        return dp[0][len_s - 1]

S = Solution()
s = "aaabbb"
print(S.strangePrinter(s))
s = "aba"
print(S.strangePrinter(s))
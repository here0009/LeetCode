"""
Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
"""


from functools import lru_cache
class Solution:
    def checkPartitioning(self, string: str) -> bool:
        @lru_cache(None)
        def isPalindrome(s2):
            print(s2)
            i, j = 0, len(s2) - 1
            while i < j and s2[i] == s2[j]:
                i += 1
                j -= 1
            return i >= j

        len_s = len(string)
        i = 1
        start, end = string[0], string[-1]
        while i < len_s:
            j = len_s
            while i < j and string[i - 1] != start and not isPalindrome(string[:i]):
                i += 1
            while j > i and string[j - 1] != end and not isPalindrome(string[j:]):
                j -= 1
                if i < j and isPalindrome(string[i:j]):
                    return True
            i += 1

        return False


from functools import lru_cache
class Solution:
    def checkPartitioning(self, string: str) -> bool:
        """
        TLE
        """
        @lru_cache(None)
        def isPalindrome(s2):
            i, j = 0, len(s2) - 1
            while i < j and s2[i] == s2[j]:
                # print(i,j)
                i += 1
                j -= 1
            return i >= j

        len_s = len(string)
        i = 1
        # start, end = string[0], string[-1]
        pre = []
        suff = []
        for i in range(1, len_s):
            if isPalindrome(string[:i]):
                pre.append(i)
        for j in range(len_s - 2, 0, -1):
            if isPalindrome(string[j + 1:]):
                suff.append(j)
        # print(pre, suff)
        suff = suff[::-1]
        for i in pre:
            for j in suff:
                if i > j:
                    break
                if isPalindrome(string[i: j + 1]):
                    return True
        return False


from functools import lru_cache
class Solution:
    def checkPartitioning(self, string: str) -> bool:
        @lru_cache(None)
        def dp(s2, k):
            if not s2:
                return False
            if k == 1:
                return s2 == s2[::-1]
            for i in range(1, len(s2)):
                # if dp(s2[:i], 1) and dp(s2[i:], k - 1) will get TLE
                if s2[:i] == s2[:i][::-1] and dp(s2[i:], k - 1):
                    return True
            return False

        return dp(string, 3)


class Solution:
    def checkPartitioning(self, string: str) -> bool:
        len_s = len(string)
        dp = [[False] * len_s for _ in range(len_s)]
        for i in range(len_s):
            dp[i][i] = True
        for i in range(len_s - 2, -1, -1):
            dp[i][i + 1] = string[i] == string[i + 1]
            for j in range(i + 2, len_s):
                dp[i][j] = dp[i + 1][j - 1] and string[i] == string[j]
        # for row in dp:
        #     print(row)
        for i in range(len_s):
            if dp[0][i]:
                for j in range(i + 1, len_s):
                    if dp[i + 1][j] and dp[j + 1][len_s - 1]:
                        return True
        return False

# source：https://leetcode.cn/problems/palindrome-partitioning-iv/solutions/


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        for length in range(1, n):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 1:
                    isPalindrome[start][end] = True
                elif length == 2:
                    isPalindrome[start][end] = s[start] == s[end]
                else:
                    isPalindrome[start][end] = s[start] == s[end] and isPalindrome[start + 1][end - 1]
        for start in range(1, n - 1):
            if not isPalindrome[0][start - 1]:
                continue
            for end in range(start, n - 1):
                if isPalindrome[start][end] and isPalindrome[end + 1][n - 1]:
                    return True
        return False




S = Solution()
string = "abcbdd"
print(S.checkPartitioning(string))
string = "bcbddxy"
print(S.checkPartitioning(string))
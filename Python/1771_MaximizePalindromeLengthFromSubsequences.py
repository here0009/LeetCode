"""
You are given two strings, word1 and word2. You want to construct a string in the following manner:

Choose some non-empty subsequence subsequence1 from word1.
Choose some non-empty subsequence subsequence2 from word2.
Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.

A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

A palindrome is a string that reads the same forward as well as backward.

 

Example 1:

Input: word1 = "cacb", word2 = "cbba"
Output: 5
Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.
Example 2:

Input: word1 = "ab", word2 = "ab"
Output: 3
Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.
Example 3:

Input: word1 = "aa", word2 = "bb"
Output: 0
Explanation: You cannot construct a palindrome from the described method, so return 0.
 

Constraints:

1 <= word1.length, word2.length <= 1000
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word2 = word2[::-1]
        m, n = len(word1), len(word2)
        max_val = 0
        max_index = None
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + int(word1[i - 1] == word2[j - 1]), dp[i - 1][j], dp[i][j - 1])
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
                    max_index = (i, j)
        for row in dp:
            print(row)
        if max_val == 0:
            return 0
        res = max_val * 2 + 1 - int(max_index == (m, n))
        return res


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:

        def calc(word, n):
            len_w = len(word)
            rev_word = word[::-1]
            dp = [[0] * (len_w + 1) for _ in range(len_w + 1)]
            for i in range(1, len_w + 1):
                for j in range(1, len_w + 1):
                    if j < n:
                        dp[i][j] = max(dp[i - 1][j - 1] + int(word[i - 1] == rev_word[j - 1]), dp[i - 1][j], dp[i][j - 1])
                    else:
                        dp[i][j] = max(dp[i - 1][j - 1] + (dp[i - 1][j - 1] != 0) * int(word[i - 1] == rev_word[j - 1]), dp[i - 1][j], dp[i][j - 1])
            for row in dp:
                print(row)
            return dp[-1][-1]

        # res1 = calc(word1)
        # res2 = calc(word2)
        print(word1, word2)
        m, n = len(word1), len(word2)
        res = calc(word1 + word2, n)
        # if res == res1 or res == res2:
        #     return 0
        return res


S = Solution()
word1 = "cacb"
word2 = "cbba"
print(S.longestPalindrome(word1, word2))
word1 = "ab"
word2 = "ab"
print(S.longestPalindrome(word1, word2))
word1 = "aa"
word2 = "bb"
print(S.longestPalindrome(word1, word2))
word1 = "d"
word2 = "ece"
print(S.longestPalindrome(word1, word2))
word1 = "afaaadacb"
word2 = "ca"
print(S.longestPalindrome(word1, word2))
word1 = "ceebeddc"
word2 = "d"
print(S.longestPalindrome(word1, word2))
"""
Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""

from functools import lru_cache
class Solution:
    def countPalindromicSubsequences(self, string: str) -> int:
        Mod = 10**9 + 7
        @lru_cache(None)
        def dp(start, end):
            if start >= end:
                return 0
            res = 0
            for letter in 'abcd':
                i = string.find(letter, start, end)
                j = string.rfind(letter, start, end)
                if i == -1 or j == -1:
                    continue
                if i == j:
                    res += 1
                else:
                    res += dp(i + 1, j) + 2
            return res % Mod
        return dp(0, len(string))

S = Solution()
string = 'bccb'
print(S.countPalindromicSubsequences(string))
string = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
print(S.countPalindromicSubsequences(string))
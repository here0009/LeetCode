"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)
        res = 0
        bonus_one = 0
        for v in s_counter.values():
            if v % 2 == 0:
                res += v
            else:
                bonus_one = 1
                if v > 2:
                    res += v-1
        return res + bonus_one

s = Solution()
k = "abccccdd"
print(s.longestPalindrome(k))
k = "a"
print(s.longestPalindrome(k))
k = "ccc"
print(s.longestPalindrome(k))
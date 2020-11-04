"""
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.
​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.
Example 3:
Input: s = "a", t = "a"
Output: 0
Example 4:

Input: s = "abe", t = "bbc"
Output: 10
 

Constraints:

1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        dp = [[(0,0)]*(len_t+1) for _ in range(len_s+1)] 
        # dp[i][j] = (m, n) means the there are m equal and n got one diff for substrings that ends with s[i-1] and t[j-1] got m 
        res = 0
        for i in range(1, len_s+1):
            for j in range(1, len_t+1):
                zero, one = dp[i-1][j-1]
                if s[i-1] == t[j-1]:
                    zero += 1
                else:
                    one = zero + 1
                    zero = 0
                dp[i][j] = (zero, one)
                res += one
        return res

S = Solution()
s = "aba"
t = "baba"
print(S.countSubstrings(s, t))
s = "ab"
t = "bb"
print(S.countSubstrings(s, t))
s = "a"
t = "a"
print(S.countSubstrings(s, t))
s = "abe"
t = "bbc"
print(S.countSubstrings(s, t))

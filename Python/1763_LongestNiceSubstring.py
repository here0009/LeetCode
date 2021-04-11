"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
Example 4:

Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""


class Solution:
    def longestNiceSubstring(self, string: str) -> str:

        def isValid(sub_str):
            letters = set(sub_str)
            return all((v.isupper() and chr(ord(v) - diff) in letters) or (v.islower() and chr(ord(v) + diff) in letters) for v in sub_str)

        max_len, res = 0, ''
        diff = ord('A') - ord('a')
        length = len(string)
        for i in range(length - 1):
            if length - i <= max_len:
                break
            for j in range(i + 2, length + 1):
                if isValid(string[i: j]) and j - i > max_len:
                    res = string[i: j]
                    max_len = j - i
        return res

S = Solution()
string = "YazaAay"
print(S.longestNiceSubstring(string))
string = "Bb"
print(S.longestNiceSubstring(string))
string = "c"
print(S.longestNiceSubstring(string))
string = "dDzeE"
print(S.longestNiceSubstring(string))
string = "cChH"
print(S.longestNiceSubstring(string))

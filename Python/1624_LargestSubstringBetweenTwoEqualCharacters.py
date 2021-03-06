"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        pos_dict = dict()
        for i, v in enumerate(s):
            if v in pos_dict:
                res = max(res, i - pos_dict[v]-1)
            else:
                pos_dict[v] = i
        return res

S = Solution()
s = "aa"
print(S.maxLengthBetweenEqualCharacters(s))
s = "abca"
print(S.maxLengthBetweenEqualCharacters(s))
s = "cbzxy"
print(S.maxLengthBetweenEqualCharacters(s))
s = "cabbac"
print(S.maxLengthBetweenEqualCharacters(s))
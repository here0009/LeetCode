"""
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
 

Constraints:

1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.
"""
from collections import Counter
class Solution_1:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        print(s_counter)
        print(t_counter)
        t_extra, s_extra, n = 0, 0, 0 # represents extra letters in t, s and unique characters
        for letter in t_counter:
            if letter not in s_counter:
                n += 1
            else:
                if s_counter[letter] >= t_counter[letter]:
                    s_extra += s_counter[letter] - t_counter[letter]
                else:
                    t_extra += t_counter[letter] - s_counter[letter]
        
        return min(t_extra, s_extra) + n + abs(t_extra - s_extra)

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        # print(s_counter)
        # print(t_counter)
        res = 0
        for letter in t_counter:
            if letter not in s_counter:
                res += t_counter[letter]
            else:
                if t_counter[letter] > s_counter[letter]:
                    res += t_counter[letter] - s_counter[letter]
        return res

S = Solution()
s = "bab"
t = "aba"
print(S.minSteps(s,t))
s = "leetcode"
t = "practice"
print(S.minSteps(s,t))
s = "anagram"
t = "mangaar"
print(S.minSteps(s,t))
s = "xxyyzz"
t = "xxyyzz"
print(S.minSteps(s,t))
s = "friend"
t = "family"
print(S.minSteps(s,t))
"""
Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

 

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92
 

Constraints:

0 <= s.length <= 10^4
s contain upper-case English letters only.
"""


from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        M = 10**9 + 7
        letter_index = defaultdict(list)
        for i, v in enumerate(s):
            letter_index[v].append(i)
        res = 0
        len_s = len(s)
        # print(letter_index)
        for lst in letter_index.values():
            lst = [-1] + lst + [len_s]
            # print(lst)
            for i in range(1, len(lst) - 1):
                res += (lst[i] - lst[i - 1]) * (lst[i + 1] - lst[i])
            res = res % M
        return res

S = Solution()
s = "ABC"
print(S.uniqueLetterString(s))
s = "ABA"
print(S.uniqueLetterString(s))
s = "LEETCODE"
print(S.uniqueLetterString(s))
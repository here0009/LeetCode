"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""


class Solution:
    def secondHighest(self, string: str) -> int:
        digits = list(set([int(s) for s in string if s.isdigit()]))
        # print(digits)
        digits.sort()
        return -1 if len(digits) < 2 else digits[-2]

S = Solution()
string = "dfa12321afd"
print(S.secondHighest(string))
string = "abc1111"
print(S.secondHighest(string))

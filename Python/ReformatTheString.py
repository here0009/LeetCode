"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
class Solution:
    def reformat(self, string: str) -> str:
        digits = ''
        letters = ''
        for s in string:
            if s.isdigit():
                digits += s
            else:
                letters += s

        if abs(len(digits)-len(letters)) > 1:
            return ''
        starter,follower = letters,digits
        if len(digits) > len(letters):
            starter,follower = digits,letters
        res = ''
        i_s,i_l,counts = 0,0,0
        length = len(starter) + len(follower)
        while counts < length:
            if counts % 2 == 0:
                res += starter[i_s]
                i_s += 1
            else:
                res += follower[i_l]
                i_l += 1
            counts += 1
        return res

class Solution:
    def reformat(self, string: str) -> str:
        a = [s for s in string if s.isdigit()]
        b = [s for s in string if s.isalpha()]
        if len(a) < len(b):
            a,b = b,a
        if len(a) - len(b) > 1:
            return ''
        res = ''
        for i in range(len(b)):
            res += a[i]
            res += b[i]
        if len(a) > len(b):
            res += a[-1]
        return res


S = Solution()
string = "a0b1c2"
print(S.reformat(string))
string = "leetcode"
print(S.reformat(string))
string = "1229857369"
print(S.reformat(string))
string = "covid2019"
print(S.reformat(string))
string = "ab123"
print(S.reformat(string))

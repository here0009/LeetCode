"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        code_to_letter = dict()

        for i in range(26):
            code = str(i+1)
            if i >= 9:
                code += '#'
            code_to_letter[code[::-1]] = chr(ord('a') + i)
        # print(code_to_letter)
        string = s[::-1]
        index = 0
        res = ''
        while index < len(string):
            if string[index] == '#':
                res += code_to_letter[string[index:index+3]]
                index += 3
            else:
                res += code_to_letter[string[index]]
                index += 1
        return res[::-1]
S = Solution()
s = "10#11#12"
print(S.freqAlphabets(s))

s = "1326#"
print(S.freqAlphabets(s))

s = "25#"
print(S.freqAlphabets(s))

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print(S.freqAlphabets(s))

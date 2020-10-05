"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-word-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        len_w, len_a = len(word), len(abbr)
        while i < len_w and j < len_a:
            # print(word[i], abbr[j], i,j)
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                pre_j = j
                while j < len_a and abbr[j].isdigit():
                    j += 1
                num = int(abbr[pre_j:j])
                if len_w - i < num:
                    return False
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len_w and j == len_a


S = Solution()
word = "internationalization"
abbr = "i12iz4n"
print(S.validWordAbbreviation(word, abbr))
word = "apple"
abbr = "a2e"
print(S.validWordAbbreviation(word, abbr))
word = "internationalization"
abbr = "i5a11o1"
print(S.validWordAbbreviation(word, abbr))
word = "a"
abbr = "01"
print(S.validWordAbbreviation(word, abbr))
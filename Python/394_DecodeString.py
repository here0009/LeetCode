"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, string: str) -> str:
        # print(string)
        res = ''
        left = 0
        p = 0
        i = 0
        tmp_num = ''
        tmp_str = ''
        length = len(string)
        while i < length:
            s = string[i]
            # print(s, i, res, tmp_str, tmp_num)
            if s.isdigit():
                tmp_num += s
            elif s == '[':
                i += 1
                left = i
                p += 1
                while i < len(string) and p != 0:
                    if string[i] == '[':
                        p += 1
                    elif string[i] == ']':
                        p -= 1
                    i += 1
                i -= 1
                tmp_str = self.decodeString(string[left:i])
                if not tmp_num:
                    res += tmp_str
                else:
                    res += int(tmp_num) * tmp_str
                # print(s, i, res, tmp_str, tmp_num)
                tmp_num = ''
                tmp_str = ''
            elif s.isalpha():
                tmp_str = s
                if not tmp_num:
                    res += tmp_str
                else:
                    res += int(tmp_num) * tmp_str
                # print(s, i, res, tmp_str, tmp_num)
                tmp_num = ''
                tmp_str = ''
            i += 1
            
        return res


class Solution:
    def decodeString(self, string: str) -> str:
        # print(string)
        res = ''
        left = 0
        p = 0
        i = 0
        tmp_num = ''
        tmp_str = ''
        length = len(string)
        while i < length:
            s = string[i]
            i += 1
            if s.isdigit():
                tmp_num += s
                continue
            elif s.isalpha():
                tmp_str = s
            elif s == '[':
                left = i
                p += 1
                while i < len(string):
                    if string[i] == '[':
                        p += 1
                    elif string[i] == ']':
                        p -= 1
                    if p == 0:
                        break
                    i += 1
                tmp_str = self.decodeString(string[left:i])
                i += 1
            num = int(tmp_num) if tmp_num else 1
            res += num * tmp_str
            tmp_num = ''
            tmp_str = ''

        return res

S = Solution()
string = "3[a]2[bc]"
print(string, S.decodeString(string))
string = "3[a2[c]]"
print(string, S.decodeString(string))
string = "2[abc]3[cd]ef"
print(string, S.decodeString(string))
string = "abc3[cd]xyz"
print(string, S.decodeString(string))
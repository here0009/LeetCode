"""
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
"""


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # delte 'aaa'
        counts = 0
        pre = None
        repeats = 0
        lower, upper, digits = 0, 0, 0
        for c in password:
            if '0' <= c <= '9':
                digits += 1
            elif 'a' <= c <= 'z':
                lower += 1
            elif 'A' <= c <= 'Z':
                upper += 1
            if c == pre:
                counts += 1
            else:
                repeats += counts//3
                counts = 1
            pre = c
        repeats += counts//3
        extra_valid = sum([lower == 0, upper == 0, digits == 0])
        length = len(password)
        print(repeats, extra_valid, length)
        if length > 20:
            remove = length-20+extra_valid
            if repeats >= remove:
                return repeats
            else:
                return remove
        elif length < 6:
            need = max(6-length, extra_valid)
            if repeats >= need:
                return repeats
            else:
                return need
        else:
            return max(repeats, extra_valid)

S = Solution()
# password = "a"
# print(S.strongPasswordChecker(password))
# password = "aA1"
# print(S.strongPasswordChecker(password))
# password = "1337C0d3"
# print(S.strongPasswordChecker(password))
# password = "aaa111"
# print(S.strongPasswordChecker(password))
password = "bbaaaaaaaaaaaaaaacccccc"
print(S.strongPasswordChecker(password))
# Output
# 7
# Expected
# 8

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
        """
        wrong answer
        """
        # delte 'aaa'
        counts = 0
        pre = None
        repeats = []
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
                if counts >= 3:
                    repeats.append(counts)
                counts = 1
            pre = c
        if counts >= 3:
            repeats.append(counts)
        extra_valid = sum([lower == 0, upper == 0, digits == 0])
        length = len(password)
        repeats.sort(reverse = True)
        print(repeats, extra_valid, length)
        if length > 20:
            # if we remove 1 a from 'aaaaaa', it is still invalid 'aaaaa', 1st try to remove extra length from repeats, then substitue repeats with extra_valid
            remove = length - 20
            rmd_remove = remove
            while repeats and rmd_remove > 0:
                tmp = repeats.pop()
                op = min(tmp - 2, rmd_remove)
                rmd_remove -= op
                tmp -= op
                if tmp >= 3:
                    repeats.append(tmp)
                print(repeats, rmd_remove)
            if repeats:  # remove extra length, still need to remove repeats
                return remove + max(extra_valid, sum(i // 3 for i in repeats))
            else: # no repeats left
                return remove - rmd_remove + max(extra_valid, rmd_remove)
        elif length < 6:
            need = max(6 - length, extra_valid)
            if repeats >= need:
                return repeats
            else:
                return need
        else:
            return max(repeats, extra_valid)

# https://leetcode.com/problems/strong-password-checker/discuss/91008/Simple-Python-solution
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """
        things were complicated when len(password) > 20
        we must do deletion and may be need to do replacement(if repeats >= 3)
        we want to use the deletion operation to reduce the needs for replacement
        it only correlates with the repeats of a letter
        if repeats % 3 == 0, one deletion for one replacement
        elif repeats % 3 == 1, two deletion for one replacement
        else repeats % 3 == 2, 3 deletion for one replacement
        """
        ist = 3
        if any('0' <= c <= '9' for c in password):
            ist -= 1
        if any('a' <= c <= 'z' for c in password):
            ist -= 1
        if any('A' <= c <= 'Z' for c in password):
            ist -= 1
        
        tmp_counts = 0
        pre = None
        replace = 0
        counts_rmd = [0] * 3

        for c in password:
            if c == pre:
                tmp_counts += 1
            else:
                if tmp_counts >= 3:
                    replace += tmp_counts // 3
                    counts_rmd[tmp_counts % 3] += 1
                tmp_counts = 1
            pre = c
        if tmp_counts >= 3:
            replace += tmp_counts // 3
            counts_rmd[tmp_counts % 3] += 1

        # print(replace, counts_rmd, ist)
        length = len(password)
        if length <= 20:
            return max(replace, 6 - length, ist)
        else:
            extra_len = length - 20
            one, two = counts_rmd[0], counts_rmd[1]
            replace -= min(extra_len, one)
            replace -= min(max(0, extra_len - one), two * 2) // 2
            replace -= max(0, extra_len - one - 2 * two) // 3
            return extra_len + max(replace, ist)





S = Solution()
password = "a"
print(S.strongPasswordChecker(password))
password = "aA1"
print(S.strongPasswordChecker(password))
password = "1337C0d3"
print(S.strongPasswordChecker(password))
password = "aaa111"
print(S.strongPasswordChecker(password))
password = "bbaaaaaaaaaaaaaaacccccc"
print(S.strongPasswordChecker(password))
# Output
# 7
# Expected
# 8

"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        A_counts = 0
        LLL_counts = 0
        s = s + '#'*2
        for i in range(len(s)-2):
            if s[i] == 'A':
                A_counts += 1
            if s[i:i+3] == 'LLL':
                LLL_counts += 1
        if A_counts > 1 or LLL_counts >= 1:
            return False
        else:
            return True

S = Solution()
# s = "PPALLP"
# print(S.checkRecord(s))
# s = "PPALLL"
# print(S.checkRecord(s))
# s = "AAAA"
# print(S.checkRecord(s))
# s = "PPALLP"
# print(S.checkRecord(s))
# s = "LLPPPLL"
# print(S.checkRecord(s))
s = "PPALLL"
print(S.checkRecord(s))
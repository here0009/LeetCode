"""
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

 

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        length = len(s1)
        flag = 0
        # print(s1, s2)
        for i in range(length):
            if flag == 0:
                if s1[i] > s2[i]:
                    flag = 1
                elif s1[i] < s2[i]:
                    flag = -1
            if (flag == 1 and s1[i] < s2[i]) or (flag == -1 and s1[i] > s2[i]):
                return False
        return True


from collections import Counter
import string
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter(s2)
        firstBreaks, secondBreaks = True, True
        diff = 0
        for c in string.ascii_lowercase:
            diff += s1_counter[c] - s2_counter[c]
            if diff > 0:
                firstBreaks = False
            elif diff < 0:
                secondBreaks = False
        return firstBreaks or secondBreaks





S = Solution()
s1 = "abc"
s2 = "xya"
print(S.checkIfCanBreak(s1, s2))
s1 = "abe"
s2 = "acd"
print(S.checkIfCanBreak(s1, s2))
s1 = "leetcodee"
s2 = "interview"
print(S.checkIfCanBreak(s1, s2))

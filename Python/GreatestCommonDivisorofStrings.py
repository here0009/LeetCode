"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        len_str1 = m = len(str1)
        len_str2 = n = len(str2)
        res = ''
        while n > 0:
            m, n = n, m%n
        gcd = m

        for i in range(gcd, 0, -1):
            d1, r1 = divmod(len_str1, i)
            d2, r2 = divmod(len_str2, i)
            if r1 != 0 or r2 != 0:
                pass
            rep1, rep2 = str1[:i], str2[:i]
            if rep1 == rep2 and str1 == d1*rep1 and str2 == d2*rep2:
                return rep1

        return res

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        len_str1 = m = len(str1)
        len_str2 = n = len(str2)
        res = ''
        while n > 0:
            m, n = n, m%n
        gcd = m
        rep1, rep2 = str1[:gcd], str2[:gcd]
        if rep1 == rep2 and str1 == len_str1//gcd *rep1 and str2 == len_str2//gcd*rep2:
            return rep1
        return res

s = Solution()
str1 = "ABABAB"
str2 = "ABAB"
print(s.gcdOfStrings(str1, str2))

str1 = "ABCABC"
str2 = "ABC"
print(s.gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(s.gcdOfStrings(str1, str2))

str1 = "A"
str2 = "B"
print(s.gcdOfStrings(str1, str2))

str1 = "A"
str2 = "A"
print(s.gcdOfStrings(str1, str2))
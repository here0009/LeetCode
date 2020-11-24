"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now and the result string is "rgeat" which is s2.
As there is one possible scenario that led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lower-case English letters.
"""


from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if s1 == s2 or s1 == s2[::-1]:
            return True
        c1 = Counter(s1[0])
        c2 = Counter(s2[0])
        for k in range(1, length):
            if c1 == c2:
                print(k)
                print(s1, s2)
                print(s1[:k], s1[k:])
                print(s2[:k], s2[k:])
                if self.isScramble(s1[:k], s2[:k]) and self.isScramble(s1[k:], s2[k:]):
                    return True
            c1[s1[k]] += 1
            c2[s2[k]] += 1
        return False



from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dp(string1, string2):
            # print(string1, string2)
            if string1 == string2:
                return True
            if len(string1) != len(string2) or sorted(string1) != sorted(string2):
                return False
            for i in range(1, len(string1)):
                if (dp(string1[:i], string2[:i]) and dp(string1[i:], string2[i:])) or (dp(string1[:i], string2[-i:]) and dp(string1[i:], string2[:-i])):
                    return True
            return False
        
        return dp(s1, s2)

S = Solution()
s1 = "great"
s2 = "rgeat"
print(S.isScramble(s1, s2))
s1 = "abcde"
s2 = "caebd"
print(S.isScramble(s1, s2))
s1 = "a"
s2 = "a"
print(S.isScramble(s1, s2))
s1 = "a"
s2 = "b"
print(S.isScramble(s1, s2))

s1 ="abcdbdacbdac"
s2 ="bdacabcdbdac"
print(S.isScramble(s1, s2))
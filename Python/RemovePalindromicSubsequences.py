"""
Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "ababa"
Output: 1
Explanation: String is already palindrome
Example 2:

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "". 
Remove palindromic subsequence "a" then "bb".
Example 3:

Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "". 
Remove palindromic subsequence "baab" then "b".
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 1000
s only consists of letters 'a' and 'b'
"""
class Solution:
    """
    wrong answer
    """
    def removePalindromeSub(self, s: str) -> int:
        start, end = 0, len(s)-1
        res = 0
        while start < end:
            print(s[start:end+1])
            if s[start] != s[end]:
                res += 1
            start += 1
            end -= 1
        if start == end and start != 0:
            res += 1
        return res

class Solution:
    """
    subsequence can be inconsecutive, remove all a in the 1st step, then remove all b
    """
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == '')

S = Solution()
s = "ababa"
print(S.removePalindromeSub(s))
s = "abb"
print(S.removePalindromeSub(s))
s = "baabb"
print(S.removePalindromeSub(s))
s = ""
print(S.removePalindromeSub(s))
s = "bbaabaaa"
print(S.removePalindromeSub(s))
# Output
# 3
# Expected
# 2
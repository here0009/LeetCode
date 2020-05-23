"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def realPalindrome(s):
            return s == s[::-1]

        if len(s) == 0 or len(s) == 1:
            return True
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                # print(s[left+1:right+1])
                # print(s[left:right])
                return realPalindrome(s[left+1:right+1]) or realPalindrome(s[left:right])
            else:
                left += 1
                right -=1
        return True
            

s = Solution()
# string = 'aba'
# print(s.validPalindrome(string))
string = "abca"
print(s.validPalindrome(string))
# string = "abc"
# print(s.validPalindrome(string))
# string = "a"
# print(s.validPalindrome(string))
"""
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length <= 1:
            return ''
        mid = length // 2
        lst = list(palindrome)
        for i in range(mid):
            if lst[i] != 'a':
                lst[i] = 'a'
                break
        else:
            lst[-1] = 'b'
        return ''.join(lst)

S = Solution()
palindrome = "abccba"
print(S.breakPalindrome(palindrome))
palindrome = "a"
print(S.breakPalindrome(palindrome))
palindrome = "aa"
print(S.breakPalindrome(palindrome))
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        space_index = s.rfind(' ')
        if space_index == -1:
            return len(s)
        else:
            return len(s)-1-space_index

s = Solution()
print(s.lengthOfLastWord(" a"))
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("World"))
print(s.lengthOfLastWord(" "))
print(s.lengthOfLastWord("a"))
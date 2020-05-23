"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {c:i for i,c in enumerate(s)}
        stack = []
        for i,c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return ''.join(stack)


s = Solution()
text = "bcabc"
print(s.removeDuplicateLetters(text))

s = Solution()
text = "cbacdcbc"
print(s.removeDuplicateLetters(text))
"""
Given a text s that consists of lower case English letters and brackets. 

Reverse the texts in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

 

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"


Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""
class Solution:
    def reverseParentheses(self, text):
        stack = []
        for s in text:
            # if s == '(':
            #     continue
            if s == ')':
                tmp = ''
                while stack[-1] != '(':
                    tmp += stack.pop()[::-1]
                stack.pop()
                stack.append(tmp)
            else:
                stack.append(s)
        return ''.join(stack)

s = Solution()
text = "(abcd)"
print(s.reverseParentheses(text))

text = "(u(love)i)"
print(s.reverseParentheses(text))

text = "(ed(et(oc))el)"
print(s.reverseParentheses(text))

text = "a(bcdefghijkl(mno)p)q"
print(s.reverseParentheses(text))

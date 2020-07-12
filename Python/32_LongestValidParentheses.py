"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, string: str) -> int:
        """
        wrong answer
        """
        stack = []
        res = 0
        pre, curr = 0, 0
        for letter in string:
            if letter == ')':
                if stack:
                    stack.pop()
                    curr += 2
                    res = max(res, curr)
                if not stack:
                    curr += pre
                    res = max(res, curr)
                    curr, pre = 0, curr
                    print(letter, 'curr', curr)
            elif letter == '(':
                stack.append('(')
            print(letter, stack, curr, res)
        return res


class Solution:
    def longestValidParentheses(self, string: str) -> int:
        length = len(string)
        dp = [0]*(length + 1)
        stack = []
        for i,v in enumerate(string):
            if v == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p] + i - p + 1
        return max(dp) 


class Solution:
    def longestValidParentheses(self, string: str) -> int:
        length = len(string)
        left, right = 0, 0
        res = 0
        for letter in string:
            if letter == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2*left)
            elif right > left:
                left, right = 0, 0
        
        left, right = 0, 0
        for letter in string[::-1]:
            if letter == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2*left)
            elif left > right:
                left, right = 0, 0
        return res
            




S = Solution()
string = "(()"
print(S.longestValidParentheses(string))
string = ")()())"
print(S.longestValidParentheses(string))
string = "()(()"
print(S.longestValidParentheses(string))

"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""
class Solution:
    def length(self,string):
            if len(string) == 0:
                return 0
            elif string[0] == '(' :
                if string[1] == ')':
                    return 1+self.length(string[2:])
                elif string[-1] == ')':
                    return 2*self.scoreOfParentheses(string[1:-1])

    def scoreOfParentheses(self, string) -> int:
        left, right = 0,0
        start_index = 0
        res = 0
        for i,v in enumerate(string):
            if v == '(':
                left += 1
            elif v == ')':
                right += 1
            if left == right:
                res += self.length(string[start_index: i+1])
                start_index = i+1
                left, right = 0,0
        return res



s = Solution()
string = '()'
print(s.scoreOfParentheses(string))

string = "(())"
print(s.scoreOfParentheses(string))

string = "()()"
print(s.scoreOfParentheses(string))

string = "(()(()))"
print(s.scoreOfParentheses(string))

string = "(())()"
print(s.scoreOfParentheses(string))

string = "((())())"
print(s.scoreOfParentheses(string))

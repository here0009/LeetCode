"""
Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
 

Example 1:

Input: expression = "!(f)"
Output: true
Example 2:

Input: expression = "|(f,t)"
Output: true
Example 3:

Input: expression = "&(t,f)"
Output: false
Example 4:

Input: expression = "|(&(t,f,t),!(t))"
Output: false
 

Constraints:

1 <= expression.length <= 20000
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.
"""
class Solution:
    def parseBoolExpr(self, expression) -> bool:
        sign_stack = []
        value_stack = []
        for s in expression:
            if s == '&' or s == '|' or s == '!':
                sign_stack.append(s)
            if s == 't':
                value_stack.append(True)
            elif s == 'f':
                value_stack.append(False)
            elif s == '(':
                value_stack.append(s)
            elif s == ')':
                tmp = []
                while value_stack[-1] != '(':
                    tmp.append(value_stack.pop())
                value_stack.pop()
                sign = sign_stack.pop()
                if sign == '&':
                    value_stack.append(all(tmp))
                elif sign == '|':
                    value_stack.append(any(tmp))
                elif sign == '!':
                    value_stack.append(not tmp[0])
        return value_stack[0]

s = Solution()

expression = "!(f)"
print(s.parseBoolExpr(expression))

expression = "|(f,t)"
print(s.parseBoolExpr(expression))

expression = "&(t,f)"
print(s.parseBoolExpr(expression))

expression = "|(&(t,f,t),!(t))"
print(s.parseBoolExpr(expression))

expression = "t"
print(s.parseBoolExpr(expression))
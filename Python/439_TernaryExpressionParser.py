"""
Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Note:

The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
Example 1:

Input: "T?2:3"

Output: "2"

Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: "F?1:T?4:5"

Output: "4"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:

Input: "T?T?F:5:3"

Output: "F"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ternary-expression-parser
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def parseTernary(self, expression: str) -> str:
        """
        treat '?' like '(' and ':' liket ')'
        """
        if len(expression) == 1:
            return expression
        condition = expression[0]
        count = 1
        index = 2
        while index < len(expression):
            if expression[index] == '?':
                count += 1
            elif expression[index] == ':':
                count -= 1
            if count == 0:
                break
            index += 1
        if condition == 'T':
            return self.parseTernary(expression[2:index])
        else:
            return self.parseTernary(expression[index+1:])


class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        index = len(expression) - 1
        while index >= 0:
            if expression[index].isdigit() or expression[index] in {'T', 'F'}:
                stack.append(expression[index])
            elif expression[index] == '?':
                index -= 1
                condition = expression[index]
                T = stack.pop()
                F = stack.pop()
                if condition == 'T':
                    stack.append(T)
                else:
                    stack.append(F)
            index -= 1
            # print(stack)
        return stack[-1]

S = Solution()
expression = "T?2:3"
print(S.parseTernary(expression))
expression = "F?1:T?4:5"
print(S.parseTernary(expression))
expression = "T?T?F:5:3"
print(S.parseTernary(expression))
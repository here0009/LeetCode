"""
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
Example 4:

Input: s = "(((((("
Output: 12
Explanation: Add 12 ')' to balance the string.
Example 5:

Input: s = ")))))))"
Output: 5
Explanation: Add 4 '(' at the beginning of the string and one ')' at the end. The string becomes "(((())))))))".
 

Constraints:

1 <= s.length <= 10^5
s consists of '(' and ')' only.
"""


class Solution:
    def minInsertions(self, string: str) -> int:
        res = 0
        stack = []
        right = 0
        for s in string:
            if s == '(':
                if right > 0:
                    if stack:
                        if right == 1:
                            stack.pop()
                            res += 1
                    else:
                        r,d = divmod(right, 2)
                        res += r + d*2
                    right = 0
                stack.append('(')
            else:
                right += 1
                if right == 2 and stack and stack[-1] == '(':
                    stack.pop()
                    right = 0
        r,d = divmod(right, 2)
        print('r,d',r,d)
        return res + len(stack) * 2 + r + d*2

class Solution:
    def minInsertions(self, string: str) -> int:
        string = string.replace('))',']')
        left = 0
        res = 0
        for s in string:
            if s == '(':
                left += 1
            elif s == ']':
                if left > 0:
                    left -= 1
                else:
                    res += 1
            elif s == ')':
                if left > 0:
                    left -= 1
                    res += 1
                else:
                    res += 2
        return res + left * 2



S = Solution()
string = "(()))"
print(S.minInsertions(string))

string = "())"
print(S.minInsertions(string))

string = "))())("
print(S.minInsertions(string))

string = "(((((("
print(S.minInsertions(string))

string = ")))))))"
print(S.minInsertions(string))





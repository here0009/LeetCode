"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""
from collections import deque
class Solution:
    def checkValidString(self, string: str) -> bool:
        left = []
        stars = []
        for letter in string:
            if letter == '(':
                left.append(letter)
                stars = [] #the stars before '(' can not be used as ')' anymore
            elif letter == '*':
                stars.append(letter)
            elif letter == ')':
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        # print(left)
        # print(stars)
        if left:
            return len(stars) >= len(left)
        return True

S = Solution()
string = "()"
print(S.checkValidString(string))

string ="(*)"
print(S.checkValidString(string))

string ="(*))"
print(S.checkValidString(string))

string = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print(S.checkValidString(string))

string = "((*)(*))((*"
print(S.checkValidString(string))

string = "(*()"
print(S.checkValidString(string))
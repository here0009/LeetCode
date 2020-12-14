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
        # print(string, left)
        # print(string, stars)
        if left:
            return len(stars) >= len(left)
        return True


class Solution:
    def checkValidString(self, string: str) -> bool:
        """
        wrong answer
        """
        left, right, stars = 0, 0, 0
        start = string.find('(')
        right, stars = string[:start].count(')'), string[:start].count('*')
        if right > stars:
            return False
        end = string.rfind(')')
        left, stars = string[end + 1:].count('('), string[end + 1:].count('*')
        if left > stars:
            return False
        # print(start, end, string[start: end + 1])
        left, right, stars = 0, 0, 0
        for v in string[stars: end + 1]:
            if v == ')':
                if left == 0 and stars == 0:
                    return False
                if left > 0:
                    left -= 1
                else:
                    stars -= 1
            elif v == '(':
                left += 1
            else:
                stars += 1
        return left <= stars


class Solution:
    def checkValidString(self, string: str) -> bool:
        while string:
            s2 = ''
            start, end = 0, len(string)
            if string[0] == ')' or string[-1] == '(':
                # print(string)
                return False
            while start < len(string) and string[start: start + 2] == '*)':
                start += 2
            while end >= 2 and string[end - 2: end] == '(*':
                end -= 2
            index = start
            while index < end:  # remove ajacent ()
                if string[index: index + 2] == '()':
                    index += 2
                else:
                    s2 += string[index]
                    index += 1
            while len(s2) > 1 and s2[0] == '(' and s2[-1] == ')':
                s2 = s2[1: -1]
            print(s2)
            if s2 == string:
                break
            string = s2
        print(s2)
        # if '(' in s2 or ')' in s2:
        #     return False
        return True

S = Solution()
# string = "()"
# print(string, '\t', S.checkValidString(string))

# string ="(*)"
# print(string, '\t', S.checkValidString(string))

# string ="(*))"
# print(string, '\t', S.checkValidString(string))

# string = "((*)(*))((*"
# print(string, '\t', S.checkValidString(string))

# string = "(*()"
# print(string, '\t', S.checkValidString(string))
# string = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
# print(string, '\t', S.checkValidString(string))

# string = "(((******))"
# print(string, '\t', S.checkValidString(string))
# Output
# true
# Expected
# false
string = "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"
# Output
# false
# Expected
# true
print(string, '\t', S.checkValidString(string))

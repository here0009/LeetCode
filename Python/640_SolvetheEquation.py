"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        re_x = re.compile(r'(-?\d*)x')
        re_num = re.compile(r'(-?\d+)\+')
        e2 = ''
        for i in range(len(equation)-1):
            e2 += equation[i]
            if equation[i+1] == '-':
                e2 += '+'
        e2 += equation[-1]
        # print(equation, e2)
        left, right = e2.split('=')
        left, right = left + '+', right + '+'
        # print(left, right)
        left_x, left_num = re_x.findall(left), re_num.findall(left)
        right_x, right_num = re_x.findall(right), re_num.findall(right)

        # print(left_x, left_num)
        # print(right_x, right_num)
        x = sum([int(i) if (i and i != '-') else int(i+'1') for i in left_x]) - sum([int(i) if (i and i != '-') else int(i+'1') for i in right_x])
        num = sum([int(i) for i in right_num]) - sum([int(i) for i in left_num])
        # print(x, num)
        if x == 0:
            return "Infinite solutions" if num == 0 else "No solution"
        else:
            num = num/x if num % x != 0 else num//x
            return 'x={}'.format(num)


class Solution:
    def solveEquation(self, E: str) -> str:
        [a,b] = (lambda x: [x.real, x.imag])(eval(E.replace('x','j').replace('=','-(')+')', {'j': 1j}))
        return 'x=' + str(int(-a//b)) if b else 'Infinite solutions' if not a else 'No solution'

import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        re_x = re.compile(r'(-?\d*)x')
        re_num = re.compile(r'(-?\d+)\+')
        e2 = equation.replace('-', '+-')
        left, right = e2.split('=')
        left, right = left + '+', right + '+'
        left_x, left_num = re_x.findall(left), re_num.findall(left)
        right_x, right_num = re_x.findall(right), re_num.findall(right)
        x = sum([int(i) if (i and i != '-') else int(i+'1') for i in left_x]) - sum([int(i) if (i and i != '-') else int(i+'1') for i in right_x])
        num = sum([int(i) for i in right_num]) - sum([int(i) for i in left_num])
        if x == 0:
            return "Infinite solutions" if num == 0 else "No solution"
        else:
            num = num/x if num % x != 0 else num//x
            return 'x={}'.format(num)
import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        s = re.sub(r'([\d]*)(x)', lambda m: '1j' if m.group(0)== 'x' else m.group(0)[:-1] + 'j', equation)
        eq = s.replace('=', '-(') + ')' 

        re = eval(eq)
        if re == 0j:
            return 'Infinite solutions'
        elif re.imag == 0:
            return 'No solution'
        return 'x=' + str(int(-re.real / re.imag))

S = Solution()
equation = "x+5-3+x=6+x-2"
print(S.solveEquation(equation))
equation = "x=x"
print(S.solveEquation(equation))
equation = "2x=x"
print(S.solveEquation(equation))
equation = "2x+3x-6x=x+2"
print(S.solveEquation(equation))
equation = "x=x+2"
print(S.solveEquation(equation))
equation = "-3=-2"
print(S.solveEquation(equation))
equation = "-x=-1"
print(S.solveEquation(equation))
equation = "1+1=x"
print(S.solveEquation(equation))
equation = "99x=99"
print(S.solveEquation(equation))

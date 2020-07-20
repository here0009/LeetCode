"""
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""

# print(int('-2'))
# print(int('+2'))
from math import gcd
from functools import reduce
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def toInt(string):
            if string[0] == '+':
                string = string[1:]
            return int(string)

        def lcm(a,b):
            return a*b//gcd(a,b)

        numerator = []
        denominator = []
        vals = expression.split('/')
        # print(vals)
        numerator.append(toInt(vals[0]))
        length = len(vals)
        for i in range(1, length-1):
            string = vals[i]
            index = 0
            tmp = ''
            while index < len(string):
                if string[index] == '-' or string[index] == '+':
                    denominator.append(toInt(tmp))
                    tmp = string[index]
                else:
                    tmp += string[index]
                index += 1
            numerator.append((toInt(tmp)))
        denominator.append(toInt(vals[length-1]))
        # print(numerator)
        # print(denominator)
        d = reduce(lcm, denominator)
        # print(k)
        n = 0
        for i in range(len(numerator)):
            n += d // denominator[i] * numerator[i]
        k = gcd(n,d)
        n,d = n//k, d//k
        return ('{}/{}').format(n,d)

from math import gcd
from functools import reduce
import re
class Solution:
    def fractionAddition(self, expression):
        ints = map(int, re.findall(r'[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)

from fractions import Fraction as f
import re
class Solution:
    def fractionAddition(self, exp):
        res = sum(map(f, re.findall(r'[+-]?\d+/\d+', exp)))
        return '%s/%s' % (res.numerator, res.denominator)


S = Solution()
expression = "-1/2+1/2"
print(S.fractionAddition(expression))
expression ="-1/2+1/2+1/3"
print(S.fractionAddition(expression))
expression ="1/3-1/2"
print(S.fractionAddition(expression))
expression ="5/3+1/3"
print(S.fractionAddition(expression))

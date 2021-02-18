"""
Given two strings S and T, each of which represents a non-negative rational number, return True if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

In general a rational number can be represented using up to three parts: an integer part, a non-repeating part, and a repeating part. The number will be represented in one of the following three ways:

<IntegerPart> (e.g. 0, 12, 123)
<IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:

1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

 

Example 1:

Input: S = "0.(52)", T = "0.5(25)"
Output: true
Explanation:
Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
Example 2:

Input: S = "0.1666(6)", T = "0.166(66)"
Output: true
Example 3:

Input: S = "0.9(9)", T = "1."
Output: true
Explanation: 
"0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
 

Note:

Each part consists only of digits.
The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
1 <= <IntegerPart>.length <= 4
0 <= <NonRepeatingPart>.length <= 4
1 <= <RepeatingPart>.length <= 4

"""


from fractions import Fraction
class Solution(object):
    def isRationalEqual(self, S, T):
        def convert(S):
            if '.' not in S:
                return Fraction(int(S), 1)
            i = S.index('.')
            ans = Fraction(int(S[:i]), 1)
            S = S[i+1:]
            if '(' not in S:
                if S:
                    ans += Fraction(int(S), 10 ** len(S))
                return ans

            i = S.index('(')
            if i:
                ans += Fraction(int(S[:i]), 10 ** i)
            S = S[i+1:-1]
            j = len(S)
            ans += Fraction(int(S), 10**i * (10**j - 1))
            return ans

        return convert(S) == convert(T)


from math import gcd
class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        """
        Thoughts:
        0.(6) is 6/9
        0.(66) is 66/99
        0.(1) is 1/9
        0.(9) is 9/9 amazing !!
        we just need to convert float to decimal
        """
        def convert(string):
            """
            convert string of float to decimal, n for numerator, d for denominator
            """
            rep_i = len(string)
            rep_n, rep_d, rep_part = 0, 1, ''
            if string[-1] == ')':
                rep_i = string.find('(')
                rep_part = string[rep_i + 1: -1]
                rep_n = int(rep_part)
                rep_d = 10**(len(rep_part)) - 1

            non_rep_part = string[:rep_i]
            # print('part', rep_part, non_rep_part)
            dot_i = non_rep_part.find('.')
            non_rep_d = 1
            if dot_i != -1:
                non_rep_d = 10**(rep_i - dot_i - 1)
            #non_rep_n = int(float(non_rep_part) * non_rep_d) # this may cause error,  
            # 300.0001 * 10**4 = 3000000.9999999995
            non_rep_n = int(''.join(non_rep_part.split('.')))
            # print(non_rep_n, non_rep_d, rep_n, rep_d)
            numerator = non_rep_n * rep_d + rep_n
            denominator = non_rep_d * rep_d
            # print(numerator, denominator)
            k = gcd(numerator, denominator)
            return numerator // k, denominator // k

        s = convert(S)
        t = convert(T)
        # print(s, t)
        return s == t

slt = Solution()
S = "0.(52)"
T = "0.5(25)"
print(slt.isRationalEqual(S, T))
S = "0.1666(6)"
T = "0.166(66)"
print(slt.isRationalEqual(S, T))
S = "0.9(9)"
T = "1."
print(slt.isRationalEqual(S, T))
S = "0.43(9)"
T = "0.43"
print(slt.isRationalEqual(S, T))
S = "300.0001"
T = "300.0000"
print(slt.isRationalEqual(S, T))
S = "1.0"
T = "1"
print(slt.isRationalEqual(S, T))
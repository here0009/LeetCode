"""
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.
"""
from collections import defaultdict
class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        rmd = defaultdict(list)
        for d in digits:
            rmd[d%3].append(d)
        # print(rmd)
        choices = rmd[0]
        rmd[1] = sorted(rmd[1])
        rmd[2] = sorted(rmd[2])
        while True:
            if len(rmd[2])>1 and len(rmd[1])>1:
                choices.extend([rmd[2][-1],rmd[1][-1]])
                rmd[2].pop()
                rmd[1].pop()
            elif len(rmd[2]) >= 3:
                choices.extend(rmd[2][-3:])
                rmd[2] = rmd[2][:-3]
            elif len(rmd[1]) >= 3:
                choices.extend(rmd[1][-3:])
                rmd[1] = rmd[1][:-3]
            elif len(rmd[2])>0 and len(rmd[1])>0:
                choices.extend([rmd[2][-1],rmd[1][-1]])
                rmd[2].pop()
                rmd[1].pop()
            else:
                break
        # print(choices)
        choices = sorted(choices, reverse = True)
        if not choices:
            return ''
        elif choices[0] == 0:
            return '0'
        else:
            return ''.join([str(i) for i in choices])

"""
if a number is multiple of 3, the sum of its digits is multiple of 3
"""
class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        sum_d = sum(digits)
        d1 = sorted([n for n in digits if n%3 == 1])
        d2 = sorted([n for n in digits if n%3 == 2])
        d0 = sorted([n for n in digits if n%3 == 0])
        choices = d0
        if sum_d % 3 == 1: #remove 1 from d1 or 2 from d2
            if len(d1) > 0:
                choices.extend(d1[1:] + d2)
            elif len(d2) > 1:
                choices.extend(d1 + d2[2:])
        elif sum_d % 3 == 2:
            if len(d2) > 0:
                choices.extend(d1 + d2[1:])
            elif len(d1) > 1:
                choices.extend(d1[2:]+d2)
        else:
            choices.extend(d1+d2)
        choices = sorted(choices, reverse = True)
        if not choices:
            return ''
        else:
            return str(int(''.join([str(i) for i in choices])))

S = Solution()
digits = [8,1,9]
print(S.largestMultipleOfThree(digits))

digits = [8,6,7,1,0]
print(S.largestMultipleOfThree(digits))

digits = [1]
print(S.largestMultipleOfThree(digits))

digits = [0,0,0,0,0,0]
print(S.largestMultipleOfThree(digits))

digits = [1,1,1,2]
print(S.largestMultipleOfThree(digits))
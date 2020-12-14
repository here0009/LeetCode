"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""


from typing import List
from math import gcd
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def calc(n1, n2, sign):
            p1, q1 = n1
            p2, q2 = n2
            if sign == '/':
                p3 = p1 * q2
                q3 = p2 * q1
            else:
                q3 = q1 * q2
                if sign == '+':
                    p3 = p1 * q2 + p2 * q1
                elif sign == '-':
                    p3 = p1 * q2 - p2 * q1
                elif sign == '*':
                    p3 = p1 * p2
            k = gcd(p3, q3)
            return p3 // k, q3 // k

        def dfs(index):
            if index == 4:
                return []
            if index == 3:  # the last one
                return [nums2[index]]
            res = []
            next_num = nums2[index + 1]
            for sign in signs:
                n1 = calc(num2[index], nums2[index + 1], sign)
                for 
                res.append()
            
            for sign in signs:
                for n2 in dfs(index + 1):
                    res.append(calc(num, n2, sign))


        signs = '+-*/'
        nums2 = [(num, 1) for num in nums]
        dfs(index)  # use fraction to do the calculation
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, string: str) -> int:
        index = 0
        len_s = len(string)
        signs_set = '+-*/'
        nums = []
        signs = []
        while index < len_s:
            c = string[index]
            index += 1
            if c.isdigit():
                while index < len_s and string[index].isdigit():
                    c += string[index]
                    index += 1
                nums.append(int(c))
                if len(nums) >1 and signs and (signs[-1] == '/' or signs[-1] == '*'):
                    p = nums.pop()
                    q = nums.pop()
                    sign = signs.pop()
                    if sign == '/':
                        num = int(float(q)/p) #round towards 0
                    else:
                        num = p*q
                    nums.append(num)
                if signs and signs[-1] == '-':
                    nums[-1] = -1*nums[-1]
                    signs[-1] = '+'
            elif c in signs_set:
                signs.append(c)
            # print(nums)
            # print(signs)

        return sum(nums)

S = Solution()
# string = "-3-2*2"
# print(S.calculate(string))
                
# string = " 3/2 "
# print(S.calculate(string))

# string = " 3+5 / 2 "
# print(S.calculate(string))

string = "14-3/2"
print(S.calculate(string))
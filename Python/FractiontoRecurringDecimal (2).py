"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:
            res = '-'
        else:
            res = ''
        numerator, denominator = abs(numerator), abs(denominator)
        d,r = divmod(numerator, denominator)
        res += str(d)
        if r == 0:
            return res
        else:
            res += '.'
        res_list = []
        pos_dict = dict()
        index = 0
        cycle_flag = False
        while True:
            pos_dict[r] = index
            d,r2 = divmod(r*10, denominator)
            res_list.append(d)
            if r2 == 0:
                break
            elif r2 in pos_dict:
                cycle_flag = True
                cycle_index = pos_dict[r2]
                break
            r = r2
            index += 1

        if cycle_flag:
            res += ''.join(str(i) for i in res_list[:cycle_index])
            res += '(' + ''.join(str(i) for i in res_list[cycle_index:]) + ')'
        else:
            res += ''.join(str(i) for i in res_list)

        return res
s = Solution()
numerator = 1
denominator = 2
print(s.fractionToDecimal(numerator, denominator))

numerator = 2
denominator = 1
print(s.fractionToDecimal(numerator, denominator))

numerator = 2
denominator = 3
print(s.fractionToDecimal(numerator, denominator))

numerator = 4
denominator = 333
print(s.fractionToDecimal(numerator, denominator))

# numerator = 1
# for i in range(1,40):
#     print( '{}/{} = '.format(numerator,i),s.fractionToDecimal(1,i))

numerator = -50
denominator = 8
print(s.fractionToDecimal(numerator, denominator))
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
import re
class Solution:
    def intToRoman(self, num: int) -> str:
        divisor = 1000
        res = []
        num_list = [int(s) for s in str(num)]

        # print(num_list)

        romans = ['I','II','III','IV','V','VI','VII','VIII','IX']
        weights = ['IVX','XLC','CDM','M']
        weights_index = 0
        pre = weights[0]
        for n in num_list[::-1]:
            if n == 0:
                weights_index += 1
                continue
            r_nums = romans[n-1]
            # print(r_nums)
            if weights_index > 0:
                curr = weights[weights_index]
                for i in range(len(curr)-1,-1,-1):
                    r_nums = r_nums.replace(pre[i],curr[i])
            weights_index += 1
            res.append(r_nums)
        # print(res)
        res_str = ''.join(res[::-1])
        return res_str

s = Solution()
print(s.intToRoman(1994))
print(s.intToRoman(58))
print(s.intToRoman(9))
print(s.intToRoman(3))
print(s.intToRoman(4))
print(s.intToRoman(10))
print(s.intToRoman(900))
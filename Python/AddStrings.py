"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution_1:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str_nums = '0123456789'
        str_to_int = dict()
        int_to_str = dict()
        for i,s in enumerate(str_nums):
            str_to_int[s] = i
            int_to_str[i] = s
        len_num1, len_num2 = len(num1), len(num2)
        leading_zeros = abs(len_num1 - len_num2) * '0'
        length = max(len_num1, len_num2)
        
        if len_num1 > len_num2:
            num2 = leading_zeros + num2
            length = len_num1
        elif len_num2 > len_num1:
            num1 = leading_zeros + num1
            length = len_num2
        else:
            length = len_num1

        res_int = 0
        for i in range(length-1, -1,-1):
            base = 10**(length-1-i)
            res_int += (str_to_int[num1[i]]+str_to_int[num2[i]]) * base

        if res_int == 0:
            return '0'

        res_str = ''
        while res_int > 0:
            res_str += int_to_str[res_int%10]
            res_int =  res_int//10
        return res_str[::-1]

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        Thoughts: although we can not use built in str to int, we can use built in int to str
        """
        str_nums = '0123456789'
        str_to_int = dict()
        for i,s in enumerate(str_nums):
            str_to_int[s] = i

        n1, n2 = 0, 0
        for s in num1:
            n1 = (n1*10) + str_to_int[s]
        for s in num2:
            n2 = (n2*10) + str_to_int[s]
        return str(n1+n2)

s = Solution()
print(s.addStrings('123', '345'))
print(s.addStrings('1230045', '345'))
print(s.addStrings('1230045', '3450000000'))
print(s.addStrings('0', '0'))
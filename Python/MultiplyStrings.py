"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def ctoi(c):
            return ord(c)-ord('0')
        
        if num1 == '0' or num2 == '0':
            return '0'
        num1_list = [ctoi(c) for c in list(num1)][::-1]
        num2_list = [ctoi(c) for c in list(num2)][::-1]
        res_list = [0]*(len(num1_list)+len(num2_list)+1)
        for i in range(len(num1_list)):
            for j in range(len(num2_list)):
                tmp = num1_list[i] * num2_list[j]
                carrier, rmd = divmod(tmp, 10)
                res_list[i+j] += rmd
                res_list[i+j+1] += carrier
        for i in range(len(res_list)):
            if res_list[i] >= 10:
                carrier, rmd = divmod(res_list[i],10)
                res_list[i] = rmd
                res_list[i+1] += carrier
        # print(res_list)
        res_list = res_list[::-1]
        tag = 0
        while res_list[tag] == 0:
            tag += 1
        res_list = res_list[tag:]
        # print(res_list)
        res = ''.join([str(i) for i in res_list])
        return res

s = Solution()
num1 = '123'
num2 = '456'
print(s.multiply(num1,num2))

num1 = '2'
num2 = '3'
print(s.multiply(num1,num2))


num1 = '0'
num2 = '0'
print(s.multiply(num1,num2))
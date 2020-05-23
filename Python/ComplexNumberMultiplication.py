"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""
import pysnooper


class Solution:
    @pysnooper.snoop('./pysnooper.log')
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def compplexNumParser(strings):
            real,img = strings.split('+')
            real = int(real)
            img = int(img[:-1])
            return real,img

        a_real, a_img = compplexNumParser(a)
        b_real, b_img = compplexNumParser(b)
        # print(a_real, a_img)
        # print(b_real, b_img)
        res_real = a_real * b_real - a_img * b_img
        res_img = a_real * b_img + b_real * a_img
        res = '{}+{}i'.format(res_real,res_img)
        return res

s = Solution()
a = "1+1i"
b = "1+1i"
print(s.complexNumberMultiply(a,b))

a = "1+-1i"
b = "1+-1i"
print(s.complexNumberMultiply(a,b))
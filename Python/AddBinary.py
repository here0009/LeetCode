"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carrier = 0
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a,b = b, a
            len_a,len_b = len_b,len_a
        a = a[::-1]
        b = b[::-1]
        res = ''
        index = 0
        while index < len_a:
            if index < len_b:
                tmp = carrier + int(a[index]) + int(b[index])
            else:
                tmp = carrier + int(a[index])
            if tmp < 2:
                res += str(tmp)
                carrier = 0
            else:
                res += str(tmp - 2)
                carrier = 1
            index += 1

        if carrier == 1:
            res += '1'
        return res[::-1]

s = Solution()
a = "11"
b = "1"
print(s.addBinary(a,b))

a = "1010"
b = "1011"
print(s.addBinary(a,b))

a = "1"
b = "111"
print(s.addBinary(a,b))

a = "1111"
b = "1111"
print(s.addBinary(a,b))
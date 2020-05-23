"""
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
 

Note:

0 <= N <= 10^9
"""
class Solution_1:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        res = []
        while N:
            # print(N)
            if N % 2 == 1:
                res.append(1)
                N -= 1
            else:
                res.append(0)
            N = N // -2
        res = ''.join([str(i) for i in res])
        return res[::-1]

class Solution:
    def baseNeg2(self, N):
"""
explanition from https://pyblog.in/programming/bitwise-operators-in-python/
Two’s Representation of Negative numbers
Negative numbers are written with a leading one instead of a leading zero. So if you are using only 8 bits for your twos-complement numbers, then you treat patterns from “00000000” to “01111111” as the whole numbers from 0 to 127, and reserve “1xxxxxxx” for writing negative numbers.

Using only 8 bits for twos-compliment negative numbers can be represented as:

-x can be represented as the complement of the bit pattern for (x-1)
So -2 is the ~(2-1) == ~(1) == “11111101”
Python doesn’t use 8-bit numbers. It USED to use however many bits were native to your machine, but since that was non-portable, it has recently switched to using an INFINITE number of bits. Thus the number -5 is treated by bitwise operators as if it were written: “…1111111111111111111011”.
"""
        if N == 0:
            return '0'
        res = []
        while N:
            print(bin(N),"=====",N)
            res.append(N & 1)
            N = -(N >> 1)
        res = ''.join([str(i) for i in res])
        return res[::-1]


s = Solution()
for i in range(10):
    print("=====",i)
    print(s.baseNeg2(i))
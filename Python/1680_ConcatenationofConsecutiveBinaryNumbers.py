"""
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        string = ''
        M = 10**9 + 7
        for i in range(1, n+1):
            string += bin(i)[2:]
        return int(string, 2) % M


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num, length = 0, 0
        M = 10**9 + 7
        for i in range(1, n + 1):
            if i == i & -i:
                length += 1
            num = ((num << length) | i) % M
            # print(i, length, num)
        return num

S = Solution()
print(S.concatenatedBinary(1))
print(S.concatenatedBinary(3))
print(S.concatenatedBinary(12))
# for i in range(15):
#     print(i, i & -i, bin(i), bin(i & -i))
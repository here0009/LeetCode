"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        str_a, str_b, str_c = bin(a)[2:],bin(b)[2:],bin(c)[2:]

        length = max(len(str_a),len(str_c), len(str_b))
        str_a = (length-len(str_a))*'0'+str_a
        str_b = (length-len(str_b))*'0'+str_b
        str_c = (length-len(str_c))*'0'+str_c
        res = 0
        # print(str_a,str_b,str_c)
        for i in range(length):
            if int(str_c[i]) != int(str_a[i]) | int(str_b[i]):
                if str_c[i] == '1':
                    res += 1
                else:
                    res += sum([str_a[i] == '1', str_b[i] == '1'])
        return res


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a | b != c:
            if c & 1  and a & 1 == 0 and b & 1 == 0: # a&1 == 0 or b&1 == 0, change one of them to 1
                res += 1
            if c & 1 == 0:
                if a & 1:
                    res += 1
                if b & 1 :
                    res += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return res


S = Solution()


a = 2
b = 6
c = 5
print(S.minFlips(a,b,c))

a = 4
b = 2
c = 7
print(S.minFlips(a,b,c))

a = 1
b = 2
c = 3
print(S.minFlips(a,b,c))

print(1&1)
print(4&1)
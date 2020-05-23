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
# from copy import deepcopy
class Solution:
    def baseNeg2(self, N: int) -> str:
        # print(N, bin(N))
        base_2 = [int(b )for b in  bin(N)[2:][::-1]]
        # base_2.append(0) #one more digit
        # print(base_2)
        carrier = 0
        res = []
        for i in range(len(base_2)):
            # print(i, base_2[i])
            carrier,b = divmod(base_2[i]+carrier,2)
            res.append(b)
            if i%2 == 1 and b==1: #odd
                carrier = 1
            else:
                carrier = 0

        if carrier:
            res.append(1)

            if len(base_2) % 2 == 1: #odd
                res.append(1)

        # print(base_2)
        res = ''.join([str(i) for i in res[::-1]])
        return res

class Solution_1:
    def baseNeg2(self, N: int) -> str:
        """
        Thoughts: convert to base4, then convert to base -2
        still not possible
        """
        if N == 0:
            return 0
        base_4 = ''
        while N > 0:
            r = N % 4
            base_4 += str(r)
            N = N // 4
        base_4 = base_4[::-1]
        print(base_4)
        dict_4_to_m2 = {'0':'0','1':'100','2':'110','3':'111'}
        res = ''
        for b in base_4:
            res += dict_4_to_m2[b]
        return res

s = Solution()
for i in range(7):
    print('=====',i)
    print(s.baseNeg2(i))
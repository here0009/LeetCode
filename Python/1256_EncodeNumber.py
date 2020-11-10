"""
Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:



 

Example 1:

Input: num = 23
Output: "1000"
Example 2:

Input: num = 107
Output: "101100"
 

Constraints:

0 <= num <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/encode-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def decode(self, string):
        """
        num = 2**(len(stirng)-1) + int(string, 2)
        """
        return 2**(len(string)) - 1 + int(string, 2)

    def encode(self, num):
        if num == 0:
            return ''
        length = 0
        while 2**length-1 <= num:
            length += 1
        length -= 1
        # print('num', num, bin(num-2**length+1))
        rmd = bin(num-2**length+1)[2:]
        # print(num, length, rmd)
        return (length-len(rmd))*'0' + rmd


from math import log
class Solution:
    def decode(self, string):
        """
        num = 2**(len(stirng)-1) + int(string, 2)
        """
        return 2**(len(string)) - 1 + int(string, 2)

    def encode(self, num):
        if num == 0:
            return ''
        length = int(log(num+1, 2))
        rmd = bin(num-2**length+1)[2:]
        return (length-len(rmd))*'0' + rmd


class Solution:
    def encode(self, num):
        return bin(num+1)[3:]

S = Solution()
# print(S.decode('1000'))
# print(S.decode('101100'))
print(S.encode(23))
print(S.encode(107))
for i in range(10):
    print(i, S.encode(i))

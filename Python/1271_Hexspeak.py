"""
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

 

Example 1:

Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.
Example 2:

Input: num = "3"
Output: "ERROR"
 

Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hexspeak
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_dict = dict()
        hex_dict[0] = 'O'
        hex_dict[1] = 'I'
        for i in range(6):
            hex_dict[10+i] = chr(ord('A')+i)
        # print(hex_dict)
        num = int(num)
        res = ''
        while num:
            num, rmd = divmod(num, 16)
            if rmd not in hex_dict:
                return 'ERROR'
            res += hex_dict[rmd]
        return res[::-1]

S = Solution()
num = "257"
print(S.toHexspeak(num))
num = "3"
print(S.toHexspeak(num))
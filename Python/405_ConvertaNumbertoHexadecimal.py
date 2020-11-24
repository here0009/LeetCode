"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = (1 << 32) + num
        res = ''
        hex_dict = dict()
        for i in range(10):
            hex_dict[i] = str(i)
        for i in range(6):
            hex_dict[10+i] = chr(ord('a')+i)
        while num > 0:
            num, rmd = divmod(num, 16)
            res += hex_dict[rmd]
        return res[::-1]

S = Solution()
print(S.toHex(26))
print(S.toHex(-1))
print(S.toHex(-2))

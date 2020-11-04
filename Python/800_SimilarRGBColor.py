"""
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:
Input: color = "#09f166"
Output: "#11ee66"
Explanation:  
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.
Note:

color is a string of length 7.
color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
Any answer which has the same (highest) similarity as the best answer will be accepted.
All inputs and outputs should use lowercase letters, and the output is 7 characters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/similar-rgb-color
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from itertools import product
class Solution:
    def similarRGB(self, color: str) -> str:
        def hexMinus(a, b):
            return 16*(hextoInt(a[0]) - hextoInt(b[0])) + hextoInt(a[1]) - hextoInt(b[1])

        def hextoInt(i):
            if i.isdigit():
                return int(i)
            else:
                return int(ord(i) - ord('a')) + 10

        def inttoHex(i):
            if 0 <= i <= 9:
                return str(i)
            if i > 9:
                return chr(ord('a')+i-10)

        def inRange(i):
            if not i:
                return False
            if i.isdigit():
                return '0' <= i <= '9'
            else:
                return 'a' <= i <= 'f'

        diff = float('inf')
        res = None
        R, G, B = color[1:3], color[3:5], color[5:7]
        r, g, b = hextoInt(R[0]), hextoInt(G[0]), hextoInt(B[0])
        # print(r,g,b,R,G,B)
        # for lst in product([-1, 0, 1], repeat=3):
        #     print(lst)

        for ir,ig,ib in product([-1, 0, 1], repeat=3):
            nr = inttoHex(r+ir)
            ng = inttoHex(g+ig)
            nb = inttoHex(b+ib)
            if inRange(nr) and inRange(ng) and inRange(nb):
                tmp = hexMinus(nr*2, R)**2 + hexMinus(ng*2, G)**2 + hexMinus(nb*2, B)**2
                # print(diff, tmp, '#{}{}{}'.format(nr*2, ng*2, nb*2))
                if tmp < diff:
                    diff = tmp
                    res = '#{}{}{}'.format(nr*2, ng*2, nb*2)
        return res




S = Solution()
# print(S.similarRGB("#09f166"))
# 输入：
# "#71c986"
# 输出：
# "#66bb77"
# 预期结果：
# "#77cc88"
print(S.similarRGB("#71c986"))

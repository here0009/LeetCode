"""
编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。

示例:

输入: 25
输出: 9
解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
提示：

n <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-2s-in-range-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        """
        digit by digit
        e.g. 5721
        power  t    q      d    r
        0    5721   572    1    0
        1    572    57     2    1
        2    57     5      7    21
        3    5      0      5    721
        4    0    
        """
        res = 0
        q, r = n, 0
        power = 0
        while True:
            t, r = divmod(n, 10**power)
            if t == 0:
                break
            q, d = divmod(t, 10)
            # print(power, t, q, d, r, res)
            if d > 2:
                res += (q + 1) * 10**(power)
            elif d == 2:
                res += q * 10**(power) + r + 1
            else:
                res += q * 10**(power)
            
            power += 1
        return res

S = Solution()
print(S.numberOf2sInRange(25))

print(S.numberOf2sInRange(57213))
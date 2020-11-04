"""
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. For example: "123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x < n) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ip-to-cidr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 作者：Tes
# 链接：https://leetcode-cn.com/problems/ip-to-cidr/solution/python350ms-zhuan-huan-er-jin-zhi-chu-li-fang-fa-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


'''
每个数值最右边连续0的个数决定了下一个可能的跨度
最右边剩余i个0，跨度就可以是1<<0, 1<<1 ..... 1<<i
每次都选择不会超过目标值的最大跨度即可
'''
# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/ip-to-cidr/solution/python-ji-bai-100yong-hu-by-hao-shou-bu-juan-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution_1:

    def getZeroNum(self, num):
        i = 0
        while ((1<<i) & num) == 0:
            i += 1
        return i

    def getNum(self, ip: str) -> int:
        l = ip.split('.')
        res = 0
        for i in range(4):
            res += int(l[i]) * 256**(3-i)
        return res

    def getString(self, num: int, mask_bits: int) -> str:
        return '{}.{}.{}.{}/{}'.format(num//(256**3), (num%(256**3)) // (256**2), (num%(256**2)) // (256**1), num%256, mask_bits)

    def ipToCIDR(self, ip: str, n: int):
        val = self.getNum(ip)
        target = val + n

        ans = []
        while val < target:
            zero_cnt = self.getZeroNum(val)

            while (val + (1 << zero_cnt)) > target:
                zero_cnt -= 1

            ans.append(self.getString(val, 32 - zero_cnt))
            val += (1 << zero_cnt)

        return ans


class Solution:
    def ipToCIDR(self, ip: str, n: int):
        def rightZero(num):
            if num == 0:
                return 0
            i = 0
            while ((1 << i) & num) == 0:
                i += 1
            return i

        def iptoInt(ip):
            res = 0
            lst = [int(i) for i in ip.split('.')]
            for i, v in enumerate(lst):
                res += 256**(3-i)*v
            return res

        def InttoIp(num, mask):
            res = []
            for i in range(4):
                res.append((num >> (3-i)*8) % 256)
            return '.'.join([str(i) for i in res]) + '/' + str(mask)

        int_ip = iptoInt(ip)
        target = int_ip + n
        res = []
        while int_ip < target:
            zeros = rightZero(int_ip)
            while (int_ip + (1 << zeros)) > target:
                zeros -= 1
            res.append(InttoIp(int_ip, 32-zeros))
            int_ip += (1 << zeros)
        return res


S = Solution()
ip = "255.0.0.7"
n = 10
print(S.ipToCIDR(ip, n))
ip = "0.0.0.0"
n = 1
print(S.ipToCIDR(ip, n))
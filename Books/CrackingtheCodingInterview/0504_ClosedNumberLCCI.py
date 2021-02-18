"""
下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

示例1:

 输入：num = 2（或者0b10）
 输出：[4, 1] 或者（[0b100, 0b1]）
示例2:

 输入：num = 1
 输出：[2, -1]
提示:

num的范围在[1, 2147483647]之间；
如果找不到前一个或者后一个满足条件的正数，那么输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closed-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""




# 作者：toulondu
# 链接：https://leetcode-cn.com/problems/closed-number-lcci/solution/dai-ma-bu-zha-di-xiao-guo-huan-bu-cuo-by-toulondu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        bigger_one = lower_one = bin(num)[2:]

        # 对于找较大值，即是找到二进制中最后一个01，改为10，再把右边所有的0左移
        bigger_one = '0'+bigger_one
        last01 = bigger_one.rfind('01')
        count0 = bigger_one.count('0',last01+1)
        len1 = len(bigger_one) - last01 - 2 - count0
        bigger_one = bigger_one[0:last01]+'10'+ '0'*count0 + '1'*len1

        # 对于找较小值，则是找到二进制中最后一个10，改为01，再把右边所有的1左移
        last10 = lower_one.rfind('10')
        if last10==-1:
            lower_one = '-1'
        else:
            count1 = lower_one.count('1',last10+1)
            len0 = len(lower_one) - last10 - 2 - count1
            lower_one = lower_one[0:last10]+'01'+'1'*count1 + '0'*len0

        return [int(bigger_one,2),int(lower_one,2)]


from typing import List
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        max_limit = (1 << 31) - 1
        if num == max_limit:
            return [-1, -1]
        # print(bin(num), len(bin(num)))
        bigger = smaller = bin(num)[2:]
        bigger = '0' + bigger
        last_01 = bigger.rfind('01')
        count_0 = bigger[last_01:].count('0')
        count_1 = len(bigger) - last_01 - count_0
        bigger = bigger[:last_01] + '10' + '0' * (count_0 - 1) + '1' * (count_1 - 1)
        last_10 = smaller.rfind('10')
        if last_10 == -1:
            smaller = '-1'
        else:
            count_0 = smaller[last_10:].count('0')
            count_1 = len(smaller) - last_10 - count_0
            smaller = smaller[:last_10] + '01' + '1' * (count_1 - 1) + '0' * (count_0 - 1)
        res = [int(bigger, 2), int(smaller, 2)]
        # print(bin(res[0]), bin(res[1]))
        return res

S = Solution()
print(S.findClosedNumbers(2))
print(S.findClosedNumbers(1))
print(S.findClosedNumbers(34))
"""
输入：
34
输出：
[591,33]
预期结果：
[36,33]
"""
print(S.findClosedNumbers(2147483647))
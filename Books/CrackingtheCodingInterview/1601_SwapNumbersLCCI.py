"""
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：

输入: numbers = [1,2]
输出: [2,1]
提示：

numbers.length == 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-numbers-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        a, b = numbers
        b = a ^ b
        a = a ^ b
        b = a ^ b
        return [a, b]

S = Solution()
numbers = [1,2]
print(S.swapNumbers(numbers))
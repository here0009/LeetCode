"""
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。

示例：

输入： a = 1, b = 2
输出： 2
"""


class Solution:
    def maximum(self, a: int, b: int) -> int:
        diff = abs(a - b)
        return (a + b + diff) // 2

class Solution:
    def maximum(self, a: int, b: int) -> int:
        diff = ((b-a) ** 2) ** 0.5
        return int((a+b+diff) // 2)

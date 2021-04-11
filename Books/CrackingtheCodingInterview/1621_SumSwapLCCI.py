"""
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。

返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。

示例:

输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
示例:

输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
提示：

1 <= array1.length, array2.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-swap-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1) - sum(array2)
        if diff % 2 == 1:
            return []
        diff = diff // 2
        num_set_1 = set(array1)
        num_set_2 = set(array2)
        for num in num_set_1:
            if num - diff in num_set_2:
                return [num, num - diff]
        return []

S = Solution()
array1 = [4, 1, 2, 1, 1, 2]
array2 = [3, 6, 3, 3]
print(S.findSwapValues(array1, array2))
array1 = [1, 2, 3]
array2 = [4, 5, 6]
print(S.findSwapValues(array1, array2))
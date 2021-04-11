"""
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

示例：

输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
提示：

0 <= len(array) <= 1000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sub-sort-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if not array:
            return [-1, -1]
        length = len(array)
        pre_stack = [0]
        suff_stack = [length - 1]
        for i in range(length):
            v = array[i]
            while pre_stack and v < array[pre_stack[-1]]:
                pre_stack.pop()
            if pre_stack and i - pre_stack[-1] == 1:
                pre_stack.append(i)
        for i in range(length - 1, -1, -1):
            v = array[i]
            while suff_stack and v > array[suff_stack[-1]]:
                suff_stack.pop()
            if suff_stack and i - suff_stack[-1] == -1:
                suff_stack.append(i)

        # print(pre_stack, suff_stack)
        if len(pre_stack) == length:
            return [-1, -1]
        return [len(pre_stack), length - 1 - len(suff_stack)]


S = Solution()
array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(S.subSort(array))
array = [1,2,3,2,3,4,9]
print(S.subSort(array))
array = [1,2,3,4,5,6]
print(S.subSort(array))
array = []
print(S.subSort(array))
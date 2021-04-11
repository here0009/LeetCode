"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sorted-merge-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # print(A, B)
        if m == 0:
            for i in range(n):
                A[i] = B[i]
        else:
            idx = m + n - 1
            ia, ib = m - 1, n - 1
            while idx >= 0:
                if A[ia] >= B[ib]:
                    A[idx] = A[ia]
                    ia -= 1
                else:
                    A[idx] = B[ib]
                    ib -= 1
                idx -= 1
        print(A)


from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        idx = m + n - 1
        ia, ib = m - 1, n - 1
        while ia >= 0 and ib >= 0:
            if A[ia] >= B[ib]:
                A[idx] = A[ia]
                ia -= 1
            else:
                A[idx] = B[ib]
                ib -= 1
            idx -= 1
        while ib >= 0:
            A[idx] = B[ib]
            idx -= 1
            ib -= 1
        # print(A)

S = Solution()
A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
print(S.merge(A, m, B, n))
A = [0]
m = 0
B = [1]
n = 1
print(S.merge(A, m, B, n))
A = [2,0]
m = 1
B = [1]
n = 1
print(S.merge(A, m, B, n))
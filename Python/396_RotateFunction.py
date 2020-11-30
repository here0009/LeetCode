"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""


from typing import List
from collections import deque
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        """
        TLE
        """
        length = len(A)
        index = deque(list(range(length)))
        res = sum(A[i]*index[i] for i in range(length))
        for i in range(length-1):
            # print(index)
            index.append(index.popleft())
            res = max(res, sum(A[i]*index[i] for i in range(length)))
        return res


from typing import List
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        length = len(A)
        index = list(range(length))
        res = curr = sum(A[i]*index[i] for i in range(length))
        total = sum(A)
        for i in range(length-1):
            curr += total - length*A[index.pop()]
            # print(index, curr)
            res = max(res, curr)
        return res


from typing import List
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        length = len(A)
        index = length-1
        res = curr = sum(A[i]*i for i in range(length))
        total = sum(A)
        for i in range(length-1):
            curr += total - length*A[index]
            res = max(res, curr)
            index -= 1
        return res

S = Solution()
A = [4, 3, 2, 6]
print(S.maxRotateFunction(A))

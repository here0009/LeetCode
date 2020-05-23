"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
"""
from collections import deque
class Solution:
    def numSubarrayBoundedMax(self, A, L: int, R: int) -> int:
        res = 0
        max_num = -1
        pre = 0
        start_index = -1
        for i,n in enumerate(A): 
            if n > R:
                pre = 0
                max_num = -1
                start_index = i
            elif n <= R and n >= L:
                pre = i - start_index
                res += pre
                max_num = max(max_num,n)
            elif n < L:
                if max_num != -1:
                    res += pre
        return res

S = Solution()
A = [2, 1, 4, 3]
L = 2
R = 3
print(S.numSubarrayBoundedMax(A,L,R))

A = [2,9,2,5,6]
L = 2
R = 8
print(S.numSubarrayBoundedMax(A,L,R))
"""
Output
4
Expected
7
"""

A = [2,1,3]
L = 2
R = 3
print(S.numSubarrayBoundedMax(A,L,R))



A = [73,55,36,5,55,14,9,7,72,52]
L = 32
R = 69
# Output:
# 25
# Expected:
# 22
print(S.numSubarrayBoundedMax(A,L,R))

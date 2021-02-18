"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""

# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/JavaC%2B%2BPython-DP-O(N)-Solution


from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        Thoughts: do not actually swap A, B. keep 2 variables, to record the minimum swaps needed to keep A and B increasing for a specific index
        at 0, swap = 1, noswap = 0
        we may encounter several conditions
        1. A[i-1] < A[i] and B[i-1] < B[i]
        swap2 = swap + 1 # if we swap A[i-1] and B[i-1] before, we also need to swap A[i] and B[i]
        noswap2 = noswap
        2. A[i-1] < B[i] and B[i-1] < A[i]
        swap2 = noswap + 1
        noswap2 = swap

        notice that conditon 2 may overlap with condition 1. so we initailize swap2, noswap2 with len(A)
        and, finally:
        swap2 = min(swap2, noswap + 1)
        noswap2 = min(noswap2, swap)

        think about the test case
        A = [1, 4, 101, 102, 103]
        B = [99, 100, 5, 6, 7]
        when i == 1, A[i-1] < A[i] and B[i-1] < B[i], but we still need to swap A[:2] and B[:2] to get the optimal solution.
        so A[i-1] < A[i] and B[i-1] < B[i] do not mean we do not need to swap
        """
        swap, noswap = 1, 0
        length = len(A)
        for i in range(1, len(A)): # because it is guaranteed there is a valid answer, there can not be A[i] < min(A[i-1], B[i-1]) or B[i]< min(A[i-1], B[i-1])
            swap2, noswap2 = length, length
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap2 = noswap + 1
                noswap2 = swap
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap2 = min(swap2, swap + 1)
                noswap2 = min(noswap, noswap2)
            swap, noswap = swap2, noswap2
            # print(i, A[i], B[i], swap, noswap)
        return min(swap, noswap)


S = Solution()
A = [1,3,5,4]
B = [1,2,3,7]
print(S.minSwap(A, B))

A = [3,3,8,9,10]
B = [1,7,4,6,8]
print(S.minSwap(A, B))
# Output
# 2
# Expected
# 1
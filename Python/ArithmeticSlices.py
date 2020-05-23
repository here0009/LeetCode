"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        diff = [A[i]-A[i-1] for i in range(1, len(A))]
        # print(diff)
        if len(diff) < 2:
            return 0
        pre = diff[0]
        counts = 1
        res = 0
        for i in range(1, len(diff)):
            if diff[i] == pre:
                res += counts
                counts += 1
            else:
                counts = 1
                pre = diff[i]
        return res

class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        dp, s = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                s += dp
            else:
                dp = 0
        return s

s = Solution()
A = [1, 2, 3, 4]
print(s.numberOfArithmeticSlices(A))
A = [1,2]
print(s.numberOfArithmeticSlices(A))
A = [6,7,8,9,10]
print(s.numberOfArithmeticSlices(A))
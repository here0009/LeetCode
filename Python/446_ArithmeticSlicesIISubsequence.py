"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
 
A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.

 
Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""


from collections import Counter
class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        gap_list = [Counter()]  # gap[i] record the gap A[i] and length A[i] make with A[:i]
        res = 0
        for i, v in enumerate(A[1:], 1):
            tmp_dict = Counter()
            for j in range(i):
                gap = A[i] - A[j]
                tmp_dict[gap] += gap_list[j][gap] + 1
                if gap_list[j][gap] > 0:
                    res += gap_list[j][gap]
            gap_list.append(tmp_dict)
            # print(gap_list, i, v, res)
        return res


from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, A):
        ans = 0
        dp = defaultdict(lambda: 0)
        for i in range(1, len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                ans += dp[(j, delta)]
                dp[(i, delta)] += dp[(j, delta)] + 1
        return ans

S = Solution()
A = [2, 4, 6, 8, 10]
print(S.numberOfArithmeticSlices(A))
A = [2,2,3,4]
print(S.numberOfArithmeticSlices(A))
A = [-2147483648,0,-2147483648]
print(S.numberOfArithmeticSlices(A))
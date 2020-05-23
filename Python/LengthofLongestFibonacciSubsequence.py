"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
 

Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
"""
"""
Thoughts:
use a gap_dict to store, (third, second):length, if (second, third - second) in gap_dict, update the gap dict for every element
"""
from collections import defaultdict
class Solution_1:
    def lenLongestFibSubseq(self, A) -> int:
        gap_dict = defaultdict(lambda:2)
        len_A = len(A)
        set_A = set(A)
        for i in range(len_A):
            for j in range(i):
                third, second = A[i], A[j]
                first = third - second
                if (second, first) in gap_dict: #
                    gap_dict[(third, second)] = gap_dict[(second, first)] + 1
                    # del gap_dict[(second, first)]
                else:
                    gap_dict[(third, second)] = 2
        res = max(gap_dict.values())
        if res <= 2:
            res = 0
        return  res

from collections import defaultdict
class Solution_2:
    def lenLongestFibSubseq(self, A) -> int:
        dp = defaultdict(lambda:2)
        len_A = len(A)
        set_A = set(A)
        for i in range(len_A):
            for j in range(i):
                first = A[i] - A[j]
                if first < A[j] and first in set_A:
                    dp[(A[i],A[j])] = dp[A[j],(A[i]-A[j])] + 1
        # print(dp)
        return max(dp.values() or [0])

class Solution_3:
    def lenLongestFibSubseq(self, A) -> int:
        set_A = set(A)
        len_A = len(A)
        res = 0
        for i in range(len_A):
            for j in range(i):
                length = 2
                first, second = A[j], A[i]
                while first+second in set_A :
                    first, second = second, first+second
                    length += 1
                res = max(res, length)
        return res if res > 2 else 0

class Solution:
    def lenLongestFibSubseq(self, A):
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0

s = Solution()
A = [1,2,3,4,5,6,7,8]
print(s.lenLongestFibSubseq(A))

A = [1,3,7,11,12,14,18]
print(s.lenLongestFibSubseq(A))

A = [2,4,7,8,9,10,14,15,18,23,32,50]
print(s.lenLongestFibSubseq(A))


A = [1,3,5]
print(s.lenLongestFibSubseq(A))

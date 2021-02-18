"""
You are given an integer array A. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

 

Example 1:

Input: A = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3],
A[4] that is greater or equal to A[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
Example 2:

Input: A = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

During our 1st jump (odd-numbered), we first jump to i = 1 because A[1] is the smallest value in [A[1], A[2],
A[3], A[4]] that is greater than or equal to A[0].

During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in [A[2], A[3],
A[4]] that is less than or equal to A[1]. A[3] is also the largest value, but 2 is a smaller index, so we can
only jump to i = 2 and not i = 3

During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in [A[3], A[4]]
that is greater than or equal to A[2].

We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.

In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
Example 3:

Input: A = [5,1,3,4,2]
Output: 3
Explanation: 
We can reach the end from starting indices 1, 2, and 4.
 

Constraints:

1 <= A.length <= 2 * 104
0 <= A[i] < 105
"""


from bisect import bisect_left, insort
class Solution:
    """
    from i we can only jump to the smallest value >= A[i] or largest value <= A[i]
    wrong answer
    """
    def oddEvenJumps(self, A: List[int]) -> int:

        len_A = len(A)
        dp = [[0, 0]] * len_A  # odd jump and even jump we can make to reach the end of A
        dp[-1] = [-float('inf'), 1]
        val_index = [(-float('inf'), -1), (A[-1], len_A - 1), (float('inf'), len_A)]
        for i in range(len_A - 2, -1, -1):
            v = A[i]
            odd, even = 0, 0
            # smallest of val that val_index[j][0] <= v
            j = bisect_left(val_index, (v, i))  # smallest of val that val_index[j][0] >= v
            # print(val_index, j)
            print(val_index, j, (v, i))
            if val_index[j][0] == v:  # only one, can be used both as odd and even jumps
                odd += dp[j][1]
                even += dp[j][0]
            else:
                if val_index[j][0] > v and val_index[j][1] != len_A: # smallest value > v and not float('inf'):
                    odd += dp[val_index[j][1]][1]
                if j - 1 > 0 : # largest value < v and not -float('inf')
                    even += dp[val_index[j - 1][1]][0]

            insort(val_index, (v, i))
            dp[i] = [odd, even]
            print(dp)
        return sum(lst[0] for lst in dp if lst[0] > 0) + 1

# https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
from typing import List
class Solution:
    """
    the way to generate next_higher and next_lower using stack is great
    """
    def oddEvenJumps(self, A: List[int]) -> int:
        len_A = len(A)
        sort_A = sorted([(a, i) for i, a in enumerate(A)])
        stack = []
        next_higher = [0] * len_A
        for a, i in sort_A:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        next_lower = [0] * len_A
        sort_A = sorted([(-a, i) for i, a in enumerate(A)])
        for a, i in sort_A:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        odd, even = [0] * len_A, [0] * len_A
        odd[-1] = 1
        even[-1] = 1
        for j in range(len_A - 2, -1, -1):
            odd[j] = even[next_higher[j]]
            even[j] = odd[next_lower[j]]
        return sum(odd)




S = Solution()
A = [10,13,12,14,15]
print(S.oddEvenJumps(A))
A = [2,3,1,1,4]
print(S.oddEvenJumps(A))
A = [5,1,3,4,2]
print(S.oddEvenJumps(A))
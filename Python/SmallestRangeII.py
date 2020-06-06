"""
Given an array A of integers, for each integer A[i] we may choose either x = -K or x = K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_A = max(A)
        min_A = min(A)
        # if K >= max_A - min_A:
        #     return max_A - min_A
        B = []
        for a in A:
            b1 = a-K
            b2 = a+K
            if b2 > max_A:
                B.append(b1)
            if b1 < min_A:
                B.append(b2)
            if max_A - b2 >= b1 - min_A:
                B.append(b2)
            else:
                B.append(b1)

        return min(max_A - min_A, max(B)-min(B))


class Solution:
    def smallestRangeII(self, A, K: int) -> int:
        """
        Thoughts: for every n in A, we try to add K to all A[:i], minus K for all A[i+1:]
        then updated the max_range of this
        """
        A = sorted(A)
        min_v, max_v = A[0], A[-1]
        res = max_v - min_v
        for i in range(len(A) - 1):
            min_v = min(A[i+1]-K, A[0]+K)
            max_v = max(A[-1]-K, A[i]+K)
            res = min(res, max_v - min_v)
        return res

s = Solution()
A = [1,3,6]
K = 3
print(s.smallestRangeII(A, K))
A = [1]
K = 0
print(s.smallestRangeII(A, K))
A = [0,10]
K = 2
print(s.smallestRangeII(A, K))
A = [7,8,8]
K = 5
print(s.smallestRangeII(A, K))
A = [6,4,10]
K = 5
print(s.smallestRangeII(A, K))
A = [7,8,8,5,2]
K = 4

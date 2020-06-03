"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""


class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        """
        TLE
        """
        if len(A) == 1:
            return A[0]
        preSum = []
        tmp = 0
        res = float('-inf')
        for n in A:
            tmp += n
            res = max(res, tmp)
            preSum.append(tmp)
        total = tmp
        length = len(preSum)
        # print(preSum)
        for i in range(length - 1):
            for j in range(i + 1, length):
                tmp = preSum[j] - preSum[i]
                res = max(res, tmp, total - tmp)
        return res


class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        """
        Kadane's Algorithm
        """
        total, curr_max, curr_min = 0, 0, 0
        sum_Max, sum_Min = A[0], A[0]
        for n in A:
            curr_max = max(curr_max + n, n)
            sum_Max = max(sum_Max, curr_max)
            curr_min = min(curr_min + n, n)
            sum_Min = min(sum_Min, curr_min)
            total += n
        # print(sum_Max, sum_Min, total)
        return max(sum_Max, total - sum_Min) if sum_Max > 0 else sum_Max

S = Solution()
A = [1,-2,3,-2]
print(S.maxSubarraySumCircular(A))
A = [5,-3,5]
print(S.maxSubarraySumCircular(A))
A = [3,-1,2,-1]
print(S.maxSubarraySumCircular(A))
A = [3,-2,2,-3]
print(S.maxSubarraySumCircular(A))
A = [-2,-3,-1]
print(S.maxSubarraySumCircular(A))
A = [-2]
print(S.maxSubarraySumCircular(A))
A = [3,1,3,2,6]
print(S.maxSubarraySumCircular(A))
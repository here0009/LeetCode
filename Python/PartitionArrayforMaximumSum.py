"""
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""

class Solution_1:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        N = len(A)
        if N == 0:
            return 0
        dp = [0]*(N+1)
        #dp[N] = dp[-1] = 0, so when i-k == -1, dp[i] = maxNum*k + 0
        for i in range(len(A)):
            maxNum = 0
            length = min(i+1,K)
            for k in range(1,length+1):
                maxNum = max(A[i-k+1], maxNum)
                dp[i] = max(dp[i], dp[i-k]+maxNum*k)
            print(dp)
        return dp[N-1]

class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        N = len(A)
        if N == 0:
            return 0
        dp = [0]*(N+1) #dp[i+1] stores the res ends of A[i]
        for i in range(len(A)):
            maxNum = 0
            length = min(i+1,K)
            tmpNum  = 0
            for k in range(1,length+1):
                maxNum = max(A[i-k+1], maxNum)
                dp[i+1] = max(dp[i+1], dp[i+1-k]+maxNum*k)
            # print(dp)
        return dp[-1]

s = Solution()
A = [1,15,7,9,2,5,10]
K = 3
print(s.maxSumAfterPartitioning(A,K))

A = []
K = 1
print(s.maxSumAfterPartitioning(A,K))

A = [1,4,1,5,7,3,6,1,9,9,3]
K = 4
print(s.maxSumAfterPartitioning(A,K))

A = [3,7]
K = 2
print(s.maxSumAfterPartitioning(A,K))
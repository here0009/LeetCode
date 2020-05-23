"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
class Solution:
    def __init__(self):
        self.N = 10**9+7

    def sumSubarrayMins(self, A) -> int:
        """
        the min value (index i) of A is the min value of (i+1)*(len(A)-i+1) subarrays
        TLE
        """
        
        if len(A) == 0:
            return 0
        min_i, min_v = 0, A[0]
        for i in range(1, len(A)):
            if A[i] < min_v:
                min_v = A[i]
                min_i = i
        return (min_v*(min_i+1)*(len(A)-min_i) + self.sumSubarrayMins(A[:min_i]) + self.sumSubarrayMins(A[min_i+1:])) % self.N


class Solution:
    def __init__(self):
        self.N = 10**9+7

    def sumSubarrayMins(self, A) -> int:
        """
        use a stack to record the index of num smaller than current num
        """
        A = [0] + A + [0]
        stack = []
        res = 0
        for i,v in enumerate(A):
            while stack and v < A[stack[-1]]:
                curr = stack.pop()
                res += A[curr]*(i-curr)*(curr-stack[-1]) 
            stack.append(i)
        return res% self.N



s = Solution()
A = [3,1,2,4]
print(s.sumSubarrayMins(A))
A = [1]
print(s.sumSubarrayMins(A))
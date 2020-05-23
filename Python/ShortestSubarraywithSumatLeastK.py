"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""
class Solution:
    """
    TLE
    """
    def shortestSubarray(self, A, K: int) -> int:
        len_A = len(A)
        accA = [0] + A
        
        for i in range(1,len_A+1):
            accA[i] += accA[i-1]
        # print(accA)
        for k in range(1,len_A+1):
            for start in range(len_A+1-k):
                if accA[start+k] - accA[start] >= K:
                    return k
        return -1

from collections import deque
class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        len_A = len(A)
        t_Sum = 0
        dq = deque()
        res = float('inf')
        index = 0
        while index < len_A:
            print(dq,t_Sum,res)
            dq.append(A[index])
            t_Sum += A[index]
            index += 1
            if t_Sum < K:
                continue
            while len(dq) > 0 and t_Sum - dq[0] >= K:
                t_Sum -= dq.popleft()
            print(dq,t_Sum,res)
            res = min(res, len(dq))
        if res == float('inf'):
            return -1
        else:
            return res


from collections import deque
class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        len_A = len(A)
        accA = [0] + A
        for i in range(1,len_A+1):
            accA[i] += accA[i-1]
        res = float('inf')
        dq = deque()
        for i in range(len_A+1):
            while dq and accA[i] - accA[dq[0]] >= K:
                res = min(res, i - dq.popleft())
            while dq and accA[dq[-1]] >= accA[i]:
                dq.pop()
            dq.append(i)
        return res if res != float('inf') else -1


s = Solution()
A = [1]
K = 1
print(s.shortestSubarray(A,K))

A = [1,2]
K = 4
print(s.shortestSubarray(A,K))

A = [2,-1,2]
K = 3
print(s.shortestSubarray(A,K))

A = [77,19,35,10,-14]
K = 19
print(s.shortestSubarray(A,K))

A = [17,85,93,-45,-21]
K = 150
print(s.shortestSubarray(A,K))

A = [84,-37,32,40,95]
K = 167
print(s.shortestSubarray(A,K))
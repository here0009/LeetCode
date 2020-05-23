"""
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
from bisect import bisect_left
class Solution:
    def advantageCount(self, A, B):
        A = sorted(A)
        res = []
        for num in B:
            index = bisect_left(A, num+1) % len(A)
            res.append(A[index])
            A.pop(index)
        return res

s = Solution()
A = [2,7,11,15]
B = [1,10,4,11]
print(s.advantageCount(A,B))

A = [12,24,8,32]
B = [13,25,32,11]
print(s.advantageCount(A,B))

"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2

Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
from collections import Counter
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_counter = Counter(A)
        half_size = len(A)//2
        for key,value in A_counter.items():
            if value == half_size:
                return key
        return -1

s = Solution()
A = [1,2,3,3]
print(s.repeatedNTimes(A))

A = [2,1,2,5,3,2]
print(s.repeatedNTimes(A))

A = [5,1,5,2,5,3,5,4]
print(s.repeatedNTimes(A))
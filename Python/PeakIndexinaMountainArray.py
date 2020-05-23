"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

"""

"""
Use the method like binary search
search from the middle point
i = (start + end) /2
if A[i-1] < A[i] > A[i+1]
return i
elif A[i-1] < A[i] < A[i+1]
search A[i, end]
elif A[i-1] > A[i] > A[i+1]
search A[start, i]
"""

class Solution_1:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        end = len(A)
        start = 0
        i = (start + end) // 2
        # print("i:", i, A[i])
        if A[i] > A[i-1] and A[i] > A[i+1] :
            # print(i)
            return i
        elif A[i-1] < A[i] and A[i] < A[i+1]:
            # print(i-1, end)
            return i-1 + self.peakIndexInMountainArray(A[i-1:])
        elif A[i-1] > A[i] and A[i] > A[i+1]:
            # print(start, i+1)
            # print(A[:i])
   
            return self.peakIndexInMountainArray(A[:i+1])

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i

s = Solution()

test = [0,1,0]
print(s.peakIndexInMountainArray(test))

test = [0,2,1,0]
print(s.peakIndexInMountainArray(test))

test = [40,48,61,75,100,99,98,39,30,10]
print(s.peakIndexInMountainArray(test))
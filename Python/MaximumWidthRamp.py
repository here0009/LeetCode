"""
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
 

Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
"""
class Solution_1:
    """
    Too Slow
    """
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 0
        end = len(A)-1
        len_A = len(A)-1
        k = 0
        while start < end:
            for i in range(k+1):
                j = k - i
                # print(i,j)
                if A[start+i] <= A[end-j]:
                    return len_A-k
            s_step = 1
            e_step = 1
            while A[start] <= A[start+s_step]:
                s_step+=1
            while A[end-e_step] <= A[end]:
                e_step+=1
            end -= e_step
            k += 1
        return 0

"""
Thoughts: Method from the discussion board
Use a stack to store the decreasing numbers from start to end.
Then loop the list from end to start. Pop the value in the stack until it is larger than the value in the list, calculate the difference of index numbers and store in res. 
If the value in the list is smaller than the last value in the stack, go to the next value in the list.
If the stack is empty, return res
"""
from collections import deque
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = deque()
        len_A = len(A)
        res = 0
        for index, a in enumerate(A):
            if not d:
                d.append(index)
            if a < A[d[-1]]:
                d.append(index)
        for i in range(len(A))[::-1]:
        # for index, a in enumerate(A[::-1]):
            while d:
                if A[d[-1]] <= A[i]:
                    res = max(res, i-d.pop())
                else:
                    break
        return res


s = Solution()

A = [6,0,8,2,1,5]
print(s.maxWidthRamp(A))

A = [9,8,1,0,1,9,4,0,4,1]
print(s.maxWidthRamp(A))

A = [3,2]
print(s.maxWidthRamp(A))

A = [4,2,3,1]
print(s.maxWidthRamp(A))
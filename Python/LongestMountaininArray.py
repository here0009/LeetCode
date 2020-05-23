"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
class Solution:
    def longestMountain(self, A) -> int:
        if len(A) < 3:
            return 0
        res = 0
        curr_length = 0
        pre = A[0]
        inc = 0 #1 for increasing, -1 for decreasing, 0 for equal
        for n in A[1:]:
            if n > pre:
                if inc == 1:
                    curr_length +=1 
                else:
                    inc = 1
                    curr_length = 2
            elif n < pre:
                if inc == 1:
                    inc = -1
                if inc == -1:
                    curr_length += 1
                    res = max(res, curr_length)
            else:
                inc = 0
            pre = n
        return res if res > 2 else 0


class Solution:
    def longestMountain(self, A) -> int:
        res = 0
        len_A = len(A)
        if len_A < 3:
            return 0
        ups = [0]*len_A
        downs = [0]*len_A
        for i in range(1,len_A):
            if A[i] > A[i-1]:
                ups[i] = ups[i-1]+1

        for i in range(len_A-2, -1, -1):
            if A[i] > A[i+1]:
                downs[i] = downs[i+1]+1

        for i in range(1,len_A-1):
            if ups[i] > 0 and downs[i] > 0:
                res =  max(res, ups[i]+downs[i]+1)
        return res if res > 2 else 0

s = Solution()
A = [2,1,4,7,3,2,5]
print(s.longestMountain(A))

A = [2,2,2]
print(s.longestMountain(A))

A = [1,2,1]
print(s.longestMountain(A))

A = [2,3]
print(s.longestMountain(A))
"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        pre_num = A[0]
        num = A[1]
        if pre_num < num:
            increasing = True
            pre_num = num
        else:
            return False
        for num in A[2:]:
            if increasing:
                # print(pre_num,num)
                if num > pre_num:
                    pass
                elif num < pre_num:
                    increasing = False
                else:
                    return False
            else:
                if num >= pre_num:
                    return False
                else:
                    pass
            pre_num = num
        if increasing:
            return False
        else:
            return True

s = Solution()
A = [2,1]
print(s.validMountainArray(A))
A = [3,5,5]
print(s.validMountainArray(A))
A = [0,3,2,1]
print(s.validMountainArray(A))
A = [0,1,2,3,4,5,6,7,8,9]
print(s.validMountainArray(A))
A = [9,8,7,6,5,4,3,2,1,0]
print(s.validMountainArray(A))
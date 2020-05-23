"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""
class Solution:
    def longestOnes(self, A, K):
        counter = []
        pre = A[0]
        counts = 1
        for i in range(1,len(A)):
            if A[i] == pre:
                counts += 1
            else:
                counter.append((pre,counts))
                pre = A[i]
                counts = 1
        counter.append((pre,counts)) # the last one

        for _num, _counts in counter:
            if _num >= K:
                
        return counter

s = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(s.longestOnes(A,K))

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(s.longestOnes(A,K))

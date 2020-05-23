"""
1004. Max Consecutive Ones III
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
"""
if in A[i]~A[j] we have zeros <= K, we continue increase j
else
we increase i, if we can remove 0 from the subarry, and zeros <= K again, we can increas j again.
"""
class Solution:
    def longestOnes(self, A, K: int) -> int:
        i = 0
        zeros = 0
        for j in range(len(A)):
            if A[j] == 0:
                zeros += 1
            if zeros > K:
                if A[i] == 0:
                    zeros -= 1
                i+=1
        return j-i+1
        

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
s = Solution()
print(s.longestOnes(A,K))
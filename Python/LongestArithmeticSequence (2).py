"""
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
 

Note:

2 <= A.length <= 2000
0 <= A[i] <= 10000
"""
class Solution:
    def longestArithSeqLength(self, A) -> int:
        length  = len(A)
        step_index_dict = dict()
        for i in range(length):
            for j in range(i):
                step = A[j] - A[i]
                if (step,j) in step_index_dict:
                    step_index_dict[(step,i)] = step_index_dict[(step,j)] + 1
                else:
                    step_index_dict[(step,i)] = 1
        # print(A)
        # print(step_index_dict)
        return max(step_index_dict.values())+1

S = Solution()
A = [3,6,9,12]
print(S.longestArithSeqLength(A))
A = [9,4,7,2,10]
print(S.longestArithSeqLength(A))
A = [20,1,15,3,10,5,8]
print(S.longestArithSeqLength(A))
A = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
print(S.longestArithSeqLength(A))
# Output
# 7
# Expected
# 4
"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have a string "abcdef" and deletion indices {0, 2, 3}, then the final string after deletion is "bef".

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]

Return the minimum possible value of D.length.

 

Example 1:

Input: ["cba","daf","ghi"]
Output: 1
Example 2:

Input: ["a","b"]
Output: 0
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 1000
"""
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        len_A = len(A)
        len_word = len(A[0])
        res = 0
        for j in range(len_word):
            for i in range(len_A-1):
                if A[i][j] > A[i+1][j]:
                    res += 1
                    break
        return res

s = Solution()
A = ["cba","daf","ghi"]
print(s.minDeletionSize(A))
A = ["a","b"]
print(s.minDeletionSize(A))
A = ["zyx","wvu","tsr"]
print(s.minDeletionSize(A))
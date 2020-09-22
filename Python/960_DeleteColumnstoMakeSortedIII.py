"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.

 

Example 1:

Input: ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
Example 2:

Input: ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
Example 3:

Input: ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""


class Solution:
    def minDeletionSize(self, A) -> int:
        """
        min deletion equals to max extension
        """
        B = [''.join(s) for s in zip(*A)] #put letters that got the same col number together
        len_A = len(A)
        len_letter = len(A[0])
        dp = [1]*len_letter # the max extension ends at each col
        for j in range(1, len_letter):
            for i in range(j):
                if all(ia <= ja for ia,ja in zip(B[i], B[j])):
                    dp[j] = max(dp[j], dp[i]+1)
        return len_letter - max(dp)


class Solution:
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for j in range(1, W):
            for i in range(j):
                if all(row[i] <= row[j] for row in A):
                    dp[j] = max(dp[i]+1, dp[j])
        return W - max(dp)

S = Solution()
A = ["babca","bbazb"]
print(S.minDeletionSize(A))
A = ["edcba"]
print(S.minDeletionSize(A))
A = ["ghi","def","abc"]
print(S.minDeletionSize(A))



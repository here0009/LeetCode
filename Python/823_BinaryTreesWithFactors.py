"""
Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
"""


from typing import List
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        M = 10**9+7
        A_set = set(A)
        A.sort()
        dp = dict()
        length = len(A)
        for i in range(length):
            num = A[i]
            dp[num] = 1
            for j in range(i):
                q, rmd = divmod(num, A[j])
                if rmd == 0 and q in A_set:
                    dp[num] += dp[A[j]]*dp[q]
            dp[num] = dp[num] % M
        return sum(dp.values()) % M

S = Solution()
A = [2, 4]
print(S.numFactoredBinaryTrees(A))
A = [2, 4, 5, 10]
print(S.numFactoredBinaryTrees(A))
A = [18,3,6,2]
print(S.numFactoredBinaryTrees(A))
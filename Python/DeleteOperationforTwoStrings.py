"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
"""
find the lcs(longest common subsequence) , then len(word1) + len(word2) - lcs
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return l1+l2-2*dp[-1][-1]

s = Solution()
word1 = "sea" 
word2 = "eat"
print(s.minDistance(word1, word2))

"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
class Solution_1:
    def longestPalindromeSubseq(self, string: str) -> int:
        rev_string = string[::-1]
        len_s = len(string)+1
        dp = [[0]*(len_s) for _ in range(len_s)]
        for i in range(1, len_s):
            for j in range(1, len_s):
                if string[i-1] == rev_string[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

class Solution:
    def longestPalindromeSubseq(self, string: str) -> int:
        len_s = len(string)
        dp = [[0]*len_s for _ in range(len_s)]
        for i in range(len_s-1, -1, -1): #i decreasing and j increasing
            dp[i][i] = 1
            for j in range(i+1, len_s):
                if string[i] == string[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][len_s-1]


s = Solution()
string = "bbbab"
print(s.longestPalindromeSubseq(string))
string = "cbbd"
print(s.longestPalindromeSubseq(string))

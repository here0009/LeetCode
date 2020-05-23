"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""
class Solution_1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        two sequences alginment
        dp[i][j] stores the longest seq that ends with text1[i] and text2[j]
        """
        len_1 = len(text1) #row number
        len_2 = len(text2) #col number
        dp = [[0]*len_2 for _ in range(len_1)]
        for i in range(len_1): #1st col
            if (i > 0 and dp[i-1][0] == 1) or text2[0] == text1[i]:
                dp[i][0] = 1
        for j in range(len_2): #1st row
            if (j > 0 and dp[0][j-1] == 1) or text1[0] == text2[j]:
                dp[0][j] = 1

        for i in range(1,len_1):
            for j in range(1, len_2):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1, dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(['#'] + list(text2))
        # for i in range(len_1):
        #     print([text1[i]]+[str(n) for n in dp[i]])
        return max([max(row) for row in dp])

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        two sequences alginment
        dp[i][j] stores the longest seq that ends with text1[i] and text2[j]
        add a extra row and col
        """
        text1 = '#' + text1
        text2 = '@' + text2
        # text1 and text2 are only small case english letters
        len_1 = len(text1) #row number
        len_2 = len(text2) #col number
        dp = [[0]*len_2 for _ in range(len_1)]
        for i in range(1,len_1):
            for j in range(1, len_2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(['#'] + list(text2))
        # for i in range(len_1):
        #     print([text1[i]]+[str(n) for n in dp[i]])
        return dp[-1][-1]


s = Solution()
text1 = "abcde"
text2 = "ace" 
print(s.longestCommonSubsequence(text1, text2))


text1 = "abc"
text2 = "abc"
print(s.longestCommonSubsequence(text1, text2))

text1 = "abc"
text2 = "def"
print(s.longestCommonSubsequence(text1, text2))

text1 ="bsbininm"
text2 = "jmjkbkjkv"
print(s.longestCommonSubsequence(text1, text2))

"""
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        length = len(s)
        dp = [[0]*(length+1) for _ in range(length+1)]
        rev_s = s[::-1]
        for i in range(1, length+1):
            for j in range(1, length+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+(s[i-1]==rev_s[j-1]))
        # for row in dp:
        #     print(row)
        return length-dp[-1][-1] <= k


from functools import lru_cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def dp(i, j, k):
            if k < 0:
                return False
            if i >= j:
                return True
            if s[i] == s[j]:
                return dp(i+1, j-1, k)
            return dp(i+1, j, k-1) or dp(i, j-1, k-1)
        return dp(0, len(s)-1, k)



S = Solution()
s = "abcdeca"
k = 2
print(S.isValidPalindrome(s, k))
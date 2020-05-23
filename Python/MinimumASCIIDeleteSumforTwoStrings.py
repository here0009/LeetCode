"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""
class Solution_1:
    """
    it is too complicated to store the largest of the longest common subsring, then delete it from both s1 and s2. We can just use dp the store the deletion information.
    """
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*len(s2) for _ in range(len(s1))]
        res = 0
        print(dp)
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                dp[i][0] = 1
        for j in range(len(s2)):
            if s2[j] == s1[0]:
                dp[0][j] = 1
        for i in range(1,len(s1)):
            for j in range(1,len(s2)):
                tmp = 0
                if s1[i] == s2[j]:
                    tmp = 1+dp[i-1][j-1] 
                dp[i][j] = max(tmp, dp[i-1][j], dp[i][j-1])
        print(dp)

        dp_text = [['']*len(s2) for _ in range(len(s1))]
        print(dp_text)
        max_length = 0
        max_set = set()
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                dp_text[i][0] = s2[0]
        for j in range(len(s2)):
            if s2[j] == s1[0]:
                dp_text[0][j] = s1[0]
        for i in range(1,len(s1)):
            for j in range(1,len(s2)):
                tmp = ''
                if s1[i] == s2[j]:
                    tmp = dp_text[i-1][j-1]+s1[i]
                if len(tmp) >= max(len(dp_text[i-1][j]), len(dp_text[i][j-1])):
                    dp_text[i][j] = tmp
                else:
                    dp_text[i][j] = max(dp_text[i-1][j], dp_text[i][j-1], key=len)

                # dp_text[i][j] = max(tmp, dp_text[i-1][j], dp_text[i][j-1], key=len)
        print(dp_text)
        
        return res

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len_s1, len_s2 = len(s1), len(s2)
        dp = [[0]*(len_s2+1) for _ in range(len_s1+1)]
        for i in range(len_s1-1, -1, -1):
            dp[i][len_s2] = dp[i+1][len_s2] + ord(s1[i])
        for j in range(len_s2-1, -1, -1):
            dp[len_s1][j] = dp[len_s1][j+1] + ord(s2[j])

        for i in range(len_s1-1, -1, -1):
            for j in range(len_s2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j]+ord(s1[i]) ,dp[i][j+1]+ord(s2[j]))
        # for i in range(len_s1+1):
        #     print(dp[i])
        return dp[0][0]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        the logic of this solution is more straight forward, find the max ascii longest common sequence, then delete it from the total sequence of s1 and s2.
        """
        len_s1, len_s2 = len(s1), len(s2)
        dp = [[0]*(len_s2+1) for _ in range(len_s1+1)]
        for i in range(len_s1):
            for j in range(len_s2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + 2*ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        # for i in range(len_s1+1):
        #     print(dp[i])
        s1_ord = sum([ord(s) for s in s1])
        s2_ord = sum([ord(s) for s in s2])
        return s1_ord + s2_ord - dp[len_s1][len_s2]



s = Solution()
s1 = "delete"
s2 = "leet"
print(s.minimumDeleteSum(s1, s2))

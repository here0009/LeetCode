"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)
        if w1 == 0 or w2 == 0:
            return w1 if w1 != 0 else w2
        print(abs(w1-w2))
        dp = [[0] * w2 for _ in range(w1)]

        row_dist, col_dist = 1, 1
        for i in range(w1):  # initialise 1st col
            if col_dist and word1[i] == word2[0]:
                col_dist = 0
            dp[i][0] = i + col_dist
        for j in range(w2):  # initialise 1st row
            if row_dist and word1[0] == word2[j]:
                row_dist = 0
            dp[0][j] = j + row_dist

        for i in range(1, w1):
            for j in range(1, w2):
                min_dist = abs(i-j)
                tmp = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + (word1[i] != word2[j])
                dp[i][j] = max(tmp, min_dist)
        print('\t'.join(['matrix'] +list(word2)))
        for i in range(w1):
            print('\t'.join([word1[i]]+[str(k) for k in dp[i]]))
        return dp[-1][-1]


class Solution_1:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)
        if w1 == 0 or w2 == 0:
            return w1 if w1 != 0 else w2
        # print(abs(w1-w2))
        dp = [[0] * w2 for _ in range(w1)]

        row_dist, col_dist = 1, 1
        for i in range(w1):  # initialise 1st col
            if col_dist and word1[i] == word2[0]:
                col_dist = 0
            dp[i][0] = i + col_dist
        for j in range(w2):  # initialise 1st row
            if row_dist and word1[0] == word2[j]:
                row_dist = 0
            dp[0][j] = j + row_dist

        for i in range(1, w1):
            for j in range(1, w2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1)+1, len(word2)+1
        if w1 == 1 or w2 == 1:
            return w1-1 if w1 != 1 else w2-1
        dp = [[0] * w2 for _ in range(w1)]
        for i in range(w1):  # initialise 1st col
            dp[i][0] = i
        for j in range(w2):  # initialise 1st row
            dp[0][j] = j
        for i in range(1,w1):
            for j in range(1,w2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]


from functools import lru_cache
class Solution:
    def minDistance(self, word1, word2):
        @lru_cache(None)
        def dfs(word1, word2, i, j):
            """Memoized solution"""
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                ans = dfs(word1, word2, i + 1, j + 1)
            else: 
                insert = 1 + dfs(word1, word2, i, j + 1)
                delete = 1 + dfs(word1, word2, i + 1, j)
                replace = 1 + dfs(word1, word2, i + 1, j + 1)
                ans = min(insert, delete, replace)
            return ans
    
        return dfs(word1, word2, 0, 0)

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)  # switch word1 and word2 if m < n to ensure n ≤ m
        curr = list(range(n+1))
        for i in range(m):
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                curr[j+1] = prev[j] if word1[i] == word2[j] else min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]
S = Solution()
word1 = "horse"
word2 = "ros"
print(S.minDistance(word1, word2))
word1 = "intention"
word2 = "execution"
print(S.minDistance(word1, word2))
word1 = ""
word2 = ""
print(S.minDistance(word1, word2))
word1 = "a"
word2 = "ab"
print(S.minDistance(word1, word2))

word1 ="zoologicoarchaeologist"
word2 = "zoogeologist"
print(S.minDistance(word1, word2))

word1 ="zoologicoarchaeologist"
word2 ="zoopsychologist"
print(S.minDistance(word1, word2))

"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
Example 3:

Input: words = ["abcd"], target = "abcd"
Output: 1
Example 4:

Input: words = ["abab","baba","abba","baab"], target = "abba"
Output: 16
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
"""


from collections import defaultdict
from functools import lru_cache
class Solution:
    def numWays(self, words, target: str) -> int:
        """
        TLE
        """

        @lru_cache(None)
        def dfs(n, limit):
            if n == len_t:
                return 1
            if limit >= C:
                return 0
            res = 0
            v = target[n]
            for i, j in matrix[v]:
                if j >= limit:
                    res += dfs(n+1, j+1)
            return res % M 

        M = 10**9+7
        len_t = len(target)
        R, C = len(words), len(words[0])
        matrix = defaultdict(list)
        for i in range(R):
            for j in range(C):
                matrix[words[i][j]].append((i,j))
        # print(matrix)
        # self.res = 0
        return dfs(0, 0) % M


from collections import defaultdict
from functools import lru_cache
from collections import Counter
class Solution:
    def numWays(self, words, target: str) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(n, limit):
            if n == len_t:
                return 1
            if limit >= C:
                return 0
            res = 0
            v = target[n]
            for j, c in matrix[v].items():
                if j >= limit:
                    res += c*dfs(n+1, j+1)
            return res % M

        M = 10**9+7
        len_t = len(target)
        R, C = len(words), len(words[0])
        matrix = defaultdict(Counter)
        for i in range(R):
            for j in range(C):
                matrix[words[i][j]][j] += 1
        # print(matrix)
        # self.res = 0
        return dfs(0, 0) % M


from collections import defaultdict
from functools import lru_cache
from collections import Counter
from bisect import bisect_left
class Solution:
    def numWays(self, words, target: str) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(n, limit):
            if n == len_t:
                return 1
            if limit >= C:
                return 0
            res = 0
            v = target[n]
            if v not in matrix:
                return 0
            index = bisect_left(matrix[v], (limit, 0))
            for j, c in matrix[v][index:]:
                res += c*dfs(n+1, j+1)
            return res % M

        M = 10**9+7
        len_t = len(target)
        R, C = len(words), len(words[0])
        matrix = defaultdict(Counter)
        for i in range(R):
            for j in range(C):
                matrix[words[i][j]][j] += 1
        for key,counter in matrix.items():
            matrix[key] = sorted((k,v) for k,v in counter.items())
        # print(matrix)
        return dfs(0, 0) % M


# 作者：GiaoGiaoWo
# 链接：https://leetcode-cn.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/solution/huan-xing-by-giaogiaowo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import Counter
class Solution:
    def numWays(self, words, target: str) -> int:
        @lru_cache(None)
        def dfs(cur, t):
            if len(t) > length - cur:
                return 0
            if not t:
                return 1
            return (dfs(cur+1, t) + counts[cur][t[0]] * dfs(cur+1, t[1:])) % M

        counts = []
        length = len(words[0])
        for i in range(length):
            counts.append(Counter(words[j][i] for j in range(len(words))))

        M = 10**9 + 7
        return dfs(0, target)


from collections import Counter
from functools import lru_cache
class Solution:
    def numWays(self, words, target: str) -> int:
        """
        instead of store letters : [indexs]
        we store index : Counter of letters, which is more convinient to use, beacuse, we traverse along with the index of word
        """
        @lru_cache(None)
        def dp(jw, jt):
            if len_w - jw < len_t - jt:
                return 0
            if jt == len_t:
                return 1
            res = dp(jw+1, jt) + counts[jw][target[jt]]*dp(jw+1, jt+1)
            return res % M

        length = len(words)
        len_w, len_t = len(words[0]), len(target)
        counts = []
        for j in range(len_w):
            counts.append(Counter(words[i][j] for i in range(length)))
        M = 10**9+7
        return dp(0,0)

class Solution:
    def numWays(self, words, target):
        n, mod = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % mod
        return res[n] % mod

S = Solution()
words = ["acca","bbbb","caca"]
target = "aba"
print(S.numWays(words, target))
words = ["abba","baab"]
target = "bab"
print(S.numWays(words, target))
words = ["abcd"]
target = "abcd"
print(S.numWays(words, target))
words = ["abab","baba","abba","baab"]
target = "abba"
print(S.numWays(words, target))
words = ["ddcc","bdcb","bdbb"]
target = "bab"
print(S.numWays(words, target))
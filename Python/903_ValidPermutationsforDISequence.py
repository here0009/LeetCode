"""
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

 

Example 1:

Input: "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
 

Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
"""


class Solution:
    """
    TLE
    """
    def numPermsDISequence(self, S: str) -> int:
        def dfs(index, num):
            # print(index, num)
            if index == n-1:
                self.res += 1
            for i in range(n):
                if visited[i] == 0:
                    if (S[index] == 'D' and i < num) or (S[index] == 'I' and i > num):
                        visited[i] = 1
                        dfs(index+1, i)
                        visited[i] = 0

        self.res = 0
        n = len(S) + 1
        visited = [0]*n
        for i in range(n):
            visited[i] = 1
            dfs(0, i)
            visited[i] = 0

        M = 10**9_7
        return self.res % M


from functools import lru_cache
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dfs(index, status, pre):
            print(index, status, pre)
            if index == n:
                return 1
            res = 0
            for i in range(n + 1):
                if status & (1 << i) == 0:
                    if (S[index] == 'D' and i < pre) or (S[index] == 'I' and i > pre):
                        s2 = status | (1 << i)
                        res += dfs(index + 1, s2, i)
            return res % M

        n = len(S)
        M = 10**9 + 7
        res = 0
        for i in range(n + 1):
            res += dfs(0, 1 << i, i)
        return res % M


from functools import lru_cache
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        """
        we can minimize the steps taking account of the continue 'D' and 'I'
        """
        @lru_cache(None)
        def dfs(index, status, pre):
            print(index, status, pre)
            if index == n:
                return 1
            res = 0
            i = index + 1
            while i < n and S[i] == S[index]:
                i += 1
            k = i - index
            if S[index] == 'D':
                lst = lst[:k]
            else:
                lst = status[:-k]
            for j in lst:
                s2 = status[k]
                res += dfs(index + 1, s2, i)
            return res % M

        n = len(S)
        M = 10**9 + 7
        res = 0
        status = tuple(range(n + 1))
        for i in range(n + 1):
            res += dfs(0, status, i)
        return res % M





class Solution_2:
    def numPermsDISequence(self, S: str) -> int:
        M = 10**9 + 7
        len_s = len(S)
        dp = [1] * (len_s + 1)
        for c in S:
            if c == 'D':  # the lst element can not be used., dp[i] += dp[i + 1], add from last to 1st
                dp = dp[1:]
                for i in range(len(dp) - 2, -1, -1) :
                    dp[i] += dp[i + 1]
            else:
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
        return dp[0] % M


class Solution_1:
     def numPermsDISequence(self, S):
            dp = [1] * (len(S) + 1)
            for c in S:
                if c == "I":
                    dp = dp[:-1]
                    for i in range(1, len(dp)):
                        dp[i] += dp[i - 1]
                else:
                    dp = dp[1:]
                    for i in range(len(dp) - 1)[::-1]:
                        dp[i] += dp[i + 1]
            return dp[0] % (10**9 + 7)


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        """
        Thoughts: 
        N = len(S) + 1
        eventualy, we will generate a sequence of whose length equal to N
        at the beiginning, we got N possible candidates : 0 ~ N - 1
        if S[0] is 'D', then 0 can not be used.
        elif S[0] is 'I', N - 1 can not be used.
        the following steps are similar, every time we encounter an 'D' the element at the beginning can not be used and vice versa
        """
        M = 10**9 + 7
        len_s = len(S)
        dp = [1] * (len_s + 1)
        for c in S:
            if c == 'D':  # the lst element can not be used., dp[i] += dp[i + 1], add from last to 1st
                dp2 = [dp[-1]]
                for i in range(len(dp) - 2, 0, -1):
                    dp2.append((dp2[-1] + dp[i]) % M)
                dp = dp2[::-1]
            else:
                dp2 = [dp[0]]  # the last element can not be used.
                for i in range(1, len(dp) - 1):
                    dp2.append((dp2[-1] + dp[i]) % M)
                dp = dp2
        return dp[0] % M

slt = Solution()
S = "DID"
print(slt.numPermsDISequence(S))
S = "IDDDIID"
print(slt.numPermsDISequence(S))
S = "IDDDIIDIIIIIIIIDIDID"
print(slt.numPermsDISequence(S))
"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""


from functools import lru_cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        @lru_cache(maxsize=10**6)
        def canGet(idx):
            if idx == 0:
                return True
            if s[idx] == '1':
                return False
            for k in range(minJump, maxJump + 1):
                if idx - k >= 0:
                    if canGet(idx - k):
                        return True
                else:
                    break
            return False

        return canGet(len(s) - 1)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        def canGet(idx):
            if idx in memo:
                return memo[idx]
            memo[idx] = False
            if s[idx] == '1':
                return memo[idx]
            for k in range(minJump, maxJump + 1):
                if idx - k >= 0:
                    if canGet(idx - k):
                        memo[idx] = True
                        break
                else:
                    break
            return memo[idx]

        memo = dict()
        memo[0] = True
        return canGet(len(s) - 1)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[-1] == '1':
            return False
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        for i in range(length):
            if dp[i] == 1:
                for k in range(minJump, maxJump + 1):
                    if i + k >= length:
                        break
                    if s[i + k] == '0':
                        dp[i + k] = 1
        return dp[-1] == 1


from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        dq = deque([0])
        visited = set([0])
        pre_max = 0
        length = len(s)
        while dq:
            idx = dq.popleft()
            if idx == length - 1:
                return True
            left = max(pre_max + 1, idx + minJump)
            right = min(length, idx + maxJump + 1)
            for j in range(left, right):
                if s[j] == '0' and j not in visited:
                    visited.add(j)
                    dq.append(j)
            pre_max = max(pre_max, idx + maxJump)
        return False


S = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(S.canReach(s, minJump, maxJump))
s = "01101110"
minJump = 2
maxJump = 3
print(S.canReach(s, minJump, maxJump))
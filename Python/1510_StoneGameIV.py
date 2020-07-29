"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.


Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.

Constraints:

1 <= n <= 10^5
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        wrong answer
        """
        steps = []
        i = 1
        while i * i <= n:
            steps.append(i*i)
            i += 1
        # print(steps)
        curr = steps
        flag = 1
        while True:
            curr2 = []
            for c in curr:
                if c == n:
                    return bool(flag)
                for step in steps:
                    if c + step > n:
                        break
                    else:
                        curr2.append(c + step)
            flag = 1 - flag
            curr = curr2


from functools import lru_cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dp(num):
            # print(num)
            if num in steps_set:
                return True
            for step in steps:
                if num - step < 0:
                    continue
                if not dp(num - step):
                    return True
            return False

        steps_set = set()
        steps = []
        i = 1
        while i * i <= n:
            steps.append(i*i)
            steps_set.add(i*i)
            i += 1
        steps = steps[::-1]
        return dp(n)


from functools import lru_cache
import math
class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        # print(n)
        if n == 0:
            return False
        i = int(math.sqrt(n))
        while i > 0:
            if not self.winnerSquareGame(n - i*i):
                return True
            i -= 1
        return False

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [None]*(n+1)
        dp[0] = False
        steps = []
        i = 1
        while i * i <= n:
            steps.append(i*i)
            i += 1
        for i in range(n):
            for step in steps:
                if i + step <= n:
                    if dp[i + step]:
                        continue
                    else:
                        dp[i + step] = (False if dp[i] else True)
            if dp[-1]:
                return True
        return False



class Solution:
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]

S = Solution()
for n in [1,2,4,7,17]:
    print(n, S.winnerSquareGame(n))
print(8, S.winnerSquareGame(8))

n = 92719
print(n, S.winnerSquareGame(n))

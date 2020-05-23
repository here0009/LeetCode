"""
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""
from functools import lru_cache
class Solution:
    def stoneGameII(self, piles) -> int:
        @lru_cache(None)
        def dp(index,M):
            """
            dp(index, self.M) represents the max score that can be got start from index
            """
            if index >= length:
                return 0
            res = -float('inf')
            total = 0
            for step in range(1,2*M+1):
                next_step = max(step, M)
                if index+step > length:
                    break
                res = max(res, acc_piles[-1]-acc_piles[index]-dp(index+step, next_step))
            return res

        length = len(piles)
        acc_piles, curr = [0], 0
        for p in piles:
            curr += p
            acc_piles.append(curr)
        # print(acc_piles)
        return dp(0,1)

S = Solution()
piles = [2,7,9,4,4]
print(S.stoneGameII(piles))
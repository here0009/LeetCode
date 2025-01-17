from typing import List
from functools import lru_cache

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(i:int, j:int, bullets:int):
            if i >= self.row or j >= self.col:
                return float('-inf')
            val = coins[i][j]
            if i == self.row - 1 and j == self.col - 1:
                if bullets > 0:
                    return max(val, 0)
                else:
                    return val
            res = val + max(dfs(i+1, j, bullets), dfs(i, j+1, bullets))
            if val < 0 and bullets > 0:
                res = max(dfs(i+1, j, bullets-1), dfs(i,j+1, bullets-1), res)
            return res
        
        self.row, self.col = len(coins), len(coins[0])
        return dfs(0, 0, 2)

s = Solution()
coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
print(s.maximumAmount(coins))
coins = [[10,10,10],[10,10,10]]
print(s.maximumAmount(coins))
coins = [[-4]]
print(s.maximumAmount(coins))
coins = [[-6,-15,-16,-8],[-10,11,6,16],[1,2,18,12],[15,19,4,17]]
print(s.maximumAmount(coins))

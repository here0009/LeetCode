"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

Example 1:


Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
 

Constraints:

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
"""


from typing import List,Tuple
from functools import lru_cache

# Time Limit Error
class Solution_1:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @lru_cache(maxsize=None)
        def dp(piles_index:Tuple[int], rmd:int):
            if rmd == 0:
                return 0
            res = 0
            for p, i in enumerate(piles_index):
                if i < length_lst[p]:
                    piles_index2 = tuple(list(piles_index[:p]) + [i+1] + list(piles_index[p+1:]))
                    res = max(res, dp(piles_index2, rmd-1) + piles[p][i]) 
            return res
        
        length_lst = [len(lst) for lst in piles]
        length_tuple = tuple([0]*len(piles))
        return dp(length_tuple, k)


class Solution_2:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(piles_index:int, rmd:int):
            if rmd == 0 or piles_index == piles_len:
                return 0
            res = dp(piles_index+1, rmd) # not take current pile
            length = min(length_lst[piles_index], rmd)
            val = 0
            for i in range(length):
                val += piles[piles_index][i]
                res = max(res, dp(piles_index+1, rmd-(i+1)) + val)
            return res
        
        length_lst = [len(lst) for lst in piles]
        piles_len = len(length_lst)
        return dp(0, k)

class Solution_3:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0]*(k+1) for _ in range(len(piles) + 1)]
        for p, pile_lst in enumerate(piles):
            for i in range(1, len(pile_lst)):
                pile_lst[i] += pile_lst[i - 1] # presum
            for j in range(1, k + 1):
                min_len = min(len(pile_lst), j)
                dp[p + 1][j] = max([dp[p][j-w]+v for w,v in enumerate(pile_lst[:min_len], 1)] + [dp[p][j]])
        return dp[-1][-1]

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0]*(k+1)
        for pile_lst in piles:
            for i in range(1, len(pile_lst)):
                pile_lst[i] += pile_lst[i - 1] # presum
            dp2 = [0]*(k+1)
            for j in range(1, k+1):
                min_len = min(len(pile_lst), j)
                dp2[j] = max([dp[j-w]+v for w,v in enumerate(pile_lst[:min_len], 1)] + [dp[j]])
            dp = dp2
        return dp[-1]  
        

s = Solution()
piles = [[1,100,3],[7,8,9]]
k = 2
print(s.maxValueOfCoins(piles, k))
piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
k = 7
print(s.maxValueOfCoins(piles, k))
piles = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]
k = 9
print(s.maxValueOfCoins(piles, k))

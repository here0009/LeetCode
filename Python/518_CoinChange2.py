"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""


from typing import List
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(index, target):
            # print(index, target)
            if target == 0:
                return 1
            if index == len_c:
                return 0
            v = coins[index]
            res = dp(index + 1, target)
            q = 1
            if target - v >= 0:
                res += dp(index, target - v)
            # print('i,t,r', index, target, res)
            return res

        len_c = len(coins)
        return dp(0, amount)

S = Solution()
amount = 5
coins = [1, 2, 5]
print(S.change(amount, coins))

amount = 3
coins = [2]
print(S.change(amount, coins))

amount = 10
coins = [10] 

print(S.change(amount, coins))

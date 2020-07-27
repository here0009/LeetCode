"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


from functools import lru_cache
class Solution:
    def maxProfit(self, prices) -> int:
        @lru_cache(None)
        def dp(start, end):
            if start >= end or end > length:
                return 0
            res = 0
            for i in range(start+1, end):
                if prices[i] > prices[start]:
                    res = max(res, prices[i]-prices[start]+dp(i+2, end))
                else:
                    res = max(res, dp(i, end))
            return res

        length = len(prices)
        return dp(0, length)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75940/5-lines-Python-O(n)-time-O(1)-space

"""
free is the maximum profit I can have while being free to buy. I am free to buy in the current iteration either because I was free to buy in the previous iteration and did nothing in the current iteration, or I was cooling down in the previous iteration and did nothing in the current iteration.
have is the maximum profit I can have while having stock, i.e., I've bought a stock and haven't sold it yet. This happens when I was already holding stock but did not sell in this iteration, or I was free to buy stock last iteration and bought the stock in the current iteration.
cooldown is the maximum profit I can have while cooling down. This only happens if I was holding a stock in the previous iteration and sold it in the current iteration.
"""

class Solution:
    def maxProfit(self, prices) -> int:
        free, have, cooldown = 0, float('-inf'), float('-inf')
        for p in prices:
            free, have, cooldown = max(free, cooldown), max(have, free-p), have+p
        return max(free, cooldown)

S = Solution()
prices = [1,2,3,0,2]
print(S.maxProfit(prices))

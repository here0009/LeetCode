"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res = 0
        if len(prices) < 2:
            return res

        init_price = prices[0]
        pre_price = prices[0]

        for price in prices[1:]:
            # print(index, price)
            if price < pre_price:
                if pre_price - init_price >0:
                    res += pre_price - init_price
                init_price = price
            pre_price = price
        if prices[-1] > init_price:
            res += prices[-1] - init_price
        return res

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
prices = [1,2,3,4,5]
print(s.maxProfit(prices))
prices = [7,6,4,3,1]
print(s.maxProfit(prices))
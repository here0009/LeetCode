"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
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
    def maxProfit(self, prices) -> int:
        """
        wrong answer
        """
        prices.append(float('-inf'))
        profit = [0,0]
        stack = []
        for p in prices:
            if len(stack) > 1 and p < stack[-1]:
                profit.append(stack[-1] - stack[0])
                stack = []
            while stack and p <= stack[-1]:
                stack.pop()
            stack.append(p)
            print(stack)
        profit = sorted(profit, reverse = True)
        print(profit)
        return sum(profit[:2])


class Solution:
    def maxProfit(self, prices) -> int:
        """
        two passes, forward[i] reprsents the most profit can make [0:i]
        backward[i] reprsents the most profit can make in [i:]
        """
        length = len(prices)
        res = 0
        if not prices:
            return 0

        forward = [0]*length
        min_price = prices[0]
        for i in range(1, length):
            forward[i] = max(forward[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        backward = [0]*length
        max_price = prices[-1]
        for i in range(length-2, -1, -1):
            backward[i] = max(backward[i+1], max_price - prices[i])
            max_price = max(max_price, prices[i])

        for i in range(length):
            res = max(res, forward[i] + backward[i])
        # print(forward, backward)
        return res

        
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/405165/python-method-%3A-dynamic-programming-keep-clean
class Solution:
    def maxProfit(self, prices):
        # dynamic programming
        first_buy, first_profit, second_buy_first_porfit, max_profit = float('inf'), 0, float('inf'), 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price-first_buy)
            second_buy_first_porfit = min(second_buy_first_porfit, price-first_profit)
            max_profit = max(max_profit, price-second_buy_first_porfit)
        return max_profit




S = Solution()
prices = [3,3,5,0,0,3,1,4]
print(S.maxProfit(prices))
prices = [1,2,3,4,5]
print(S.maxProfit(prices))
prices = [7,6,4,3,1]
print(S.maxProfit(prices))
prices = [2,1,4]
print(S.maxProfit(prices))
prices = [1,2,4,2,5,7,2,4,9,0]
print(S.maxProfit(prices))
# Output
# 12
# Expected
# 13
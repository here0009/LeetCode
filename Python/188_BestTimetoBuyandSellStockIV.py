"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices or k == 0:
            return 0
        len_p = len(prices)
        if k >= len_p//2:
            return sum(max(p-q, 0) for p,q in zip(prices[1:], prices[:-1]))
        dp_buy = [[-float('inf')]*(k+1) for _ in range(len_p)]
        dp_sell = [[-float('inf')]*(k+1) for _ in range(len_p)]
        dp_sell[0][0] = 0
        dp_buy[0][1] = -prices[0]
        for day in range(1, len_p):
            for t in range(k+1):
                dp_sell[day][t] = max(dp_sell[day-1][t], dp_buy[day-1][t] + prices[day])
                if t > 1:
                    dp_buy[day][t] = max(dp_buy[day-1][t], dp_sell[day-1][t-1] - prices[day])
        for row in dp_buy:
            print(row)
        print('+++++++++++')
        for row in dp_sell:
            print(row)
        return max(dp_sell[-1])


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices or k == 0:
            return 0
        len_p = len(prices)
        if k >= len_p // 2:
            return sum(max(p-q, 0) for p,q in zip(prices[1:], prices[:-1]))
        dp = [[0] * (len_p) for _ in range(k + 1)]  #dp[t][d] stand for the maxprofit we can make on day d through at most t transctions
        for t in range(1, k + 1):
            hold = -prices[0]
            for d in range(1, len_p):
                dp[t][d] = max(dp[t][d - 1], hold + prices[d])
                hold = max(hold, dp[t - 1][d - 1] - prices[d])
        return dp[-1][-1]



S = Solution()
prices = [2,4,1]
k = 2
print(S.maxProfit(k, prices))
prices = [3,2,6,5,0,3]
k = 2
print(S.maxProfit(k, prices))
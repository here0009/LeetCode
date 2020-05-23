"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        res = 0
        buy = prices[0]
        sell = prices[0]
        for p in prices[1:]:
            if p >= sell:
                sell = p
            else:
                if p < buy or (sell-fee > p and  sell-buy-fee > 0): #buy at price p may make profit in the future
                    res += max(0,sell-buy-fee)
                    buy = p
                    sell = p

        res += max(sell-buy-fee, 0)
        return res

class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        res = 0
        buy = prices[0]
        for p in prices[1:]:
            if p < buy:
                buy = p
            elif p - buy > fee:
                res += p-buy-fee
                buy = p-fee #the critical step, we sell at the price of p is equal to we buy at the price p-fee, make profit p-buy-fee so if there is a higher price, we can still sell it.
        return res

class Solution:
    def maxProfit(self, prices, fee: int) -> int:

s = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(s.maxProfit(prices, fee))


prices = [1,3,7,5,10,3]
fee = 3
print(s.maxProfit(prices, fee))
"""
Output
5
Expected
6
"""

prices = [1,4,6,2,8,3,10,14]
fee = 3
print(s.maxProfit(prices, fee))

"""
Output
12
Expected
13
"""

prices =[4,5,2,4,3,3,1,2,5,4]
fee = 1
print(s.maxProfit(prices, fee))
"""
Output
0
Expected
4
"""
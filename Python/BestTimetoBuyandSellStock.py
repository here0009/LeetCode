import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        i,j stood for the left and right bar of prices, if prices[i+1] > prices[i], i++
        if prices[j-1] < prices[j], j--
        max_profit = prices[i] - prices[j] (if it is larger than 0)
        then repeat the process until i meets j
        Wrong Idead:(too many pairs of i and j should be stored and calculated, and their postion reationship should be considered)

        The right one:
        two variable.
        min_val: keep track of the min value meets so far
        max_profit: keep track of the final answer, the max_profit
        """
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price
        return max_profit


prices_list = [7,6,4,3,1,9]
s = Solution()
print(s.maxProfit(prices_list))
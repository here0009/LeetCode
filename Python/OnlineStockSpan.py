"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
 

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
"""
class StockSpanner:

    def __init__(self):
        """
        stock_price record the prices of stock of each day
        stock_spanner record the spanner days of each day
        self.index reocrd the day number
        """
        self.stock_price = [0]
        self.stock_spanner = [0]
        self.index = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.stock_price.append(price)
        self.index += 1
        #the first day
        if self.index == 1: 
            self.stock_spanner.append(1)
            # return self.stock_spanner[self.index]
        #other than the first day
        else:
            tmp = self.index - 1
            if price < self.stock_price[tmp]:
                self.stock_spanner.append(1)
                # return self.stock_spanner[self.index]
            else:
                while (price >= self.stock_price[tmp] and tmp >= 1):
                    # print(price, tmp)
                    tmp -= self.stock_spanner[tmp]
                    #tmp is the postion before the spanning value, for example stock_spanner of 75 is 2, so the postion is 80. current index - position of 80, is the right positon
                self.stock_spanner.append(self.index - tmp)
        return self.stock_spanner[self.index]


"""
Thoughts:
Do not record the price information, cover the price information with spanner, for example, in 
[100, 80, 60, 70, 60, 75, 85], 
use a stack of tuple(price, spanner value) to store the spanner of each day, 
1 for 100,
1 for 80,
1 for 60,
2 for 70
when 60 was smaller than 70, its information was pop out of the stack, and covered by (70, 2), so when the next value >= 70 was compared with it. we can still get the right answer.
"""
            
class StockSpanner_1:

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res       


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()

price_list = [100, 80, 60, 70, 60, 75, 85]
for price in price_list:
    param_1 = obj.next(price)
    print(param_1)
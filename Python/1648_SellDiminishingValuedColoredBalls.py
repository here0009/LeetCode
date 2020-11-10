"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
500000000500000000

Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""


from typing import List
from bisect import bisect_left
class Solution:
    """
    wrong answer
    """
    def maxProfit(self, inventory, orders: int) -> int:
        def calc(start, end):
            """
            sum from start to end
            """
            return (start+end)*(start-end+1)//2

        def check(n):
            index = bisect_left(inventory, n)
            return total - preSum[index] - (length-index)*n >= orders

        length = len(inventory)
        M = 10**9 + 7
        inventory.sort()
        preSum = [0]
        for num in inventory:
            preSum.append(num + preSum[-1])
        total = preSum[-1]
        left, right = 0, inventory[-1]
        while left < right:

            mid = (left + right)//2
            # print(left, right, mid)
            if check(mid):
                left = mid + 1
            else:
                right = mid
        v = left
        
        res = 0
        index = bisect_left(inventory, v)
        # print('inventory',inventory)
        # print('v',v, index)
        for i in range(length-1, index-1, -1):
            start = inventory[i]
            end = max(v, start-orders+1)
            res += calc(start, end)
            orders -= start-end+1
            if orders == 0:
                return res % M
        return res % M


class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        arr=sorted(Counter(inv).items(), reverse=True)+[(0,0)]
        ans, ind, width=0,0,0
        
        while orders>0:
            width += arr[ind][1]
            sell=min(orders, width * (arr[ind][0] - arr[ind+1][0]))
            whole, residual= divmod(sell, width)
            ans += width*(whole*(arr[ind][0]+arr[ind][0]-(whole-1)))//2 + residual*(arr[ind][0]-whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007  


from collections import Counter
class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        counts = Counter(inv)
        vals = sorted([(k,v) for k,v in counts.items()], reverse=True) + [(0,0)]
        length = len(vals)
        index, res, groups = 0, 0, 0
        M = 10**9+7
        while orders > 0 and index < length:
            k,v = vals[index]
            nk, nv = vals[index+1]
            groups += v
            sell = min(orders, groups*(k - nk))
            d, rmd = divmod(sell, groups)  # if rmd != 0, then sell == orders, so the loop will end in this cycle
            res += groups*(k+k-d+1)*d//2 + rmd*(k-d)
            orders -= sell
            index += 1
        return res % M


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % 1_000_000_007
            k += 1     


S = Solution()
inventory = [2,5]
orders = 4
print(S.maxProfit(inventory, orders))
inventory = [3,5]
orders = 6
print(S.maxProfit(inventory, orders))
inventory = [2,8,4,10,6]
orders = 20
print(S.maxProfit(inventory, orders))
inventory = [1000000000]
orders = 1000000000
print(S.maxProfit(inventory, orders))

inventory = [497978859,167261111,483575207,591815159]
orders = 836556809
print(S.maxProfit(inventory, orders))
# 输出：
# 373219332
# 预期：
# 373219333
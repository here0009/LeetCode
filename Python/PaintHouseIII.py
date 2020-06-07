"""
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array houses, an m * n matrix cost and an integer target where:

houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods, if not possible return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5

Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
"""


class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        """
        wrong answer
        """
        def dfs(paint_index, money, curr_color):
            # print(paint_index, money, curr_color)
            if curr_color > target or money > self.res:
                return
            if paint_index == paint_length:
                if curr_color == target:
                    self.res = min(self.res, money)
                    print(houses, money, curr_color, self.res)
                return

            h_index = need_to_paint[paint_index]
            for c in range(1, n+1):
                d_color, d_money = curr_color, money
                if c != houses[h_index-1] and c != houses[next_non_zero_dict[h_index]]:
                    d_color += 1
                d_money += cost[h_index-1][c-1]
                houses[h_index] = c
                dfs(paint_index+1, d_money, d_color)
                houses[h_index] = 0


        # print(houses, cost, target)
        # check the current color of houses
        houses = [float('inf')] + houses + [float('inf')]
        index, colors, money = 1,0,0
        zeros = []
        need_to_paint = []
        next_non_zero_dict = dict()
        while index < m+1 and houses[index] == 0:
            zeros.append(index)
            need_to_paint.append(index)
            index += 1
        if index < m+1:
            pre = houses[index]
            colors = 1
            while zeros:
                next_non_zero_dict[zeros.pop()] = index
        while index < m+1:
            if houses[index] == 0:
                zeros.append(index)
                need_to_paint.append(index)
            elif houses[index] != pre:
                colors += 1
                while zeros:
                    next_non_zero_dict[zeros.pop()] = index
                pre = houses[index]
            index += 1

        # print(colors)
        if colors > target:
            return -1
        # print(zeros)
        paint_length = len(need_to_paint)
        if paint_length == 0:
            if colors == target:
                return 0
            else:
                return -1
        #paint houses
        paint_index = 0
        self.res = float('inf')
        print(colors)
        dfs(paint_index, 0, colors)
        return self.res

#https://leetcode.com/problems/paint-house-iii/discuss/674313/Simple-Python-explanation-and-why-I-prefer-top-down-DP-to-bottom-up

from functools import lru_cache
class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(index, t, p):
            """
            return the min cost with the color of houses[index-1] == p
            """
            if t < 0:
                return float('inf')
            if index == m:
                return 0 if t == 0 else float('inf')
            if houses[index] == 0:
                return min(dfs(index + 1, t - (p != nc), nc) + cost[index][nc - 1] for nc in range(1, n + 1))
            else:
                return dfs(index + 1, t - (p != houses[index]), houses[index])


        res = dfs(0, target, -1)
        return res if res != float('inf') else -1


class Solution:
    def minCost(self, A, cost, m: int, n: int, target: int) -> int:
        dp, dp2 = {(0,0):0}, {}
        for i,a in enumerate(A):
            for cj in (range(1, n+1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target:
                        continue
                    dp2[cj, b2] = min(dp2.get((cj, b2), float('inf')), dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}
        return min([dp[c,b] for c,b in dp if b == target] or [-1])

S = Solution()
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
print(S.minCost(houses, cost, m, n, target))
houses = [0,2,1,2,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
print(S.minCost(houses, cost, m, n, target))
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[1,10],[10,1],[1,10]]
m = 5
n = 2
target = 5
print(S.minCost(houses, cost, m, n, target))
houses = [3,1,2,3]
cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
m = 4
n = 3
target = 3
print(S.minCost(houses, cost, m, n, target))

houses = [0,1,0,0,1,2,0,0,2,1]
cost = [[4,5,2,6],[8,3,2,9],[6,7,3,1],[10,10,2,7],[6,5,2,4],[4,4,3,9],[9,8,3,5],[7,9,10,3],[8,5,9,10],[10,7,4,6]]
m = 10
n = 4
target = 6
print(S.minCost(houses, cost, m, n, target))
# Output:
# 15
# Expected:
# 24

houses =[0,0,0,1]
cost = [[1,5],[4,1],[1,3],[4,4]]
m = 4
n =2
target = 4
print(S.minCost(houses, cost, m, n, target))
# Output
# 3
# Expected
# 12

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        Thoughts
        e.g.
        for sequence as [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        the answer is either ends with 1 or 100, 
        use cost_even and cost odd to record the minCostClimbingStairs ends with even or odd number, the final result is min of cost_even and cost_odd

        hint from leetcode: 
        Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).
        """
        cost = cost[::-1]
        cost_even, cost_odd = cost[0], cost[1]
        for i in range(2, len(cost)):
            if i%2:
                cost_odd = cost[i] + min(cost_even, cost_odd)
            else:
                cost_even = cost[i] + min(cost_even, cost_odd)

s = Solution()
cost = [10, 15, 20]
print(s.minCostClimbingStairs(cost))

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(cost))

cost = [0,1]
print(s.minCostClimbingStairs(cost))

cost = [0,0,1,1]
print(s.minCostClimbingStairs(cost))
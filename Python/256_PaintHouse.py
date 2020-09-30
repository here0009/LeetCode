"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = []
Output: 0
Example 3:

Input: costs = [[7,6,2]]
Output: 2
 

Constraints:

costs.length == n
costs[i].length == 3
0 <= n <= 100
1 <= costs[i][j] <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minCost(self, costs) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = costs[0]
        for i in range(1, n):
            dp2 = []
            dp2.append(costs[i][0] + min(dp[1], dp[2]))
            dp2.append(costs[i][1] + min(dp[0], dp[2]))
            dp2.append(costs[i][2] + min(dp[0], dp[1]))
            dp = dp2
        return min(dp)

S = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(S.minCost(costs))
costs = []
print(S.minCost(costs))
costs = [[7,6,2]]
print(S.minCost(costs))
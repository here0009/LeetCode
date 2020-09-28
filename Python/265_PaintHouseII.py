"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def minCostII(self, costs) -> int:
        @lru_cache(None)
        def dp(i, j):
            # print(i,j)
            """
            return the val at row i, col j
            """
            if i == m-1:
                return costs[i][j]
            return costs[i][j] + min(dp(i+1, nj) for nj in range(n) if nj != j)

        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        return min(dp(0,j) for j in range(n))


class Solution:
    def minCostII(self, costs) -> int:
        def min2(lst):
            """
            return the min elements of lst, except res[min_v_index] = min2
            """
            if len(lst) == 1:
                return lst
            m1, m2, i1, i2 = float('inf'), float('inf'), 0, 0
            for j,v in enumerate(lst):
                if v < m1:
                    m2, i2 = m1, i1
                    m1, i1 = v, j
                elif v < m2:
                    m2, i2 = v, j
            res = [m1]*n
            res[i1] = m2
            return res

        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        dp = min2(costs[0])
        for i in range(1,m):
            dp = min2([costs[i][j] + dp[j] for j in range(n)])  #update costs based on costs, all costs value add min(dp) except the one got the same index with min(dp)
        return min(dp)

S = Solution()
costs = [[1,5,3],[2,9,4]]
print(S.minCostII(costs))
costs = [[8]]
print(S.minCostII(costs))
costs = [[20,19,11,13,12,16,16,17,15,9,5,18],[3,8,15,17,19,8,18,3,11,6,7,12],[15,4,11,1,18,2,10,9,3,6,4,15]]
print(S.minCostII(costs))
# 输出：
# 15
# 预期结果：
# 9
"""
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def waysToChange(self, n: int) -> int:
        @lru_cache(None)
        def split_coin(num, unit_idx):
            if num == 0:
                return 0
            if unit_idx == len_units:
                return 1
            res = 0
            unit = units[unit_idx]
            if unit > num:
                return split_coin(num, unit_idx + 1)
            tmp = num
            while tmp > 0:
                res += split_coin(tmp, unit_idx + 1)
                tmp -= unit
            print(num, unit_idx, res)
            return res % M

        M = 10**9 + 7
        units = [25, 10, 5, 1]
        len_units = len(units)
        return split_coin(n, 0)


# from functools import lru_cache
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0] * (n + 1)  # dp[i] represents ways to split i 
        dp[0] = 1
        coins = [1, 5, 10, 25]
        M = 10**9 + 7
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] = (dp[i] + dp[i - coin]) % M
        return dp[n]

S = Solution()
print(S.waysToChange(1))
print(S.waysToChange(5))
print(S.waysToChange(10))

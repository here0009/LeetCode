"""
You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

 

Example 1:

Input: prob = [0.4], target = 1
Output: 0.40000
Example 2:

Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125
 

Constraints:

1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
Answers will be accepted as correct if they are within 10^-5 of the correct answer.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/toss-strange-coins
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import reduce
from itertools import combinations
class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        """
        TLE
        """
        def mul(a, b):
            return a*b

        tail_prob = [1-p for p in prob]
        total_tail_prob = 1
        for t in tail_prob:
            if t != 0:
                total_tail_prob *= t
        if target == 0:
            return total_tail_prob
        length = len(prob)
        index_list = list(range(len(prob)))
        res = 0
        # print(total_tail_prob)
        for lst in combinations(index_list, target):
            tail = [tail_prob[i] for i in lst if tail_prob[i] != 0]
            head = [prob[i] for i in lst]
            if not head or not tail:
                continue
            res += total_tail_prob/reduce(mul, tail)*reduce(mul, head)
        return res




# 作者：Wzhaooooo
# 链接：https://leetcode-cn.com/problems/toss-strange-coins/solution/dong-tai-gui-hua-by-wzhaooooo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # 动态规划dp[i][j]表示下标从0 - i正面朝上硬币数为j的概率
        # 状态转移:dp[i][j] = dp[i - 1][j] * (1 - prob[i]) + dp[i - 1][j - 1] * prob[i] 
        # dp[len(prob) - 1][target]即为所求
        dp = [[0 for i in range(target + 1)] for i in range(len(prob))]
        # 初始化
        temp = 1
        for i in range(len(prob)):
            temp *= 1 - prob[i]
            dp[i][0] = temp
        if target == 0:
            return dp[-1][0]
        dp[0][1] = prob[0]
        for i in range(1,len(prob)):
            for j in range(1,min(i + 2,target + 1)):
                dp[i][j] = dp[i - 1][j] * (1 - prob[i]) + dp[i - 1][j - 1] * prob[i]
        return dp[len(prob) - 1][target]





# 作者：bu-jian-de-feng-jing
# 链接：https://leetcode-cn.com/problems/toss-strange-coins/solution/python-ji-yi-hua-di-gui-you-hua-cheng-er-wei-dong-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        size = len(prob)
        memo = dict()
        right= [0 for i in range(size)]
        right[-1]=1-prob[-1]
        for i in range(size-1,-1,-1):
            if i==size-1:
                continue
            right[i]=right[i+1]*(1-prob[i])

        def flit(index,n):
            if (index,n) in memo:
                return memo[(index,n)]
            if n==target:
                if index==size:
                    return 1
                return right[index]
            if index==size:
                return 0
            cur1=0
            cur1+=prob[index]*flit(index+1,n+1)
            cur1+=(1-prob[index])*flit(index+1,n)
            memo[(index,n)]=cur1
            return cur1
        return flit(0,0)


class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        """
        dp[i][j] means in prob[:i] there are j heads
        """
        length = len(prob)
        dp = [[0]*(target+1) for _ in range(length+1)]
        dp[0][0] = 1  # no sequence, no head, 100% prob
        for i in range(1, length+1):
            dp[i][0] = dp[i-1][0]*(1-prob[i-1])
        for i in range(1, length+1):
            for j in range(1, min(i+2, target+1)): # only dp[0] ~ dp[j+1] is relative to next line
                dp[i][j] = prob[i-1]*dp[i-1][j-1] + (1-prob[i-1])*dp[i-1][j]
        return dp[-1][-1]

from functools import lru_cache
class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        @lru_cache(None)
        def dp(index, k):
            if k == 0:
                return no_heads[index]
            if length - index < k or index >= length:
                return 0
            return prob[index]*dp(index+1, k-1) + (1-prob[index])*dp(index+1, k)

        length = len(prob)
        no_heads = [1]  # record the probability of no head for prob[i:], we should avoid to use total_prob_no_heads/prob_no_heads[i], for the divisor may be zero.
        tmp = 1
        for p in prob[::-1]:
            tmp *= 1-p
            no_heads.append(tmp)
        no_heads = no_heads[::-1]
        return dp(0, target)


S = Solution()
prob = [0.4]
target = 1
print(S.probabilityOfHeads(prob, target))
prob = [0.5,0.5,0.5,0.5,0.5]
target = 2
print(S.probabilityOfHeads(prob, target))
prob = [0.5,0.5,0.5,0.5,0.5]
target = 0
print(S.probabilityOfHeads(prob, target))

prob = [1,1,1,1,1,1,1,1,1,1]
target = 9
print(S.probabilityOfHeads(prob, target))






"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:

Choose an integer x > 1, and remove the leftmost x stones from the row.
Add the sum of the removed stones' values to the player's score.
Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.

 

Example 1:

Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.
Example 2:

Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.
Example 3:

Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.
 

Constraints:

n == stones.length
2 <= n <= 105
-104 <= stones[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game-viii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from functools import lru_cache
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def maxScore(lst):
            length = len(lst)
            if length == 1:
                return 0, 0
            curr = lst[0]
            diff = sum(lst)
            res = [diff, 0]
            for i in range(1, len(lst) - 1):
                curr += lst[i]
                a, b = maxScore(tuple([curr]) + lst[i + 1:])
                diff2 = curr + b - a
                if diff2 > diff:
                    diff = diff2
                    res = [curr + b, a]
            return res

        a, b = maxScore(tuple(stones))
        return a - b


from typing import List
from functools import lru_cache
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        @lru_cache(None)
        def maxScore(lst):
            length = len(lst)
            if length == 1:
                return 0

            res = sum(lst)
            for i in range(1, len(lst) - 1):
                tmp = maxScore(lst[i + 1:])
                res = max(res, -tmp)
            return res

        return maxScore(tuple(stones))

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        preSum = stones[:]
        for i in range(1, len(preSum)):
            preSum[i] += preSum[i - 1]
        res = preSum[-1]
        for i in range(len(preSum) - 2, 0, -1):
            res = max(res, preSum[i] - res)
        return res


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 1. 每次取走最左边的x个石子，把他们的和放回最左边，前缀和presum[x]不变
        # 2. 位置i的最大收益为i右边最大的 presum[j] - dp[j] 的j
        for i in range(1, len(stones)):
            stones[i] += stones[i-1]

        res = stones[-1]
        for num in stones[-2:0:-1]:
            # 我们取到j，获得presum[j]的分数，对手最多能取dp[j]
            # 或者我们跨过j，获得dp[j]的分数
            res = max(num - res, res)
        return res

# 作者：qubenhao
# 链接：https://leetcode-cn.com/problems/stone-game-viii/solution/python-dong-tai-gui-hua-by-qubenhao-j287/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
S = Solution()
stones = [-1,2,-3,4,-5]
print(S.stoneGameVIII(stones))
stones = [7,-6,5,10,5,-2,-6]
print(S.stoneGameVIII(stones))
stones = [-10,-12]
print(S.stoneGameVIII(stones))

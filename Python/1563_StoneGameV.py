"""
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""


from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j - i == 1:
                return 0
            elif j - i == 2:
                return min(stoneValue[i:i+2])
            res = 0
            for k in range(i+1, j):
                left, right = preSum[k]-preSum[i], preSum[j]-preSum[k]
                if left < right:
                    res = max(res, left + dp(i,k))
                elif left > right:
                    res = max(res, right + dp(k, j))
                else:
                    res = max(res, left + dp(i,k), right + dp(k, j))
            return res

        length = len(stoneValue)
        preSum = [0]
        for v in stoneValue:
            preSum.append(preSum[-1] + v)
        # print(preSum)
        return dp(0, length)

S = Solution()
stoneValue = [6,2,3,4,5,5]
print(S.stoneGameV(stoneValue))
stoneValue = [7,7,7,7,7,7,7]
print(S.stoneGameV(stoneValue))
stoneValue = [4]
print(S.stoneGameV(stoneValue))
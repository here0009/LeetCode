"""
Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

 

Example 1:



Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:



Input: n = 5, m = 8
Output: 5
Example 3:



Input: n = 11, m = 13
Output: 6
 

Constraints:

1 <= n <= 13
1 <= m <= 13
"""


from functools import lru_cache
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        try to fill the rectangle from left to right, from bottom to top
        use a tuple to record the heights of already filled rectangle
        """
        @lru_cache(None)
        def dp(state):
            min_h = min(state)
            if min_h == n:
                return 0
            state = list(state)
            idx = state.index(min_h)
            r_idx = idx
            while r_idx < m and state[r_idx] == state[idx]:
                r_idx += 1
            max_side = min(r_idx - idx, n - min_h)
            res = m * n
            for side_len in range(1, max_side + 1):
                state[idx: idx + side_len] = [min_h + side_len] * side_len
                res = min(res, 1 + dp(tuple(state)))
            return res
        return dp(tuple([0] * m))


from functools import lru_cache
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        try to fill the rectangle from left to right, from bottom to top
        use a tuple to record the heights of already filled rectangle
        similar idea with previous dp solution, far more faster for prunning
        """
        def dfs(heights, moves):
            if moves >= self.res:
                return
            min_h = min(heights)
            if min_h == n:
                self.res = min(self.res, moves)
                return
            idx = heights.index(min_h)
            r_idx = idx
            while r_idx < m and heights[r_idx] == heights[idx]:
                r_idx += 1
            max_side = min(r_idx - idx, n - min_h)
            for side_len in range(max_side, 0, -1):
                h2 = heights[:]
                h2[idx: idx + side_len] = [min_h + side_len] * side_len
                dfs(h2, moves + 1)

        self.res = m * n
        dfs([0] * m, 0)
        return self.res

S = Solution()
n = 2
m = 3
print(S.tilingRectangle(n, m))
n = 5
m = 8
print(S.tilingRectangle(n, m))
n = 11
m = 13
print(S.tilingRectangle(n, m))
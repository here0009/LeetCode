"""Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 


 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/android-unlock-patterns
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def inRange(i,j):
            return 0 <= i < 3 and 0 <= j < 3

        @lru_cache(None)
        def dp(i, steps, status):
            """
            i, j is the current position of the pointer, steps is step that already taken
            """
            res = 0
            if steps > n:
                return 0

            if steps >= m:
                res += 1

            for ni in range(9):
                if status & (1 << ni) == 0:  # not visited before
                    key = tuple(sorted([ni, i]))
                    if key in gaps_dict and status & (1 << gaps_dict[key]) == 0:
                        #i, ni are gapped and the gapped one has not visited before
                        continue
                    new_status = status ^ (1 << ni)
                    res += dp(ni, steps+1, new_status)
            return res

        res = 0
        gaps_dict = dict()  
        gaps_dict[(0,8)] = gaps_dict[(2,6)] = 4 # diaganol and anti-diaganol
        for i in range(3):  # rows and cols
            for j in range(3):
                if inRange(i+2, j):
                    gaps_dict[(i*3+j, (i+2)*3+j)] = (i+1)*3 + j
                if inRange(i, j+2):
                    gaps_dict[(i*3+j), (i*3+j+2)] = i*3+j+1
        # print(gaps_dict)
        for i in range(9):
            res += dp(i, 1, 1<<i)
        return res

S = Solution()
m = 1
n = 1
print(S.numberOfPatterns(m, n))

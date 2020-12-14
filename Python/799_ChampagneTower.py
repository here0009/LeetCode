"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

 

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
 

Constraints:

0 <= poured <= 109
0 <= query_glass <= query_row < 100
"""


from math import comb
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        wrong answer: the top glass may not fullfilled
        """
        i = 0
        while poured - (i+1) >= 0 and i <= query_row:
            poured -= (i+1)
            i += 1
        if i > query_row:
            return 1
        elif i < query_row:
            return 0
        q, rmd = divmod(i+1, 2)
        total = 0
        if rmd:
            total = comb(i, i//2)
        for j in range(i//2+1):
            total += 2*comb(i, j)
        # print(i, poured, total)
        return min(1, poured*comb(i, query_glass)/total)

from functools import lru_cache
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache(None)
        def dp(i,j):
            if i == 0 and j == 0:
                return poured
            if j == 0 or j == i:
                return max(0, dp(i-1, 0)-1)/2 # symetric
            return max(0, (dp(i-1, j-1)-1)/2) + max(0, (dp(i-1, j)-1)/2)

        flow = dp(query_row, query_glass)
        return min(1, max(0, flow))





S = Solution()
poured = 1
query_row = 1
query_glass = 1
print(S.champagneTower(poured, query_row, query_glass))
poured = 2
query_row = 1
query_glass = 1
print(S.champagneTower(poured, query_row, query_glass))
poured = 100000009
query_row = 33
query_glass = 17
print(S.champagneTower(poured, query_row, query_glass))

print(S.champagneTower(10, 4, 2))
poured = 25
query_row =6
query_glass =1
print(S.champagneTower(25,6,1))
# Output
# 0.00000
# Expected
# 0.18750

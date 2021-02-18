"""
You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.

You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

 

Example 1:

Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
 

Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.
"""


from typing import List
from functools import lru_cache
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        try binary search, check if we can get two group of rods of the same length
        try use dp to find the max num we can get of a specific diff value
        """
        @lru_cache(None)
        def dp(diff, index):
            """
            return the max value we can get from rods[index:]  for a specific diff
            """
            if index == len_rods:
                return 0 if diff == 0 else -float('inf')
            v = rods[index]
            return max(v + dp(diff + v, index + 1), dp(diff - v, index + 1), dp(diff, index + 1))

        len_rods = len(rods)
        return dp(0, 0)

S = Solution()
rods = [1,2,3,6]
print(S.tallestBillboard(rods))
rods =[1,2,3,4,5,6]
print(S.tallestBillboard(rods))
rods =[1,2]
print(S.tallestBillboard(rods))
        
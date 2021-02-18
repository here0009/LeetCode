"""
There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick. 
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

 

Example 1:



Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
Example 2:



Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
Example 3:

Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21
Example 4:

Input: slices = [3,1,2]
Output: 3
 

Constraints:

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
"""


from typing import List
from functools import lru_cache
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(lst):
            # print(lst)
            if not lst:
                return 0
            if len(lst) == 3:
                return max(lst)
            res = max(lst[0] + dp(lst[2: -1]), lst[-1] + dp(lst[1:-2]))
            for i in range(1, len(lst) - 1):
                res = max(res, lst[i] + dp(lst[:i - 1] + lst[i + 2:]))
            return res

        return dp(tuple(slices))



from typing import List
from functools import lru_cache
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        k = len(slices) // 3
        we want to choose k elments out of slices, these elements can not be ajacent to each other, and the 1st and last element can not be choosed at the same time.
        so the problem is equal to choose max(dp(0, len(slices) -2, k) and dp(1, len(slices) - 1, k)))
        we kow that in dp(i, j, k), there are total j - i + 1 elment, because we want to choose k elements that are not ajacent to each other, j - i + 1 larger than  2 * (k -1). or it will be impossible.
        """
        @lru_cache(None)
        def dp(i, j, k):
            if j - i + 1 <= 2 * (k - 1):
                return -float('inf')
            if k == 0:
                return 0
            return max(dp(i + 2, j, k - 1) + slices[i], dp(i + 1, j, k))

        len_s = len(slices)
        group = len_s // 3
        return max(dp(0, len_s - 2, group), dp(1, len_s - 1, group))

# for row in dp1:
#     print(row)
# print('=====================')
# for row in dp2:
#     print(row)
from typing import List
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        use bottom up dp to do the calculation
        """
        len_s = len(slices)
        group = len_s // 3
        dp1 = [[0] * (len_s) for _ in range(group + 1)]
        dp2 = [[0] * (len_s) for _ in range(group + 1)]
        for k in range(1, group + 1):
            for i in range(1, len_s):
                if i == 1:
                    dp1[k][1] = slices[i - 1]  # take 1st, not the last
                    dp2[k][1] = slices[i]  # take last, not the 1st
                else:
                    dp1[k][i] = max(dp1[k][i - 1], dp1[k - 1][i - 2] + slices[i - 1])  # take slices[i-1] or not
                    dp2[k][i] = max(dp2[k][i - 1], dp2[k - 1][i - 2] + slices[i])  # take slices[i] or not
        return max(dp1[-1][-1], dp2[-1][-1])

S = Solution()
slices = [1,2,3,4,5,6]
print(S.maxSizeSlices(slices))
slices = [8,9,8,6,1,1]
print(S.maxSizeSlices(slices))
slices = [4,1,2,5,8,3,1,9,7]
print(S.maxSizeSlices(slices))
slices = [3,1,2]
print(S.maxSizeSlices(slices))
slices = [3,9,4,5,3,8,1,10,3,7,2,9,10,2,6,2,9,8,7,10,7,5,1,6,5,8,9,10,6,5,7,7,2,5,3,10,4,3,4]
print(S.maxSizeSlices(slices))
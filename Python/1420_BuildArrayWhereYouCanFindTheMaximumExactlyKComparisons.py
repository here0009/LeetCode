"""
Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
Example 4:

Input: n = 50, m = 100, k = 25
Output: 34549172
Explanation: Don't forget to compute the answer modulo 1000000007
Example 5:

Input: n = 37, m = 17, k = 7
Output: 418930126
 

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
"""


from functools import lru_cache
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m:
            return 0
        M = 10**9 + 7
        # m < n, choose k distinct digits out of m, other n-m digits can be any digit from 1~m

        # m > n, choose k distinct digits out of m,  other n-k digits can be andy digit from 1~m\
        # can not calculate the result directly by a formula, need to use dp
        pass

from functools import lru_cache
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        @lru_cache(None)
        def dp(length, max_num, cost):
            """
            the ways to construc a subarry of length, with max_num and cost
            """
            # the original value if -1, so cost have to be a least 1
            if cost == 0:
                return 0
            if length == 1:
                return 1 if cost == 1 else 0
            res = dp(length-1, max_num, cost)*max_num # max_num have been seen previouse
            for i in range(1, max_num):
                res += dp(length-1, i, cost-1)
            return res % M

        res = 0
        M = 10**9 + 7
        for i in range(1, m+1):
            res += dp(n, i, k)
        return res % M

S = Solution()

n = 2
m = 3
k = 1
print(S.numOfArrays(n, m, k))
n = 5
m = 2
k = 3
print(S.numOfArrays(n, m, k))
n = 9
m = 1
k = 1
print(S.numOfArrays(n, m, k))
n = 50
m = 100
k = 25
print(S.numOfArrays(n, m, k))
n = 37
m = 17
k = 7
print(S.numOfArrays(n, m, k))
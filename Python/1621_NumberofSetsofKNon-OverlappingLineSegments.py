"""
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: 
The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
Example 4:

Input: n = 5, k = 3
Output: 7
Example 5:

Input: n = 3, k = 2
Output: 1

Constraints:

2 <= n <= 1000
1 <= k <= n-1
"""
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/898830/Python-O(N)-Solution-with-Prove
from math import comb
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        choose end-sharing k segements form n points is the same as choose k segments of non-end-sharing k segements from n+k-1 points
        we just point one/remove one extra point after each segement to sepearte them
        """
        return comb(n+k-1, 2*k) % (10**9+7)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        res = 1
        for i in range(1, 2*k+1):
            res *= n+k-i
            res //= i
        return res % (10**9+7)

S = Solution()
n = 4
k = 2
print(S.numberOfSets(n, k))
n = 3
k = 1
print(S.numberOfSets(n, k))
n = 30
k = 7
print(S.numberOfSets(n, k))
n = 5
k = 3
print(S.numberOfSets(n, k))
n = 3
k = 2
print(S.numberOfSets(n, k))
n = 42
k =25
print(S.numberOfSets(n, k))

"""
Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:



Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
Example 2:



Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
Example 3:

Input: houses = [7,4,6,1], k = 1
Output: 8
Example 4:

Input: houses = [3,6,14,10], k = 4
Output: 0
 

Constraints:

n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
Array houses contain unique integers.
"""


from functools import lru_cache
class Solution:
    def minDistance(self, houses, k: int) -> int:
        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == length:
                return 0
            if k == 0 or i == length:
                return float('inf')
            res = float('inf')
            for j in range(i, length):
                res = min(res, costs[i][j] + dp(k-1, j+1)) ## Try to put a mailbox among house[i:j]
            return res


        length = len(houses)
        houses = sorted(houses)
        costs = [[0]*length for _ in range(length)]
        for i in range(length):
            for j in range(i+1, length):
                median = houses[(i+j)//2]
                for t in range(i, j+1):
                    costs[i][j] += abs(houses[t] - median)
                costs[j][i] = costs[i][j]

        return dp(k, 0)

from functools import lru_cache
class Solution:
    def minDistance(self, houses, k: int) -> int:
        @lru_cache(None)
        def dp(k, i):
            if k == length-i:
                return 0
            if k > length-i or k == 0:
                return float('inf')
            res = float('inf')
            for j in range(i, length):
                res = min(res, costs[i][j] + dp(k-1, j+1)) ## Try to put a mailbox among house[i:j]
            return res


        length = len(houses)
        houses = sorted(houses)
        costs = [[0]*length for _ in range(length)]
        for i in range(length):
            for j in range(i+1, length):
                median = houses[(i+j)//2]
                for t in range(i, j+1):
                    costs[i][j] += abs(houses[t] - median)
                costs[j][i] = costs[i][j]

        return dp(k, 0)


S = Solution()
houses = [1,4,8,10,20]
k = 3
print(S.minDistance(houses, k))
houses = [2,3,5,12,18]
k = 2
print(S.minDistance(houses, k))
houses = [7,4,6,1]
k = 1
print(S.minDistance(houses, k))
houses = [3,6,14,10]
k = 4
print(S.minDistance(houses, k))
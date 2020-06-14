"""
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
Example 4:

Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.
Example 5:

Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9
 

Constraints:

bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
"""


from functools import lru_cache
class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(left, right, group):
            if group == 0:
                return 0
            if right - left < k * group:
                # print(left, right, group, 'k-inf')
                return float('inf')

            elif right - left == k * group:
                # print(left, right, group, max(bloomDay[left: right]))
                return max(bloomDay[left: right])
            else:
                res = float('inf')
                g = 0
                while group - g >= 0:
                    for mid in range(left + 1, right):
                        x = dp(left, mid, g)
                        y = dp(mid, right, group - g)
                        if x == float('inf'):
                            continue
                        if y == float('inf'):
                            break
                            res = min(res, max(x, y))
                        # g += 1
                # print(left, right, group, res, 'p')
                return res
        res = dp(0, len(bloomDay), m)
        # print(dp(0, 3, 1))

        return -1 if res == float('inf') else res


from functools import lru_cache
class Solution_1:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        @lru_cache(None)
        def dp(left, right, group):
            if group == 0:
                return 0
            if right - left < k * group:
                # print(left, right, group, 'k-inf')
                return float('inf')

            elif right - left == k * group:
                # print(left, right, group, max(bloomDay[left: right]))
                return max(bloomDay[left: right])
            else:
                res = float('inf')
                start = 0
                while start + k*group < right:
                    res = min(res, dp(start, start + k*group, group))
                    start += 1

                g = 1
                while group - g >= 0:
                    for mid in range(left + 1, right):
                        x = dp(left, mid, g)
                        y = dp(mid, right, group - g)
                        if x == float('inf') or y == float('inf'):
                            continue
                        res = min(res, max(x, y))
                    g += 1
                # print(left, right, group, res, 'p')
                return res
        res = dp(0, len(bloomDay), m)
        # print(dp(0, 3, 1))

        return -1 if res == float('inf') else res

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686415/Python-Concise-and-easy-python-binary-search
class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def check(n):
            currSize, res = 0, 0
            for b in bloomDay:
                if b <= n:
                    currSize += 1
                else:
                    res += currSize //k
                    currSize = 0
            res += currSize // k
            return res

        if len(bloomDay) < k * m:
            return -1
        left, right = 0, max(bloomDay)
        while left < right:
            mid = (left + right) //2
            if check(mid) < m:
                left = mid + 1
            else:
                right = mid
        return left

S = Solution()
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(S.minDays(bloomDay, m, k))
bloomDay = [1,10,3,10,2]
m = 3
k = 2
print(S.minDays(bloomDay, m, k))
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(S.minDays(bloomDay, m, k))
bloomDay = [1000000000,1000000000]
m = 1
k = 1
print(S.minDays(bloomDay, m, k))
bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2
print(S.minDays(bloomDay, m, k))
bloomDay =[62,75,98,63,47,65,51,87,22,27,73,92,76,44,13,90,100,85]
m = 2
k = 7
print(S.minDays(bloomDay, m, k))
# Output:
# 100
# Expected:
# 98
"""
TLE
"""
bloomDay =[11,9,48,24,77,52,31,19,28,34,54,7,54,75,34,7,2,58,96,19,76,21,64,27,10,16,49,73,7,19,61,39,68,51,48,27,25,97,86,76,88,96,32,100,38,94,64,77,6,7,30,52,25,91,30,59,30,38,26,58,66,32,8,77,81,68,14,12,12,14,60,41,37,14,66,97,56,15,37,18,3,9,2,77,84,77,10,61,27,95,98,20,22,24,45,96,42]
m = 7
k = 13
print(S.minDays(bloomDay, m, k))


bloomDay =[5,37,55,92,22,52,31,62,99,64,92,53,34,84,93,50,28]
m = 8
k = 2
print(S.minDays(bloomDay, m, k))
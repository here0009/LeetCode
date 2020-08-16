"""
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

 

Example 1:

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
Example 2:

Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
Example 3:

Input: n = 1
Output: 1
Example 4:

Input: n = 56
Output: 6
 

Constraints:

1 <= n <= 2*10^9
"""


class Solution:
    def minDays(self, n: int) -> int:
        """
        TLE
        """
        bfs = {0}
        res = 0
        visited = {0}
        while bfs:
            if n in bfs:
                return res
            # print(bfs)
            bfs2 = set()
            visited |= bfs
            for node in bfs:
                nums = [node + 1, node * 2, node*3]
                # if node % 2 == 0:
                #     nums.append()
                for num in nums:
                    if num not in visited:
                        bfs2.add(num)
            else:
                bfs = bfs2
                res += 1

from functools import lru_cache
class Solution:
    def minDays(self, num: int) -> int:
        """
        RecursionError: maximum recursion depth exceeded
        """
        @lru_cache(None)
        def dp(n):
            # print(n)
            if n == 0:
                return 0
            res = [dp(n-1)]
            if n % 2 == 0:
                res.append(dp(n//2))
            if n % 3 == 0:
                res.append(dp(n//3))
            return min(res) + 1
        return dp(num)


from functools import lru_cache
class Solution:
    def minDays(self, num: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return n
            return 1 + min(n%2 + dp(n//2), n % 3 + dp(n//3))
        return dp(num)


class Solution:
    def minDays(self, n: int) -> int:
        ans = 1
        bfs = [n]
        seen = set()
        while bfs: #bfs 
            bfs2 = []
            for x in bfs: 
                if x == 1: return ans 
                seen.add(x)
                if x-1 not in seen: bfs2.append(x-1)
                if x % 2 == 0 and x//2 not in seen: bfs2.append(x//2)
                if x % 3 == 0 and x//3 not in seen: bfs2.append(x//3)
            ans += 1
            bfs = bfs2 

S = Solution()
n = 10
print(S.minDays(n))
n = 6
print(S.minDays(n))
n = 1
print(S.minDays(n))
n = 56
print(S.minDays(n))
n = 820592
print(S.minDays(n))
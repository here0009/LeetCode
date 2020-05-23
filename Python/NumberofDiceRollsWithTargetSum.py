"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""
from collections import defaultdict
class Solution_1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 or target == 0 or f == 0:
            return 0
        if target < d or target > d*f:
            return 0
        M = 10**9+7
        dp_dict = {i:1 for i in range(1,f+1)}
        while d > 1:
            dp_dict_2 = defaultdict(int)
            for num in range(1,f+1):
                for key,v in dp_dict.items():
                    dp_dict_2[key+num] = (dp_dict_2[key+num] + v) % M
            dp_dict = dp_dict_2
            d -= 1
        return dp_dict[target]


from functools import lru_cache
class Solution_2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def roll(d,target):
            if target < d or target > d*f:
                return 0
            if target == 0 and d == 0:
                return 1
            return sum(roll(d-1, target-face) for face in range(1,f+1)) % (10**9+7)
        return roll(d,target)



class Solution_3:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        def roll(d,target):
            if target < d or target > d*f:
                return 0
            if target == 0 and d == 0:
                return 1
            if (d,target) in cache_dict:
                return cache_dict[(d,target)]
            res = sum(roll(d-1, target-face) for face in range(1,f+1)) % (10**9+7)
            cache_dict[(d,target)] = res
            return res

        cache_dict = dict()
        return roll(d,target)


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 or target == 0 or f == 0:
            return 0
        if target < d or target > d*f:
            return 0
        M = 10**9+7
        dp = [0]*(target+1)
        dp[0] = 1
        cycle = 1
        while cycle <= d:
            upper_bound = min(target, cycle*f)
            dp2 = [0]*(target+1)
            for key in range(upper_bound, cycle-1, -1):
                for num in range(1,f+1):
                    if num > key:
                        break
                    dp2[key] += dp[key-num]
            cycle += 1
            dp = dp2
        return dp[target] % M



s = Solution()
d = 1
f = 6
target = 3
print(s.numRollsToTarget(d,f,target))
d = 2
f = 6
target = 7
print(s.numRollsToTarget(d,f,target))
d = 2
f = 5
target = 10
print(s.numRollsToTarget(d,f,target))
d = 1
f = 2
target = 3
print(s.numRollsToTarget(d,f,target))
d = 30
f = 30
target = 500
print(s.numRollsToTarget(d,f,target))
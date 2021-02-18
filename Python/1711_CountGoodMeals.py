"""
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.

 

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 

Constraints:

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220
"""


from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        wrong answer
        """
        counts = Counter(deliciousness)
        keys = sorted(counts.keys())
        print(list([(k, counts[k]) for k in keys]))
        M = 10**9 + 7
        res = 0

        # for key in keys:
        #     val = counts[key]
        for key, val in counts.items():
            bit_key = bin(key)[2:]
            bit_len = len(bit_key)
            max_limit = 2**bit_len
            # print(key, max_limit, max_limit//2)
            if key == max_limit // 2:
                res = (res + val * (val - 1) // 2) % M
                # if 0 in counts and key != 0:
                #     res = (res + val * counts[0]) % M

                if key > 0 and 0 in counts:
                    res = (res + val * counts[0]) % M

            rmd = max_limit - key
            if rmd in counts and rmd != key:
                res = (res + val * counts[rmd]) % M

        return res


from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts = Counter(deliciousness)
        M = 10**9 + 7
        res = 0
        limit = len(bin(max(deliciousness))) - 1
        for key, val in counts.items():
            for j in range(limit, -1, -1):
                rmd = (1 << j) - key
                if rmd < 0:
                    break
                if rmd in counts:
                    if rmd != key:
                        res += val * counts[rmd]
                    else:
                        res += val * (val - 1)
        res = res // 2 % M
        return res

from typing import List
from collections import defaultdict
class Solution_1:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts = defaultdict(int)
        M = 10**9 + 7
        res = 0
        for v in deliciousness:
            for j in range(22):
                res += counts[(1 << j) - v]
            counts[v] += 1
        return res % M


S = Solution()
deliciousness = [1,3,5,7,9]
print(S.countPairs(deliciousness))
deliciousness = [1,1,1,3,3,3,7]
print(S.countPairs(deliciousness))
deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]
print(S.countPairs(deliciousness))
# 输出：
# 10
# 预期：
# 12
deliciousness = [2,14,11,5,1744,2352,0,1,1300,2796,0,4,376,1672,73,55,2006,42,10,6,0,2,2,0,0,1,0,1,0,2,271,241,1,63,1117,931,3,5,378,646,2,0,2,0,15,1]
# print(S.countPairs(deliciousness))
# 输出：
# 65
# 预期结果：
# 174
deliciousness = [0, 1]
print(S.countPairs(deliciousness))
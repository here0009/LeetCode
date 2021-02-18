"""
There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.
Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats
(3,5), (5,3), (1,3) and (1,5)
Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.
Example 4:

Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
Output: 111
 

Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.
"""


from typing import List
from functools import lru_cache
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """
        TLE 50 / 65 test cases passed.
        """
        @lru_cache(None)
        def dp(index, status):
            if index == len_hats:
                return 1
            res = 0
            for j in hats[index]:
                if (1 << j) & status == 0:
                    s2 = status | (1 << j)
                    res += dp(index + 1, s2)
            return res % M

        M = 10**9 + 7
        len_hats = len(hats)
        return dp(0, 0)


from typing import List
from functools import lru_cache
from collections import defaultdict
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """
        try to use people as status, let the hat choose people
        """
        @lru_cache(None)
        def dp(index, status):
            # print(index, status)
            # res = (status == target) 
            if index == len_h:
                return status == target
            res = dp(index + 1, status)
            people = h_dict[hat_keys[index]]
            for p in people:
                if (1 << p) & status == 0:
                    s2 = status | (1 << p)
                    res += dp(index + 1, s2)
            return res % M

        M = 10**9 + 7
        h_dict = defaultdict(list)
        for p, lst in enumerate(hats):
            for h in lst:
                h_dict[h].append(p)
        hat_keys = list(h_dict.keys())
        hat_keys.sort(key=lambda x: len(h_dict[x]))  # put the hat got less choice 1st
        # print(h_dict, hat_keys)
        len_h = len(hat_keys)
        target = (1 << len(hats)) - 1

        return dp(0, 0)

S = Solution()
hats = [[3,4],[4,5],[5]]
print(S.numberWays(hats))
hats = [[3,5,1],[3,5]]
print(S.numberWays(hats))
hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(S.numberWays(hats))
hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
print(S.numberWays(hats))
hats = [[2,6,8,9,10,11,16,17,19,21,23,25],[1,3,6,7,8,9,10,11,12,13,14,19,20,22,23,25],[1,3,4,6,7,8,10,12,13,15,16,17,19,20,22],[2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,20,23,25],[1,4,5,8,12,14,15,16,19,22,24,25],[1,2,3,4,7,8,9,11,12,13,16,17,18,19,22,24,25],[1,2,3,4,10,12,14,17,18,20,21,22,23,24],[2,14,17,22]]
print(S.numberWays(hats))
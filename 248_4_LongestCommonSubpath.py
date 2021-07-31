"""
There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that path.

 

Example 1:

Input: n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3].
Example 2:

Input: n = 3, paths = [[0],[1],[2]]
Output: 0
Explanation: There is no common subpath shared by the three paths.
Example 3:

Input: n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]
Output: 1
Explanation: The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.
 

Constraints:

1 <= n <= 105
m == paths.length
2 <= m <= 105
sum(paths[i].length) <= 105
0 <= paths[i][j] < n
The same city is not listed multiple times consecutively in paths[i].
"""


from typing import List
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        """
        TLE
        """

        def get_sub_paths(path, len_p):
            res = set()
            for i in range(len(path) - len_p + 1):
                res.add(tuple(path[i : len_p + i]))
            # print(path, len_p, res)
            return res

        def check(len_p):
            # print(len_p)
            if len_p == 0:
                return True
            if len_p == min_len + 1:
                return False
            path_set = get_sub_paths(paths[0], len_p)
            for path in paths[1:]:
                path_set &= get_sub_paths(path, len_p)
                if not path_set:
                    return False
            return True

        min_len = min([len(p) for p in paths])
        left, right = 0, min_len + 1
        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

from typing import List
# from functools import lru_cache
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        # @lru_cache(None)
        def get_sub_paths(path, len_p):
            return set([tuple(path[i : len_p + i]) for i in range(len(path) - len_p + 1)])


        def check(len_p):
            # print(len_p)
            if len_p == 0:
                return True
            if len_p == min_len + 1:
                return False
            path_set = get_sub_paths(paths[0], len_p)
            for path in paths[1:]:
                path_set &= get_sub_paths(path, len_p)
                if not path_set:
                    return False
            return True

        min_len = min([len(p) for p in paths])
        left, right = 0, min_len + 1
        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

S = Solution()
n = 5
paths = [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]
print(S.longestCommonSubpath(n, paths))
n = 3
paths = [[0],[1],[2]]
print(S.longestCommonSubpath(n, paths))
n = 5
paths = [[0,1,2,3,4],[4,3,2,1,0]]
print(S.longestCommonSubpath(n, paths))
n = 5
paths = [[1,2,3,4],[4,1,2,3],[4]]
print(S.longestCommonSubpath(n, paths))
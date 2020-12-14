"""
Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

 

Example 1:



Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
Example 2:



Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6
 

Constraints:

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
The given graph is a directed acyclic graph.
"""


from typing import List
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(status, take, avaliable):
            if status == target:  # all taken
                return 0
            bin_take = bin(take)[2:][::-1]
            for i,v in enumerate(bin_take):
                if v == '1':
                    for j in edges[i]: # the indegree number changed during recursion
                        indegree[j] -= 1
                        if indegree[j] == 0:
                            avaliable |= (1 << j)
                    status |= (1 << i)
                    # print('i, status', i, v, bin(status))
                    # take -= (1 << i)

            lst = [i for i,v in enumerate(bin(avaliable)[2:][::-1]) if v == '1']
            # print(indegree)
            # print(lst)
            if not lst:
                res = 0
            # print('lst', lst, k)
            elif len(lst) <= k:
                res = dp(status, avaliable, 0)
            else:
                res = float('inf')
                for comb in combinations(lst, k):
                    # print(comb)
                    t, a = 0, avaliable
                    for d in comb:
                        t |= (1 << d)
                        a -= (1 << d)
                    res = min(res, dp(status, t, a))
            for i,v in enumerate(bin_take):
                if v == '1':
                    for j in edges[i]: 
                        indegree[j] += 1
            return 1 + res

        self.counts = 0
        edges = defaultdict(list)
        indegree = Counter()
        for i,j in dependencies:
            edges[i].append(j)
            indegree[j] += 1

        courses = set(range(1, n+1))
        start = courses - indegree.keys()
        target = 2**(n+1) - 1
        # print(edges, indegree, start, bin(target))
        avaliable = 0
        for i in start:
            avaliable |= (1 << i)
        # print(bin(avaliable))
        return dp(1, 0, avaliable) - 1# first dp not take courses



from typing import List
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        """
        try to use tuple replace bin
        """

        @lru_cache(None)
        def dp(status, take, avaliable):
            if status == target:  # all taken
                return 0
            bin_take = bin(take)[2:][::-1]
            for i,v in enumerate(bin_take):
                if v == '1':
                    for j in edges[i]: # the indegree number changed during recursion
                        indegree[j] -= 1
                        if indegree[j] == 0:
                            avaliable |= (1 << j)
                    status |= (1 << i)
                    # print('i, status', i, v, bin(status))
                    # take -= (1 << i)

            lst = [i for i,v in enumerate(bin(avaliable)[2:][::-1]) if v == '1']
            # print(indegree)
            # print(lst)
            if not lst:
                res = 0
            # print('lst', lst, k)
            elif len(lst) <= k:
                res = dp(status, avaliable, 0)
            else:
                res = float('inf')
                for comb in combinations(lst, k):
                    # print(comb)
                    t, a = 0, avaliable
                    for d in comb:
                        t |= (1 << d)
                        a -= (1 << d)
                    res = min(res, dp(status, t, a))
            for i,v in enumerate(bin_take):
                if v == '1':
                    for j in edges[i]: 
                        indegree[j] += 1
            return 1 + res

        self.counts = 0
        edges = defaultdict(list)
        indegree = Counter()
        for i,j in dependencies:
            edges[i].append(j)
            indegree[j] += 1

        courses = set(range(1, n+1))
        start = courses - indegree.keys()
        target = 2**(n+1) - 1
        avaliable = 0
        for i in start:
            avaliable |= (1 << i)

        return dp(1, 0, avaliable) - 1# first dp not take courses


# https://leetcode.com/problems/parallel-courses-ii/discuss/708445/Weak-test-case-most-solutions-posted-using-depth-or-outdgree-are-wrong
import collections
import itertools
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        degrees = collections.Counter()
        deps = collections.defaultdict(list)
        for dep, course in dependencies:
            degrees[course] += 1
            deps[dep] += course,

        def process(courses, taken):
            mask = courses
            for course in taken:
                mask |= 1 << course
                for dep in deps[course]:
                    degrees[dep] -= 1

            ans = 1 + count(mask)

            for course in taken:
                for dep in deps[course]:
                    degrees[dep] += 1

            return ans

        @lru_cache(None)
        def count(courses):
            taken = []
            for i in range(1, n+1):
                if courses & (1 << i) or degrees[i] != 0:
                    continue
                taken += i,

            if not taken:
                return 0
            if len(taken) <= k:
                return process(courses, taken)

            return min(process(courses, subset) for subset in itertools.combinations(taken, k))
        return count(0)


S = Solution()
n = 4
dependencies = [[2,1],[3,1],[1,4]]
k = 2
print(S.minNumberOfSemesters(n, dependencies, k))
n = 5
dependencies = [[2,1],[3,1],[4,1],[1,5]]
k = 2
print(S.minNumberOfSemesters(n, dependencies, k))
n = 11
dependencies = []
k = 2
print(S.minNumberOfSemesters(n, dependencies, k))
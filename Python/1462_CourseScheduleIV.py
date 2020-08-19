"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

 

Example 1:


Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.
Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.
Example 3:


Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]
Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]
 

Constraints:

2 <= n <= 100
0 <= prerequisite.length <= (n * (n - 1) / 2)
0 <= prerequisite[i][0], prerequisite[i][1] < n
prerequisite[i][0] != prerequisite[i][1]
The prerequisites graph has no cycles.
The prerequisites graph has no repeated edges.
1 <= queries.length <= 10^4
queries[i][0] != queries[i][1]
"""

from collections import defaultdict
from functools import lru_cache
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        @lru_cache(None)
        def dfs(node):
            res = set()
            for next_node in edges[node]:
                res.add(next_node)
                res |= dfs(next_node)
            return res

        # print("++++++++++")
        # print(n, prerequisites, queries)
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)
        # print(edges)
        nodes_dict = defaultdict(set)
        for node in range(n):
            nodes_dict[node] = dfs(node)
        # print(nodes_dict)
        res = []
        for u, v in queries:
            if v in nodes_dict[u]:
                res.append(True)
            else:
                res.append(False)
        return res


from functools import lru_cache
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        @lru_cache(None)
        def isPre(u, v):
            if u == v:
                return True
            for next_node in edges[u]:
                if isPre(next_node, v):
                    return True
            return False

        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)
        return [isPre(u,v) for u,v in queries]

# https://leetcode.com/problems/course-schedule-iv/discuss/660509/JavaPython-FloydWarshall-Algorithm-Clean-code-O(n3)      
class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        connected = [[False] * n for i in range(n)]
        for i, j in prerequisites:
            connected[i][j] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])
        return [connected[i][j] for i, j in queries]


S = Solution()
n = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
print(S.checkIfPrerequisite(n, prerequisites, queries))
n = 2
prerequisites = []
queries = [[1,0],[0,1]]
print(S.checkIfPrerequisite(n, prerequisites, queries))
n = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
print(S.checkIfPrerequisite(n, prerequisites, queries))
n = 3
prerequisites = [[1,0],[2,0]]
queries = [[0,1],[2,0]]
print(S.checkIfPrerequisite(n, prerequisites, queries))
n = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
print(S.checkIfPrerequisite(n, prerequisites, queries))
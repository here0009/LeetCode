"""
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.

 

Example 1:


Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5
Explantion: Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
Example 2:


Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3
Explantion: Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. 
Example 3:

Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
Output: 4
 

Constraints:

1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n
"""


from collections import Counter
class Solution:
    def maximumRequests(self, n: int, requests) -> int:
        """
        Thoughts: the max cycyle to visit all edges, wrong answer
        """
        def dfs(start, node, path, res):
            if node == start:
                res += path
                self.res = max(res, self.res)
            # print(start, node, path, res)
            for j in range(length):
                s, e = requests[j]
                if visited[j] == 0:
                    visited[j] = 1
                    if s == node:
                        dfs(start, e, path+1, res)
                    else:
                        dfs(s, e, path, res)
                    visited[j] = 0

        length = len(requests)
        visited = [0]*length
        
        self.res = 0
        # visited[0] = 1
        dfs(0, 0, 0, 0)

        # for i in range(length):
        #     
        #     dfs(i, 0, 0, 0)
        #     visited[i] = 0
        return self.res

class Solution:
    def maximumRequests(self, n: int, requests) -> int:
        """
        use bitmask to represent the picked nodes, we can visit all the picked nodes that indegree == outdegree
        """
        def test(mask):
            outdegree = [0]*n
            indegree = [0]*n
            for i in range(length):
                if mask & (1 << i):
                    s, e = requests[i]
                    outdegree[s] += 1
                    indegree[e] += 1
            if outdegree == indegree:
                return sum(indegree)
            else:
                return 0

        length = len(requests)
        comb = 1 << length
        res = 0
        for mask in range(1, comb):
            res = max(res, test(mask))
        return res



class Solution:
    def maximumRequests(self, n, requests):
            nr = len(requests)
            res = 0

            def test(mask):
                outd = [0] * n
                ind = [0] * n
                for k in range(nr):
                    if (1 << k) & mask:
                        outd[requests[k][0]] += 1
                        ind[requests[k][1]] += 1
                return sum(outd) if outd == ind else 0

            for i in range(1 << nr):
                res = max(res, test(i))
            return res

from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests) -> int:
        def access(node):
            for nei in adj[node]:
                if adj[node][nei] > 0:
                    dfs(nei, [node], candidate)
            return

        def dfs(node, stack, candidate):
            if node in visited:
                return
            if node == stack[0]:
                candidate.append(tuple(stack))
                return
            elif node in stack:
                return
            stack.append(node)
            for nei in adj[node]:
                if adj[node][nei] > 0:
                    dfs(nei, stack, candidate)
            stack.pop()
        
        def backtrack(routes, res):
            self.res = max(res, self.res)
            if not routes:
                return
            for i, route in enumerate(routes):
                if i > 0 and route == routes[i-1]:
                    continue
                if all(adj[u][v] > 0 for u, v in zip(route, route[1:] + route[0:1])):
                    for u, v in zip(route, route[1:] + route[0:1]):
                        adj[u][v] -= 1
                    backtrack(routes[:i] + routes[i+1:], res + len(route))
                    for u, v in zip(route, route[1:] + route[0:1]):
                        adj[u][v] += 1

        self.res = 0
        adj = defaultdict(lambda: defaultdict(int))

        for v, w in requests:
            adj[v][w] += 1
        visited = set()
        candidate = []

        for node in range(n):
            access(node)
            visited.add(node)

        routes = []
        # print('+++++++++++++++++')
        # print(n, requests)
        # print(candidate)
        for route in candidate:
            for i in range(min(adj[u][v] for u, v in zip(route, route[1:] + route[0:1]))):
                routes.append(route)
        # print(routes)
        backtrack(routes, 0)
        return self.res

# https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/solution/python-ji-yi-hua-di-gui-jian-dan-gao-ding-by-hao-s/
from functools import lru_cache
class Solution:
    def maximumRequests(self, n: int, requests) -> int:

        # 前i条边选择后让每个点的入度减出度达到stat状态的最多的能选的边数

        @lru_cache(None)
        def dp(i, stat):
            #print(i, stat)
            if i == -1:
                for val in stat:
                    if val != 0:
                        return -1
                return 0

            a, b = requests[i]
            new_stat = list(stat)
            new_stat[a] += 1
            new_stat[b] -= 1
            ret = dp(i-1, tuple(new_stat))

            ans = -1
            if ret != -1:
                ans = max(ret + 1, ans)

            ret = dp(i-1, stat)
            if ret != -1:
                ans = max(ret, ans)

            return ans

        return dp(len(requests)-1, tuple([0]*n))

from functools import lru_cache
class Solution:
    def maximumRequests(self, n: int, requests) -> int:
        @lru_cache(None)
        def dp(i, status):
            # the max value we can get from requests[:i] for a specific status
            if i == length:
                if all(v == 0 for v in status):  # indegree and outdegree are the same
                    return 0
                return -float('inf') # if the final status are not all 0, return -float('inf')

            s, e = requests[i]
            status2 = list(status) #update the status if we choose requests[i]
            status2[s] += 1
            status2[e] -= 1
            choose = dp(i+1, tuple(status2))  # if we choose requests[i], the new status is status2
            no_choose = dp(i+1, status)
            res = max(choose+1, no_choose)  # res is the max value between choose+1 an no_choose 
            return res

        length = len(requests)
        return dp(0, tuple([0]*n))

S = Solution()
n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
print(S.maximumRequests(n, requests))
n = 3
requests = [[0,0],[1,2],[2,1]]
print(S.maximumRequests(n, requests))
n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
print(S.maximumRequests(n, requests))
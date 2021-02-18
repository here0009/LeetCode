"""

User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Hard
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""
"""
    1-2
   /   \
  3     4
   \\   /
   5---6
   |
   7-8
  /   \\
  9---10 

Thoughts:
The following code is not right, 
5-7 is a critical connection, but counter[5] and counter[7] were not 1
class Solution:
    def criticalConnections(self, n, connections):
        counter = {i:0 for i in range(n)}
        for p,q in connections:
            counter[p] += 1
            counter[q] += 1
        nodes = {i for i in counter.keys() if counter[i] == 1}
        # print(nodes)
        res = []
        for p,q in connections:
            if p in nodes or q in nodes:
                res.append([p,q])
        return res

s = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(s.criticalConnections(n, connections))
"""
"""
Thoughts:
the problem should be solved use bridge finding algorithm
"""

# https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation


from typing import List
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        if we can travel along a circle without using an edge twice, then all the edges in the circle is not critical, otherwise it is critical
        """
        def dfs(curr, pre):
            # print(curr, pre)
            if node_id[curr] is None:
                node_id[curr] = self.id
                low_id[curr] = self.id
                self.id += 1
            for nxt in graph[curr]:
                if node_id[nxt] is None:
                    dfs(nxt, curr)
            low_id[curr] = min([low_id[nxt] for nxt in graph[curr] if nxt != pre] + [low_id[curr]])

        graph = defaultdict(list)
        self.id = 0
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
        node_id = [None] * n
        low_id = [None] * n
        dfs(0, None)
        res = []
        for p, q in connections:
            if low_id[p] != low_id[q]:  # that won't work https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation
                res.append([p, q])
        # print(node_id)
        # print(low_id)
        return res



from typing import List
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        if we can travel along a circle without using an edge twice, then all the edges in the circle is not critical, otherwise it is critical
        """
        def dfs(curr, pre):
            if node_id[curr] is None:
                node_id[curr] = self.id
                low_id[curr] = self.id
                self.id += 1
                for nxt in graph[curr]:
                    if node_id[nxt] is None:
                        dfs(nxt, curr)
                low_id[curr] = min([low_id[nxt] for nxt in graph[curr] if nxt != pre] + [node_id[curr]])

        graph = defaultdict(list)
        self.id = 0
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
        node_id = [None] * n
        low_id = [None] * n
        dfs(0, None)
        res = []
        for p, q in connections:
            if low_id[p] > node_id[q] or low_id[q] > node_id[p]:
                res.append([p, q])
        # print(node_id)
        # print(low_id)
        return res


class Solution_1:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.num = 0
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        dfs_num, dfs_low = [None]*n, [None]*n
        
        def dfs(node, parent):
            # already visited
            if dfs_num[node] is not None:return 
            dfs_num[node] = dfs_low[node] = self.num
            self.num += 1
            for neighbor in graph[node]:
                if dfs_num[neighbor] is None:
                    dfs(neighbor, node)
            
            # minimal num in the neignbors, exclude the parent
            dfs_low[node] = min([dfs_num[node]] + [dfs_low[neighbor] for neighbor in graph[node] if neighbor != parent])   
        
        dfs(0, None)
        
        res = []
        for u, v in connections:
            # non bridge
            if dfs_low[u] > dfs_num[v] or dfs_low[v] > dfs_num[u]:
                res.append([u, v])
        return res

s = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(s.criticalConnections(n, connections))

n = 5
connections =[[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]
print(s.criticalConnections(n, connections))

# Output
# [[1,0],[2,0],[3,0],[4,0]]
# Expected
# [[0,1]]
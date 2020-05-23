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
class Solution:
    def criticalConnections(self, n, connections):




s = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(s.criticalConnections(n, connections))
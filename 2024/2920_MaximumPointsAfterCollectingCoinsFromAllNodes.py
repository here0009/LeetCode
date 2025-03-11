"""
There exists an undirected tree rooted at node 0 with n nodes labeled from 0 to n - 1. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given a 0-indexed array coins of size n where coins[i] indicates the number of coins in the vertex i, and an integer k.

Starting from the root, you have to collect all the coins such that the coins at a node can only be collected if the coins of its ancestors have been already collected.

Coins at nodei can be collected in one of the following ways:

Collect all the coins, but you will get coins[i] - k points. If coins[i] - k is negative then you will lose abs(coins[i] - k) points.
Collect all the coins, but you will get floor(coins[i] / 2) points. If this way is used, then for all the nodej present in the subtree of nodei, coins[j] will get reduced to floor(coins[j] / 2).
Return the maximum points you can get after collecting the coins from all the tree nodes.



Example 1:


Input: edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5
Output: 11
Explanation:
Collect all the coins from node 0 using the first way. Total points = 10 - 5 = 5.
Collect all the coins from node 1 using the first way. Total points = 5 + (10 - 5) = 10.
Collect all the coins from node 2 using the second way so coins left at node 3 will be floor(3 / 2) = 1. Total points = 10 + floor(3 / 2) = 11.
Collect all the coins from node 3 using the second way. Total points = 11 + floor(1 / 2) = 11.
It can be shown that the maximum points we can get after collecting coins from all the nodes is 11.
Example 2:


Input: edges = [[0,1],[0,2]], coins = [8,4,4], k = 0
Output: 16
Explanation:
Coins will be collected from all the nodes using the first way. Therefore, total points = (8 - 0) + (4 - 0) + (4 - 0) = 16.


Constraints:

n == coins.length
2 <= n <= 105
0 <= coins[i] <= 104
edges.length == n - 1
0 <= edges[i][0], edges[i][1] < n
0 <= k <= 104
"""

from typing import List
from collections import defaultdict

# TLE

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        def dfs(node:int, scale:int, vis:List[int]) -> int:
            vis[node] = 1
            if len(edge_dict[node]) == 0:
                return max(coins[node]//scale - k, coins[node]//(2*scale))
            children = [c for c in edge_dict[node] if vis[c] == 0]
            val_1 = coins[node]//scale - k +sum(dfs(c, scale, vis[::1]) for c in children)
            if scale >= 2**14:
                return val_1
            else:
                val_2 = coins[node]//(2*scale) + sum(dfs(c, scale*2, vis[::1]) for c in children)
                return max(val_1, val_2)
            

        edge_dict = defaultdict(list)
        for s, d in edges:
            edge_dict[s].append(d)
            edge_dict[d].append(s)

        return dfs(0, 1, [0] * len(coins))


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        pass



s = Solution()
edges = [[0,1],[1,2],[2,3]]
coins = [10,10,3,3]
k = 5
print(s.maximumPoints(edges, coins, k))
edges = [[0,1],[0,2]]
coins = [8,4,4]
k = 0
print(s.maximumPoints(edges, coins, k))
edges = [[1,0],[0,2],[1,3]]
coins = [9,3,8,9]
k = 0
print(s.maximumPoints(edges, coins, k))
edges = [[1,0],[2,1],[3,1],[2,4],[5,4],[6,3],[6,7]]
coins = [9,9,5,5,7,9,6,9]
k = 8
print(s.maximumPoints(edges, coins, k))
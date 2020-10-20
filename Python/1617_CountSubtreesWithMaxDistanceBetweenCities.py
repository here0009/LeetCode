"""
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

 

Example 1:



Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.
Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]
Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]
 

Constraints:

2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
"""

# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/discuss/889070/C%2B%2BPython-Bitmask-try-all-subset-of-cities-Clean-and-Concise-O(2n-*-n)
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        """
        list all the combinations of nodes, use bitmask to represent the nodes.
        check the nodes and their conncetions and the max distance
        if connections == nodes - 1, then it is a tree
        use Floyd Warshall to calculate the distance between nodes
        """
        def check(status):
            max_dist = 0
            connections = 0
            cities = 0
            for i in range(n):
                if status >> i & 1 == 0:
                    continue
                cities += 1
                for j in range(i+1, n):
                    if status >> j & 1 == 0:
                        continue
                    connections += dist[i][j] == 1
                    max_dist = max(max_dist, dist[i][j])
            return max_dist if connections == cities-1 else 0

        dist = [[float('inf')]*n for _ in range(n)]
        for i, j in edges:
            dist[i-1][j-1] = 1
            dist[j-1][i-1] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        res = [0]*(n-1)
        for status in range(1, 2**n):
            tmp = check(status)
            if tmp > 0:
                res[tmp-1] += 1
        return res


from collections import deque
from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        """
        two rounds of bfs to find the diameter of a tree
        """
        def bfs(src, cities):
            i, d = src, 0
            dq = deque([(src, 0)])
            visited = {src}
            while dq:
                i, d = dq.popleft()
                for j in edges_dict[i]:
                    if j not in visited and j in cities:
                        dq.append((j, d+1))
                        visited.add(j)
            return i,d,visited

        def diameterTree(cities):
            node = cities.pop()
            cities.add(node)
            end_node, d, visited = bfs(node, cities)
            if len(visited) != len(cities):
                return 0
            _, res, _ = bfs(end_node, cities)
            return res

        def maxDist(status):
            cities = set()
            for i in range(n):
                if (status >> i) & 1 == 1:
                    cities.add(i)
            return diameterTree(cities)

        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i-1].append(j-1)
            edges_dict[j-1].append(i-1)

        res = [0]*(n-1)
        for status in range(1, 2**n):
            tmp = maxDist(status)
            if tmp > 0:
                res[tmp-1] += 1
        return res

# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/discuss/889400/C%2B%2BPython-Floyd-Warshall-%2B-Enumerate-Subsets-O(2N-*-N2)
from itertools import combinations, permutations
class Solution_1:
    def countSubgraphsForEachDiameter(self, n, edges):
        g = [[float('inf') for _ in range(n)] for _ in range(n)]
        for [i, j] in edges:
            g[i - 1][j - 1], g[j - 1][i - 1] = 1, 1

        for k, i, j in permutations(range(n), 3):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        ans = [0]*(n-1)
        for k in range(2, n + 1):
            for s in combinations(range(n), k):
                e = sum(g[i][j] for i, j in combinations(s, 2) if g[i][j] == 1)
                d = max(g[i][j] for i, j in combinations(s, 2))
                if e == k - 1:
                    ans[d - 1] += 1
        return ans

S = Solution()
n = 4
edges = [[1,2],[2,3],[2,4]]
print(S.countSubgraphsForEachDiameter(n, edges))
n = 2
edges = [[1,2]]
print(S.countSubgraphsForEachDiameter(n, edges))
n = 3
edges = [[1,2],[2,3]]
print(S.countSubgraphsForEachDiameter(n, edges))
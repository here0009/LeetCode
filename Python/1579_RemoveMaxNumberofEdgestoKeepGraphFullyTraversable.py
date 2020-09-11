"""
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
"""


from collections import defaultdict
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        edges_alice = defaultdict(list)
        edges_bob = defaultdict(list)
        res = 0
        for t, u, v in edges:
            if t == 1:
                edges_alice[u].append(v)
                edges_alice[v].append(u)
            elif t == 2:
                edges_bob[u].append(v)
                edges_bob[v].append(u)
            elif t == 3:
                edges_alice[u].append(v)
                edges_alice[v].append(u)
                edges_bob[u].append(v)
                edges_bob[v].append(u)

# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/discuss/831573/Python-Union-Find
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            root[ru] = rv
            return True

        root = list(range(n+1))
        edges_alice, edges_bob, res = 0, 0, 0
        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    edges_alice += 1
                    edges_bob += 1
                else:
                    res += 1

        root_copy = root[:] # a copy of connection 3
        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    edges_alice += 1
                else:
                    res +=1

        root = root_copy
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    edges_bob += 1
                else:
                    res += 1
        if edges_alice == n-1 and edges_bob == n-1:
            return res
        else:
            return -1

# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/discuss/831509/Python3-union-find
class UnionFind:
    """A minimalist standalone union-find implementation."""
    def __init__(self, n):
        self.count = n               # number of disjoint sets 
        self.parent = list(range(n)) # parent of given nodes
        self.rank = [1]*n            # rank (aka size) of sub-tree 
        
    def find(self, p):
        """Find with path compression."""
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # path compression 
        return self.parent[p]
    
    def union(self, p, q):
        """Union with ranking."""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        self.count -= 1 # one more connection => one less disjoint 
        if self.rank[prt] > self.rank[qrt]: 
            prt, qrt = qrt, prt # add small sub-tree to large sub-tree for balancing
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt] # ranking 
        return True
    
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        ufa = UnionFind(n) # for Alice
        ufb = UnionFind(n) # for Bob
        ans = 0
        edges.sort(reverse=True)  # make 3 first
        for t, u, v in edges: 
            u, v = u-1, v-1
            if t == 3: 
                ans += not (ufa.union(u, v) and ufb.union(u, v)) # Alice & Bob
            elif t == 2: 
                ans += not ufb.union(u, v)                     # Bob only
            else: 
                ans += not ufa.union(u, v)                            # Alice only
        return ans if ufa.count == 1 and ufb.count == 1 else -1 # check if uf is connected 

S = Solution()
n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(S.maxNumEdgesToRemove(n, edges))
n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
print(S.maxNumEdgesToRemove(n, edges))
n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
print(S.maxNumEdgesToRemove(n, edges))
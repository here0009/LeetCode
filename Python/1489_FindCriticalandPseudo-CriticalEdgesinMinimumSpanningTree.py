"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between nodes fromi and toi. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph. An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. A pseudo-critical edge, on the other hand, is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:



Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti <= 1000
All pairs (fromi, toi) are distinct.
"""


class UnionFindSet:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        return True


from collections import defaultdict
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        def dfs(curr, level, parent):
            levels[curr] = level
            for child, i in graph[curr]:
                if child == parent:
                    continue
                elif levels[child] == -1:
                    levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
                else:
                    levels[curr] = min(levels[curr], levels[child])
                if levels[child] >= level + 1 and i not in p_cri:
                    cri.add(i)
            return levels[curr]

        cri, p_cri = set(), set()
        dic = defaultdict(list)
        for i, (u,v,w) in enumerate(edges):
            dic[w].append([u,v,i])

        union_set = UnionFindSet(n)
        for w in sorted(dic):
            seen = defaultdict(set)
            for u,v,i in dic[w]:
                pu, pv = union_set.find(u), union_set.find(v)
                if pu == pv:
                    continue
                seen[min(pu, pv), max(pu, pv)].add(i)

        w_edges, graph = [], defaultdict(list)
        for pu,pv in seen:
            if len(seen[pu, pv]) > 1:
                p_cri |= seen[pu, pv]
            edge_idx = seen[pu,pv].pop()
            graph[pu].append((pv, edge_idx))
            graph[pv].append((pu, edge_idx))
            w_edges.append((pu, pv, edge_idx))
            union_set.union(pu, pv)

        levels = [-1]*n
        for u,v,i in w_edges:
            if levels[u] == -1:
                dfs(u, 0, -1)
        for u,v,i in w_edges:
            if i not in cri:
                p_cri.add(i)

        return [cri, p_cri]

class Solution_1:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
    
        # reference: LC 1192
        def dfs(curr, level, parent):
            levels[curr] = level
            for child, i in graph[curr]:
                if child == parent:
                    continue
                elif levels[child] == -1:
                    levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
                else:
                    levels[curr] = min(levels[curr], levels[child])
                if levels[child] >= level + 1 and i not in p_cri:
                    cri.add(i)
            return levels[curr]
        
        # init critical and pseudo-critical edge set
        cri, p_cri = set(), set()
        
        # use dic to store all edges associated with a given weight
        dic = defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            dic[w].append([u, v, i])
        
        # define union find et
        union_set = UnionFindSet(n)
        # iterate through all weights in ascending order
        for w in sorted(dic):
            # seen[(pu, pv)] contains all edges connecting pu and pv,
            # where pu and pv are the parent nodes of their corresponding groups
            seen = defaultdict(set)
            # populate seen
            for u, v, i in dic[w]:
                pu, pv = union_set.find(u), union_set.find(v)
                # skip the edge that creates cycle
                if pu == pv:
                    continue
                seen[min(pu, pv), max(pu, pv)].add(i) # edge i connects pu and pv
            # w_edges contains all weight-w edges we may add to MST
            w_edges, graph = [], defaultdict(list)
            for pu, pv in seen:
                # more than 1 edge can connect pu and pv
                # these edges are pseudo-critical
                if len(seen[pu, pv]) > 1:
                    p_cri |= seen[pu, pv]
                # construct graph for weight w
                edge_idx = seen[pu, pv].pop()
                graph[pu].append((pv, edge_idx))
                graph[pv].append((pu, edge_idx))
                w_edges.append((pu, pv, edge_idx))
                # union pu and pv groups
                union_set.union(pu, pv)
            
            # run dfs to mark all critical w_edges
            levels = [-1] * n
            for u, v, i in w_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)
            # the edges in w_edges cycles are pseudo-critical
            for u, v, i in w_edges:
                if i not in cri:
                    p_cri.add(i)
        
        return [cri, p_cri]

###############################################################################
class UF:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            return False
        self.root[rj] = ri
        self.size[ri] += self.size[rj]
        return True


from collections import defaultdict
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        def mst(include, exlude):
            uf = UF(n)
            cost = 0
            idx = -1

            if include is not None:
                p, q, w, idx = include
                uf.union(p, q)
                cost += w

            elif exlude is not None:
                idx = exlude[-1]
            for p, q, w, i in edges_idx:
                if i == idx:
                    continue
                if uf.union(p, q):
                    cost += w
            size = uf.size[uf.find(0)]
            # print(include, exlude, visited, cost)
            return float('inf') if size < n else cost

        edges_idx = [lst + [i] for i, lst in enumerate(edges)]
        edges_idx.sort(key=lambda x: x[2])  # sort by weight
        base = mst(None, None)
        print('base', base)
        critical, p_cirtical = list(), list()
        for lst in edges_idx:
            index = lst[-1]
            if mst(None, lst) > base:
                critical.append(index)
            elif mst(lst, None) == base:
                p_cirtical.append(index)
        return [critical, p_cirtical]


S = Solution()
n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
print(S.findCriticalAndPseudoCriticalEdges(n, edges))
n = 4
edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
print(S.findCriticalAndPseudoCriticalEdges(n, edges))

n = 6
edges = [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]
print(S.findCriticalAndPseudoCriticalEdges(n, edges))
# Output
# [[],[0,1,2,4,5,6,3]]
# Expected
# [[3],[0,1,2,4,5,6]]
"""
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
 

Constraints:

2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.
"""


from typing import List
import heapq
from collections import defaultdict
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        TLE
        """
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, e in edgeList:
            dist[i][j] = min(e, dist[i][j])
            dist[j][i] = min(e, dist[j][i])
        edgeList = [(e, i, j) for i, j, e in edgeList if e <= dist[i][j]]
        heapq.heapify(edgeList)
        # print(edgeList)
        # for row in dist:
        #     print(row)
        # print('+++++++++++++++++++')
        edges_to = defaultdict(list)
        for e, i, j in edgeList:
            edges_to[i].append((j, e))
            edges_to[j].append((i, e))
        # print(edges_to)
        while edgeList:
            # print('pq', edgeList)
            e, p, q = heapq.heappop(edgeList)
            if dist[p][q] > e:
                dist[p][q] = e
                dist[q][p] = e
            for i, v in edges_to[p]:
                v = max(e, v)
                if dist[i][q] > v:
                    heapq.heappush(edgeList, (v, i, q))
            for i, v in edges_to[q]:
                v = max(e, v)
                if dist[i][p] > v:
                    heapq.heappush(edgeList, (v, i, p))
        res = []
        # for row in dist:
        #     print(row)
        for p, q, e in queries:
            res.append(dist[p][q] < e)
        return res


import heapq
from collections import defaultdict
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        TLE
        """
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, e in edgeList:
            dist[i][j] = min(e, dist[i][j])
            dist[j][i] = min(e, dist[j][i])
        edgeList = [(e, i, j) for i, j, e in edgeList if e <= dist[i][j]]
        heapq.heapify(edgeList)
        edges_to = defaultdict(list)
        for e, i, j in edgeList:
            edges_to[i].append((j, e))
            edges_to[j].append((i, e))

        visited = set()
        while edgeList:
            e, p, q = heapq.heappop(edgeList)

            if (p, q) in visited:
                continue
            visited.add((p, q))
            visited.add((q, p))

            for i, v in edges_to[p]:
                v = max(e, v)
                if dist[i][q] > v:
                    dist[i][q] = v
                    dist[q][i] = v
                    heapq.heappush(edgeList, (v, i, q))
            for i, v in edges_to[q]:
                v = max(e, v)
                if dist[i][p] > v:
                    dist[i][p] = v
                    dist[p][i] = v
                    heapq.heappush(edgeList, (v, i, p))
        res = []
        # for row in dist:
        #     print(row)
        for p, q, e in queries:
            res.append(dist[p][q] < e)
        return res



import heapq
from collections import defaultdict
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        TLE
        """
        def extend_node(p, q):
            """
            extend p's neighbors to q, wrong answer
            """
            if p not in visited:
                visited.add(p)
                for i, v in edges_to[p]:
                    if dist[i][q] > v:
                        dist[i][q] = v
                        dist[q][i] = v
                        heapq.heappush(edgeList, (v, i, q))

        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, e in edgeList:
            dist[i][j] = min(e, dist[i][j])
            dist[j][i] = min(e, dist[j][i])
        edgeList = [(e, i, j) for i, j, e in edgeList if e <= dist[i][j]]
        heapq.heapify(edgeList)
        edges_to = defaultdict(list)
        for e, i, j in edgeList:
            edges_to[i].append((j, e))
            edges_to[j].append((i, e))

        visited = set()
        while edgeList:
            # print(edgeList, visited)
            e, p, q = heapq.heappop(edgeList)
            if p in visited and q in visited:
                continue
            extend_node(p, q)
            extend_node(q, p)
        res = []
        # for row in dist:
        #     print(row)
        for p, q, e in queries:
            res.append(dist[p][q] < e)
        return res



class UnionFind:

    def __init__(self, length):
        self.root = list(range(length))

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            return False
        self.root[rj] = ri
        return True


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        building the dist matrix will cost O(n**2), n is 1E5, so will get TLE.
        we can use off-line algorithm in this problem, sort edges and queries. for p,q,e in queries, union the nodes that got distance < limit in the matrix, and check if p, q are unioned
        """
        uf = UnionFind(n)
        edgeList.sort(key=lambda x: x[2])
        index = 0
        len_e = len(edgeList)
        q2 = sorted([(*lst, i) for i, lst in enumerate(queries)], key=lambda x: x[2])
        res = [False] * len(q2)
        for p, q, d, i in q2:
            while index < len_e and edgeList[index][2] < d:
                uf.union(edgeList[index][0], edgeList[index][1])
                index += 1
            res[i] = uf.find(p) == uf.find(q)
        return res




S = Solution()
n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]
print(S.distanceLimitedPathsExist(n, edgeList, queries))
n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]
print(S.distanceLimitedPathsExist(n, edgeList, queries))

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries =[[0,1,2],[0,2,5]]
print(S.distanceLimitedPathsExist(n, edgeList, queries))
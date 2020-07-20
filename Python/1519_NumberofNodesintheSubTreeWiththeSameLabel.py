"""
Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
Example 2:


Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
Example 3:


Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]
Example 4:

Input: n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
Output: [1,2,1,1,2,1]
Example 5:

Input: n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
Output: [6,5,4,1,3,2,1]
 

Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
labels.length == n
labels is consisting of only of lower-case English letters.
"""


from collections import defaultdict
# from functools import lru_cache
from collections import Counter
# import sys
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        """
        reach max recurrsion depth
        """
        # @lru_cache(None)
        # def dfs(node, label):
        #     res = int(labels[node] == label)
        #     for i in uni_edges[node]:
        #         res += dfs(i, label)
            # return res
        # sys.setrecursionlimit(10000)
        # @lru_cache(None)
        def dfs(node):
            # print(node)
            # print(labels[node])
            res_dict[node][labels[node]] += 1
            for i in uni_edges[node]:
                res_dict[node] += dfs(i) 
            return res_dict[node]



        edges_dict = defaultdict(list)
        uni_edges = defaultdict(list)
        res_dict = defaultdict(Counter)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)

        
        res = []
        bfs = [0]
        visited = [False]*n
        print('edges_dict',edges_dict)
        
        while bfs:
            bfs2 = []
            for node in bfs:
                visited[node] = True
                for i in edges_dict[node]:
                    if not visited[i]:
                        bfs2.append(i)
                        uni_edges[node].append(i)
            bfs = bfs2

        dfs(0)
        # print('uni_edges',uni_edges)
        # print('res_dict',res_dict)
        for i in range(n):
            res.append(res_dict[i][labels[i]])
        return res



from collections import Counter
from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        def dfs(node):
            visited[node] = True
            c = Counter({labels[node]:1})
            for nei in tree[node]:
                if not visited[nei]:
                    c += dfs(nei)
            res[node] = c[labels[node]]
            return c

        tree = defaultdict(list)
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)
        res = [1]*n
        visited = [False]*n
        dfs(0)
        return res


from collections import Counter
from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        # @lru_cache(None)  Add this line,ther will be an error, OMG
        def dfs(node):
            visited[node] = True
            c = Counter({labels[node]:1})
            for i in edges_dict[node]:
                if not visited[i]:
                    c += dfs(i)
            res[node] = c[labels[node]]
            return c

        edges_dict = defaultdict(list)
        for i, j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)

        visited = [False]*n
        res = [0]*n
        dfs(0)
        return res

S = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(S.countSubTrees(n, edges, labels))
n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"
print(S.countSubTrees(n, edges, labels))
n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
labels = "aabab"
print(S.countSubTrees(n, edges, labels))
n = 6
edges = [[0,1],[0,2],[1,3],[3,4],[4,5]]
labels = "cbabaa"
print(S.countSubTrees(n, edges, labels))
n = 7
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
labels = "aaabaaa"
print(S.countSubTrees(n, edges, labels))

n = 4
edges = [[0,2],[0,3],[1,2]]
labels = "aeed"
print(S.countSubTrees(n, edges, labels))
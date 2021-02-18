"""
You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

 

Example 1:


Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:


Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.
 

Constraints:

1 <= pairs.length <= 105
1 <= xi < yi <= 500
The elements in pairs are unique.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List, Set
from collections import defaultdict
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # print(pairs)
        nodes = set()
        edges = defaultdict(list)
        for p, q in pairs:
            nodes |= set([p, q])
            edges[p].append(q)
            edges[q].append(p)
        n = len(nodes)

        root_lst = []
        for e, lst in edges.items():
            if len(lst) == n - 1:
                root_lst.append(e)
        print(pairs, edges, nodes, root_lst)
        # print('root', root, len(pairs))
        len_root = len(root_lst)
        if len_root == 0 or (len_root == 1 and len(pairs) == n - 1):
            return len_root
        elif len(root_lst) > 1:
            return 2
        else:
            root = root_lst[0]
            pairs2 = []
            for p, q in pairs:
                if p != root and q != root:
                    pairs2.append([p, q])
            if self.checkWays(pairs2) == 1:
                return 1
            return 2

# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/discuss/1009018/Python-Solution-commented
class Solution:
    def checkWays(self, P: List[List[int]]) -> int:
        # build graph
        g = defaultdict(set)
        for u, v in P:
            g[u].add(v)
            g[v].add(u)
        for i in g: 
            g[i].add(i)  # easy to compare if two nodes is equivalent (see below)
        n = len(g)
        # try using `rt` as the root of `nodes`
        def try_root(rt: int, nodes: Set[int]):
            print(rt, nodes, g)
            ways = 1
            # remove `rt` from all its children. similar to topological sorting
            for p in g[rt]:
                if p == rt:
                    continue
                if p not in nodes:
                    return 0  # if see a node not in `nodes`, wrong
                if g[p] == g[rt]:
                    ways = 2  # `p` is equivalent with `rt`, so switching them gives another answer
                g[p].remove(rt)
            # try `rt`'s children as root of subtree starting from larger degree
            to_try = sorted(((len(g[p]), p) for p in g[rt] if p != rt), reverse=True)
            for l, p in to_try:
                # a node is modified means it's already a child of a previous node in `to_try`, need to skip it
                if l >= 2 and l == len(g[p]):
                    w = try_root(p, nodes & g[p])
                    if w == 0:
                        return 0
                    if w == 2:
                        ways = 2
            return ways
        # this question requires one single rooted tree, not a forest
        # so we have to find a root connected to all the other nodes
        for i in g:
            if len(g[i]) == n:
                return try_root(i, g[i])
        return 0

# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/discuss/1009238/Python-dfs-solution-explained
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        def check(nodes):
            def dfs(p, i):
                comp[i].add(p)
                for q in graph[p]:
                    if q not in visited:
                        visited.add(q)
                        dfs(q, i)

            edges_len = defaultdict(list)
            n = len(nodes) - 1
            for p in nodes:
                edges_len[len(graph[p])].append(p)
            if len(edges_len[n]) == 0:
                return 0
            root = edges_len[n][0]
            for q in graph[root]:
                graph[q].remove(root)
            visited, idx = set([root]), 0
            comp = defaultdict(set)
            for p in nodes:
                if p not in visited:
                    visited.add(p)
                    dfs(p, idx)
                    idx += 1
            candi = [check(tmp) for tmp in comp.values()]
            if 0 in candi:
                return 0
            if 2 in candi or len(edges_len[n]) > 1:
                return 2
            return 1

        graph = defaultdict(set)
        for p, q in pairs:
            graph[p].add(q)
            graph[q].add(p)
        return check(graph.keys())

S = Solution()
pairs = [[1,2],[2,3]]
print(S.checkWays(pairs))
pairs = [[1,2],[2,3],[1,3]]
print(S.checkWays(pairs))
pairs = [[1,2],[2,3],[2,4],[1,5]]
print(S.checkWays(pairs))
pairs = [[1,5],[1,3],[2,3],[2,4],[3,5],[3,4]]
print(S.checkWays(pairs))
pairs = [[3,5],[4,5],[2,5],[1,5],[1,4],[2,4]]
print(S.checkWays(pairs))
pairs = [[3,4],[2,3],[4,5],[2,4],[2,5],[1,5],[1,4]]
print(S.checkWays(pairs))
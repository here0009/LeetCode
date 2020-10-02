"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/graph-valid-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges) -> bool:
        """
        a valid tree is a acyclic graph that connect every node in the tree
        """
        def dfs(node):
            if self.cycle:
                return
            visited[node] += 1
            if visited[node] > 1:
                self.cycle = True
                return
            for next_node in edges_dict[node]:
                if node in edges_dict[next_node]:
                    edges_dict[next_node].remove(node)
            for next_node in edges_dict[node]:
                dfs(next_node)

        edges_dict = defaultdict(set)
        for p, q in edges:
            edges_dict[p].add(q)
            edges_dict[q].add(p)

        # print(edges_dict)
        visited = [0]*n
        self.cycle = False
        dfs(0)
        # print(visited)
        return not self.cycle and all(num == 1 for num in visited)


class Solution:
    def validTree(self, n: int, edges) -> bool:
        """
        union find
        """
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i,j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[rj] = ri
            return True

        if len(edges) != n-1:
            return False
        if not edges:
            return True
        root = dict()
        for i in range(n):
            root[i] = i
        visited = set()

        for i,j in edges:
            if not union(i,j):
                return False
            visited |= {i,j}
        return len(visited) == n


class Solution:
    def validTree(self, n: int, edges) -> bool:
        """
        because n == len(edges)-1, so if there are redundant edges, then not every node will be visited
        """
        if n != len(edges)+1: return False
        if not edges: return True
        def dfs(i):
            for node in adjacency[i]:
                if not flags[node]:
                    flags[node] = 1
                    dfs(node)
        adjacency = [[] for _ in range(n)]
        flags = [0 for _ in range(n)]
        for cur,pre in edges:
            adjacency[pre].append(cur)
            adjacency[cur].append(pre)
        dfs(0)
        return sum(flags) == len(flags)

# 作者：luo_luo
# 链接：https://leetcode-cn.com/problems/graph-valid-tree/solution/yi-tu-pan-shu-python3shen-du-yan-du-you-xian-sou-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
S = Solution()
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(S.validTree(n, edges))
n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(S.validTree(n, edges))

n = 4
edges = [[0,1],[2,3]]
print(S.validTree(n, edges))

n = 1
edges = []
print(S.validTree(n, edges))
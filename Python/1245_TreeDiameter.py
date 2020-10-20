"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/tree-diameter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from collections import deque
class Solution:
    def treeDiameter(self, edges) -> int:
        def bfs(src):
            dq = deque([(src, 0)])
            visited = {src}
            node, d = src, 0
            while dq:
                node, d = dq.popleft()
                for next_node in edges_dict[node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        dq.append((next_node, d+1))
            return node, d

        nodes = set()
        edges_dict = defaultdict(list)
        for i,j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
            nodes.add(i)
            nodes.add(j)

        node = nodes.pop()
        f_node, _ = bfs(node)
        _, res = bfs(f_node)
        return res

S = Solution()
edges = [[0,1],[0,2]]
print(S.treeDiameter(edges))
edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
print(S.treeDiameter(edges))
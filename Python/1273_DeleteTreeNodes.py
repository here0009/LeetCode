"""
A tree rooted at node 0 is given as follows:

The number of nodes is nodes;
The value of the i-th node is value[i];
The parent of the i-th node is parent[i].
Remove every subtree whose sum of values of nodes is zero.

After doing so, return the number of nodes remaining in the tree.

 

Example 1:


Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
Example 2:

Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
Output: 6
Example 3:

Input: nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]
Output: 5
Example 4:

Input: nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]
Output: 5
 

Constraints:

1 <= nodes <= 10^4
parent.length == nodes
0 <= parent[i] <= nodes - 1
parent[0] == -1 which indicates that 0 is the root.
value.length == nodes
-10^5 <= value[i] <= 10^5
The given input is guaranteed to represent a valid tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def deleteTreeNodes(self, nodes: int, parent, value) -> int:
        def dfs(i):
            val = value[i]
            counts = 1
            for j in edges[i]:
                vj, cj = dfs(j)
                val += vj
                counts += cj
            if val == 0:
                return 0, 0
            else:
                return val, counts

        edges = defaultdict(list)

        for i, v in enumerate(parent):
            edges[v].append(i)
            if v == -1:
                root = i
        return dfs(root)[1]

S = Solution()
nodes = 7
parent = [-1,0,0,1,2,2,2]
value = [1,-2,4,0,-2,-1,-1]
print(S.deleteTreeNodes(nodes, parent, value))
nodes = 7
parent = [-1,0,0,1,2,2,2]
value = [1,-2,4,0,-2,-1,-2]
print(S.deleteTreeNodes(nodes, parent, value))
nodes = 5
parent = [-1,0,1,0,0]
value = [-672,441,18,728,378]
print(S.deleteTreeNodes(nodes, parent, value))
nodes = 5
parent = [-1,0,0,1,1]
value = [-686,-842,616,-739,-746]
print(S.deleteTreeNodes(nodes, parent, value))

nodes = 1
parent = [-1]
value = [0]
print(S.deleteTreeNodes(nodes, parent, value))
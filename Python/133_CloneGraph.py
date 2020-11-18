"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]
 

Constraints:

1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

# Definition for a Node.


from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        length = 101
        matrix = [[0]*length for _ in range(length)]
        visited = [0]*length
        bfs = [node]
        while bfs:
            for n in bfs:
                visited[n.val] = 1
            bfs2 = []
            for n in bfs:
                i = n.val
                lst = n.neighbors
                for next_n in lst:
                    j = next_n.val
                    if visited[j] == 0:
                        matrix[i][j] = 1
                        matrix[j][i] = 1
                        bfs2.append(next_n)


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            visited.add(node)
            v = node.val
            for n_node in node.neighbors:
                if n_node not in visited:
                    edges[v].add(n_node.val)
                    edges[n_node.val].add(v)
                    dfs(n_node)

        edges = defaultdict(set)
        print(edges)
        nodes = [Node(i) for i in  edges.keys()]
        for node in nodes:
            node.neighbors = []
            
from collections import defaultdict
class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        """
        wrong anwer
        """
        def dfs(pre, curr):
            if not curr:
                return None
            lst = []
            for n_node in curr.neighbors:
                if n_node is not pre:
                    lst.append(dfs(curr, n_node))
            return Node(curr.val, lst)

        def addEdge(pre, curr):
            if not curr:
                return
            if pre:
                curr.neighbors.append(pre)
                print(pre.val, curr.val)
            else:
                print('None', curr.val)
            for n_node in curr.neighbors:
                if n_node != pre:
                    addEdge(curr, n_node)

        res = dfs(None, root)
        addEdge(None, res)
        return res


class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            if node in seen:
                return seen[node]
            cp_node = Node(node.val)
            seen[node] = cp_node
            for nxt in node.neighbors:
                cp_node.neighbors.append(dfs(nxt))
            return cp_node

        seen = dict()
        return dfs(root)


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import deque
class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        visited = {}

        # 将题目给定的节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存储到哈希表中
        visited[node] = Node(node.val, [])

        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            n = queue.popleft()
            # 遍历该节点的邻居
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列中
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]


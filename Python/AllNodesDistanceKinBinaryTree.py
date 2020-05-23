"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from LeetCode import Tree_Builds_BFS
class Solution:
    def distanceK(self, root, target, K):

        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        Thougths: change the tree to a self.graph, then find the nodes that got a distance K from target
        """
        
        def dfs(root, pre):
            self.graph[root.val] = set()
            if pre is not None:
                self.graph[root.val].add(pre)
            if root.left:
                self.graph[root.val].add(root.left.val)
                dfs(root.left, root.val)
            if root.right:
                self.graph[root.val].add(root.right.val)
                dfs(root.right, root.val)

        self.graph = dict()
        dfs(root, None)
        # print(self.graph)
        visited = set()
        nodes = set([target.val])
        while K > 0 and nodes:
            next_nodes = set()
            for node in nodes:
                visited.add(node)
                for k in self.graph[node]:
                    if k not in visited:
                        next_nodes.add(k)
            nodes = next_nodes
            K -= 1
        #     print(next_nodes)
        # print(visited)
        return list(nodes)

s = Solution()
vals = [3,5,1,6,2,0,8,None,None,7,4]
target = 5
K = 2
root = Tree_Builds_BFS(vals)
print(root.right.right.val)
print(root.right.left.val)
print(s.distanceK(root, target, K))
print(s.distanceK(root, 3, 5))
            
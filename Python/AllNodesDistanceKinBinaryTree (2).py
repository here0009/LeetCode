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

from collections import defaultdict
class Solution:
    """
    use a dict to store the connections, then BFS
    """
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node):
            if not node:
                return
            if node.left:
                conn[node.val].append(node.left.val)
                conn[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                conn[node.val].append(node.right.val)
                conn[node.right.val].append(node.val)
                dfs(node.right)

        conn = defaultdict(list)
        dfs(root)
        print(conn)
        visited = set()
        t_val = target.val
        bfs = [t_val]
        visited.add(t_val)
        while len(bfs) > 0 and K > 0:
            bfs2 = []
            for val in bfs:
                for next_val in conn[val]:
                    if next_val not in visited:
                        visited.add(next_val)
                        bfs2.append(next_val)
            bfs = bfs2
            K -= 1
        return bfs

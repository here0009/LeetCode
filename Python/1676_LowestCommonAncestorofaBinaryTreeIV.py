"""
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
Example 4:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]
Output: 3
Explanation: The lowest common ancestor of all the nodes is the root node.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
All nodes[i] will exist in the tree.
All nodes[i] are distinct.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Thoughts: use a dict to store the node's all decendent, TLE
        """
        def dfs(node):
            if not node:
                return None
            nodes_dict[node].add(node)
            if node.left:
                nodes_dict[node] |= dfs(node.left)
            if node.right:
                nodes_dict[node] |= dfs(node.right)
            return nodes_dict[node]

        def search(node):
            if node.left and len(nodes_set - nodes_dict[node.left]) == 0:
                return search(node.left)
            if node.right and len(nodes_set - nodes_dict[node.right]) == 0:
                return search(node.right)
            return node

        nodes_dict = defaultdict(set)
        dfs(root)
        nodes_set = set(nodes)
        return search(root)

from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        Thoughts: use a dict to store the node's all decendent, TLE
        """
        def dfs(node):
            if not node:
                return None
            nodes_dict[node].add(node)
            if node.left:
                nodes_dict[node] |= dfs(node.left)
            if node.right:
                nodes_dict[node] |= dfs(node.right)
            return nodes_dict[node]

        def search(node):
            if node.left and len(nodes_set - nodes_dict[node.left]) == 0:
                return search(node.left)
            if node.right and len(nodes_set - nodes_dict[node.right]) == 0:
                return search(node.right)
            return node

        nodes_dict = defaultdict(set)
        dfs(root)
        nodes_set = set(nodes)
        return search(root)

        
from collections import defaultdict
from functools import lru_cache
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(node):
            """
            remove the children of node
            """
            if not node or node in removed:
                return
            if node in nodes_set:
                nodes_set.remove(node)
                removed.add(node)
            dfs(node.left)
            dfs(node.right)

        @lru_cache(None)
        def search(node, x):
            if node is None:
                return False
            if x is node or search(node.left, x) or search(node.right, x):
                return True
            return False

        def lca(node, x, y):
            if node is None:
                return False
            if search(node.left, x) and search(node.left, y):
                return lca(node.left, x, y)
            if search(node.right, x) and search(node.right, y):
                return lca(node.right, x, y)
            return node

        def lca_list(i, j):
            if i == j:
                return nodes[i]
            if j - i == 1:
                return lca(root, nodes[i], nodes[j])
            mid = (i + j) // 2
            return lca(root, lca_list(i, mid), lca_list(mid + 1, j))

        nodes_set = set(nodes)
        removed = set()
        for node in nodes:
            dfs(node.left)
            dfs(node.right)
        nodes = list(nodes_set)
        print([node.val for node in nodes])
        return lca_list(0, len(nodes) - 1)



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(node):
            if not node or node not in nodes:
                return None
            if node in nodes:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            return l or r

        return dfs(root)
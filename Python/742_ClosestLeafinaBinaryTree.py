"""Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        wrong answer
        """
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    diff = abs(node.val - k)
                    if diff < self.diff:
                        self.diff = diff
                        self.res = node.val
                dfs(node.left)
                dfs(node.right)

        self.diff = float('inf')
        self.res = None
        dfs(root)
        return self.res


class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node):
            """
            return the nodes on the path from node to the nearest leaf node and the value of the leaf node
            """
            if not node:
                return float('inf'), None
            if not node.left and not node.right:
                return 1, node.val
            ld, lv = dfs(node.left)
            rd, rv = dfs(node.right)
            if ld < rd:
                return ld+1, lv
            else:
                return rd+1, rv

        def check(pre, node):
            if node.val == k:
                d1, v1 = dfs(pre)
                d2, v2 = dfs(node)
                if d1 < d2:
                    self.res = v1
                else:
                    self.res = v2
                return
            check(node, node.left)
            check(node, node.right)

        head = TreeNode(0)
        head.right = root
        self.res = None 
        check(head, root)
        return self.res



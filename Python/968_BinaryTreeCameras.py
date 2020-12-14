"""
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        we have to monitor all nodes, the leaves can only monitored by itself or its parent
        put monitors at parent should always save monitors, if the children is not monitored
        wrong answer
        """
        def dfs(node):
            """
            return True if we put at it, else False
            """
            if not node:
                return True
            left, right = dfs(node.left), dfs(node.right)
            if left and right:
                return False
            else:
                self.res += 1
                return True

        self.res = 0
        if not root.left and not root.right:
            return 1
        dfs(root)
        return self.res


from typing import Tuple
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        we have to monitor all nodes, the leaves can only monitored by itself or its parent
        put monitors at parent should always save monitors, if the children is not monitored
        wrong answer
        """
        def dfs(node: TreeNode) -> Tuple[bool, bool]:
            """
            return isCameraed and isMonitored
            """
            if not node:
                return False, True
            lc, lm = dfs(node.left)
            rc, rm = dfs(node.right)
            if not (lm and rm):
                self.res += 1
                return True, True
            else:
                if lc or rc:
                    return False, True
                else:  # left node and right node is all monitored, but no cameras, we can put camera at the parent of current node, unless node is root
                    if node is root:
                        self.res += 1
                    return True, False

        self.res = 0
        dfs(root)
        return self.res

"""
Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.
Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
All Node.val are unique.
p and q are values in the tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-distance-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.


"""
[3,5,1,6,2,0,8,null,null,7,4]
5
0

[3,5,1,6,2,0,8,null,null,7,4]
5
7

[3,5,1,6,2,0,8,null,null,7,4]
5
5
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        """
        find the lowest common ancestor of p and q (lca), result is the dist(lca - p) + dist(lca - q)
        """

        def dfs(node):
            # if self.res != float('inf'):
            #     return float('inf'), float('inf')
            if not node:
                return float('inf'), float('inf')
            vp, vq = float('inf'), float('inf')
            if node.val == p:
                vp = 0
            if node.val == q:
                vq = 0
            lp, lq = dfs(node.left)
            rp, rq = dfs(node.right)
            vp, vq = min(lp + 1, rp + 1, vp), min(lq + 1, rq + 1, vq)
            if vp != float('inf') and vq != float('inf'):
                self.res = min(self.res, vp + vq)
            return vp, vq

        self.res = float('inf')
        dfs(root)
        return self.res



"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def Tree_Builds_BFS(node_val_list):
    node_q = deque()
    if node_val_list[0]:
        root = TreeNode(node_val_list[0])
        node_q.append(root)
    else:
        return None
    counts = 0 #counts for left and right
    for val in node_val_list[1:]:
        # print(val)
        if val is not None: #make a mistake by using if val, so if val is zero, node will not be construted
            node = TreeNode(val)
        else:
            node = None
        if node:
            node_q.append(node)
        tmp_node = node_q[0]
        if counts == 0:
            tmp_node.left = node
            counts = 1
        else: #make a mistake by using if counts == 1, so the node keep on popleft, stupid
            tmp_node.right = node
            node_q.popleft()
            counts = 0

    return root

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def isLeaf(root):
            return not root.left and not root.right
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        if isLeaf(root) and root.val == 0:
            return None
        return root

s = Solution()
node_val_list = [1,None,0,0,1]
root = Tree_Builds_BFS(node_val_list)

# print(root.val)
# print(root.right.val)
# print(root.right.left.val)
# print(root.right.right.val)

# root = s.pruneTree(root)

# print(root.val)
# print(root.right.val)
# print(root.right.left)



node_val_list = [1,0,1,0,0,0,1]

root = Tree_Builds_BFS(node_val_list)
print(root.left.val)
root = s.pruneTree(root)
print(root.left)

"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode):
        #inorder traverse, so the values will be in ascending order
        def fn(node, v):
            # print(node.val, v)
            counts = 1
            if node.left:
                if node.left.val == v:
                    counts += fn(node.left, v)
                else:
                    fn(node.left, node.left.val)
            if node.right:
                if node.right.val == v:
                    counts += fn(node.right, v)
                else:
                    fn(node.right, node.right.val)
            if counts > self.max:
                self.res = [v]
                self.max = counts
            elif counts == self.max:
                self.res.append(v)
            return counts

        if not root:
            return None
        else:
            self.max = 0
            self.res = [root.val]
            fn(root, root.val)
            return self.res

from collections import Counter
class Solution:
    def findMode(self, root: TreeNode):
        def dfs(node):
            if node:
                tree_counter[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        tree_counter = Counter()
        if not root:
            return []
        dfs(root)
        max_v = max(tree_counter.values())
        return [key for key in tree_counter.keys() if tree_counter[key] == max_v]

S = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
# root.right.left = TreeNode(2)
print(S.findMode(root))

# [1,null,2]
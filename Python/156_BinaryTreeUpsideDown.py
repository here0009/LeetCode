"""
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every node has either 0 or 2 children.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-upside-down
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from LeetCode import Tree_Builds_BFS, printBinaryTree
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        wrong anwer
        """
        def switch(node):
            print(node.val)
            if node.left:
                new_root = switch(node.left)
                node.left = None
                new_root.left = node
                new_root.right = node.right
                return new_root
            return node

        return switch(root)

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = []
        while root: # reach the most left node, which is the new root
            stack.append(root)
            root = root.left
        new_root = node = stack.pop()
        while stack:
            pre_node = stack.pop() #pre_node is the pre parent of node
            node.left = pre_node.right
            node.right = pre_node
            node = pre_node
        node.left = node.right = None #node is now the leaf-node, set  its children to None
        return new_root

input_list = [1,2,3,4,5]
root = Tree_Builds_BFS(input_list)
S = Solution()
r = S.upsideDownBinaryTree(root)
printBinaryTree(r)

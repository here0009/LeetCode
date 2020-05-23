"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeLevel(root):
    """
    return the depth of the tree
    """

    if not root:
        return 0
    else:
        return 1+max(treeLevel(root.left),treeLevel(root.right))
def construcTree(voyage):
    """
    contruct a tree from a list named voyage, e.g: [1,2,3,None,None,4,5]
      1
     / \
    2   3
        /\
       4  5
    """
    def treeNode(val):
        if val is None:
            return None
        else:
            return TreeNode(val)

    v_root = TreeNode(voyage[0])
    bfs = deque([v_root])
    index = 0
    len_v = len(voyage)
    while bfs and index < len_v:
        node = bfs.popleft()
        if index+1 < len_v:
            node.left = treeNode(voyage[index+1])
        if index+2 < len_v:
            node.right = treeNode(voyage[index+2])
        if node.left:
            bfs.append(node.left)
        if node.right:
            bfs.append(node.right)
        index += 2
    return v_root

def printBinaryTree(root):
    """
    print the binary tree, not very elegant now
    """
    level = treeLevel(root)
    q = deque([root])
    while level > 0:
        new_q = deque()
        while q:
            tmp = q.popleft()
            if tmp:
                new_q.append(tmp.left)
                new_q.append(tmp.right)
                print(level*' ', tmp.val, end='')
        print('\n')
        q = new_q
        level -= 1
    return

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def depth(node):
            if node is None:
                return 0
            return 1+max(depth(node.left),depth(node.right))

        def nodeShift(node):
            if node:
                # print(node.val)
                node.left = nodeShift(node.left)
                node.right = nodeShift(node.right)
                ld = depth(node.left)
                rd = depth(node.right)
                new_root = node
                if rd - ld > 1: #rotateLeft
                    new_root = node.right
                    node.right = new_root.left
                    new_root.left = node
                if ld - rd > 1: #rotateRight
                    new_root = node.left
                    node.left = new_root.right
                    new_root.right = node
                return new_root

        return nodeShift(root)


class Solution:
    """
    Thoughts: inorder travers, then construct a tree
    """
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.left)
                self.nodes.append(node)
                dfs(node.right)

        def construcTree(vals):
            len_v = len(vals)
            if len_v == 0:
                return None
            index = len_v//2
            root = vals[index]
            root.left = construcTree(vals[:index])
            root.right = construcTree(vals[index+1:])
            return root

        self.nodes = []
        dfs(root)
        # print([node.val for node in self.nodes])
        return construcTree(self.nodes)

S = Solution()
root = [1,None,2,None,3,None,4,None,None]
root = construcTree(root)
printBinaryTree(root)
printBinaryTree(S.balanceBST(root))

root = [1,None,15,14,17,7,None,None,None,2,12,None,3,9,None,None,None,None,11]
root = construcTree(root)
printBinaryTree(root)
printBinaryTree(S.balanceBST(root))


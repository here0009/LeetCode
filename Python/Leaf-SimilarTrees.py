"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.
"""

"""
Thoughts:
Tranverse the tree from the root.
when a leaf is reached, compare its value of tree1 and tree2 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        pass

    def leafGenerator(self, root):
        """
        generete the nodes in tree
        """    
        if root.left:
            return leafGenerator(root.left)
        if root.right:
            return leafGenerator(root.right)
        else:
            yield root.val


# s = Solution()
treeSeq = [3,5,1,6,2,9,8,None,None,7,4,None,None,None,None]
print(len(treeSeq))

def treeGenerator(treeSeq):
    len_treeSeq = len(treeSeq)
    root = TreeNode(treeSeq[0])
    if len_treeSeq > 1:
        root.left = TreeNode(treeSeq[1])
    else:
        root.left = None
    if len_treeSeq > 2:
        root.right = TreeNode(treeSeq[2])
    else:
        root.right = None

    for i in range(len_treeSeq//2 + 1)[1:]:
        tmp = TreeNode(treeSeq[i])
        if len_treeSeq > 2*i + 1 :
            tmp.left = TreeNode(treeSeq[2*i+1])
        else:
            tmp.left = None
        if len_treeSeq > 2*i + 2:
            tmp.right = TreeNode(treeSeq[2*i+2])
        else:
            tmp.right = None
    return root


root = treeGenerator(treeSeq)
print(root.left.left.val)
    


class Solution_1:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool

        """
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

# print(s.nodeGenerator(root))

class Solution_2:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        value_set1 = []
        value_set2 = []
        def get_leaf_value(root, value_list):
            if root is None:
                return
            if root.left is None and root.right is None:
                value_list.append(root.val)
                return
            else:
                get_leaf_value(root.left, value_list)
                get_leaf_value(root.right, value_list)
        
        get_leaf_value(root1, value_set1)
        get_leaf_value(root2, value_set2)
        return value_set1 == value_set2
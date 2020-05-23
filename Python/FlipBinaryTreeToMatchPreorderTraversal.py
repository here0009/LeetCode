"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:



Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:



Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:



Input: root = [1,2,3], voyage = [1,2,3]
Output: []
 

Note:

1 <= N <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
class Solution_1:
    """
    too complicated, did not get the right answer
    """
    def construcTree(self,voyage):
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

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def equalNode(n1,n2):
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val

        def dfs(n1,n2):
            if equalNode(n1,n2):
                if equalNode(n1.left, n2.right) and equalNode(n1.right, n2.left):
                    if n1.left or n1.right:
                        self.res.append(n1.val)
                return True
            else:
                if equalNode(n1.left,n2.left):
                    dfs(n1.left, n2.left)
                if equalNode(n1.right,n2.right):
                    dfs(n1.right, n2.right)

        v_root = self.construcTree(voyage)
        print(v_root.val)
        print(v_root.left.val)
        self.res = []
        dfs(root, v_root)
        return self.res

from typing import List
# from collections import deque
class Solution:
    def construcTree(self,voyage):
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

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(node):
            if not node:
                return True
            if node.val  != voyage[self.index]:
                return False
            self.index += 1
            if self.index < len_v and node.left and node.left.val != voyage[self.index]:
                node.left, node.right = node.right, node.left
                res.append(node.val)
            return dfs(node.left) and dfs(node.right)


        res = []
        len_v = len(voyage)
        self.index = 0
        if not dfs(root):
            return [-1]
        else:
            return res

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(node):
            if not node:
                return True
            if node.val  != voyage[self.index]:
                return False
            self.index += 1
            if self.index < len_v and node.left and node.left.val != voyage[self.index]:
                node.left, node.right = node.right, node.left
                res.append(node.val)
            return dfs(node.left) and dfs(node.right)

        res = []
        len_v = len(voyage)
        self.index = 0
        if not dfs(root):
            return [-1]
        else:
            return res

class Solution:
    def construcTree(self,voyage):
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

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
            self.index=0
            self.res=[]

            def find(node):
                if not node: 
                    return True

                if node.val!=voyage[self.index]: 
                    return False
                self.index+=1

                if node.left and node.right and voyage[self.index]!=node.left.val:
                    self.res.append(node.val)
                    return find(node.right) and find(node.left)
                else: 
                    return find(node.left) and find(node.right)
                    
            return self.res if find(root) else [-1]

S = Solution()
root = [1,2]
root = S.construcTree(root)
# root.left = TreeNode(2)
voyage = [2,1]
print(S.flipMatchVoyage(root, voyage))
root = [1,2,3]
root = S.construcTree(root)
voyage = [1,3,2]
print(S.flipMatchVoyage(root, voyage))
root = [1,2,3]
root = S.construcTree(root)
voyage = [1,2,3]
print(S.flipMatchVoyage(root, voyage))
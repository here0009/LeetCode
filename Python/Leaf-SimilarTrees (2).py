# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        """
        not right
        """
        def bfsTraverse(root):
            res = []
            bfs = [root]
            while len(bfs) > 0:
                bfs2 = []
                for node in bfs:
                    if not node.left and not node.right:
                        res.append(node.val)
                    if node.left:
                        bfs2.append(node.left)
                    if node.right:
                        bfs2.append(node.right)
                bfs = bfs2
            return res

        l1 = bfsTraverse(root1)
        l2 = bfsTraverse(root2)
        return l1 == l2

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        """
        not right
        """
        def dfs(node, res):
            if not node.left and not node.right:
                res.append(node.val)
            if node.left:
                dfs(node.left, res)
            if node.right:
                dfs(node.right, res)
            return res

        l1 = dfs(root1,[])
        l2 = dfs(root2,[])
        print(l1)
        print(l2)
        return l1 == l2

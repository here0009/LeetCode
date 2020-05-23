"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def delNodes(self, root: TreeNode, to_delete):

        def dfs(root, n):
            if not root or (not root.left and not not root.right):
                return
            if root.val == n:
                if root.left:
                    self.res.append(root.left)
                    root.left = None
                if root.right:
                    self.res.append(root.right)
                    root.right = None
                return None
            if root.left:
                left = root.left.val
            else:
                left = 0
            if root.right:
                right = root.right.val
            else:
                right = 0
            tmp = n
            val = max(left, right)
            while (tmp > root.right.val):
                tmp = tmp//2
            if tmp == root.left.val:
                root.left = dfs(root.left, n)
            elif tmp == root.right.val:
                root.right = dfs(root.right,n)



class Solution_2:
    def delNodes(self, root: TreeNode, to_delete):
        """
        not an ordered tree, the solution is wrong
        """
        self.res = []
        to_delete = sorted(to_delete, reverse = True)
        for i in to_delete:
            tmp_node = root
            path = []
            while i > 1:
                i = i//2
                path.append(i)
            path = path[::-1]
            for val in path[1:]:
                if tmp_node.left.val == val:
                    tmp_node = tmp_node.left
                if tmp_node.right.val == val:
                    tmp_node = tmp_node.right
            print(path)
            print(tmp_node.val)
            #tmp_node is the father of i
            if tmp_node.val*2 == i:
                node = tmp_node.left
                tmp_node.left = None
            else:
                node = tmp_node.right
                tmp_node.right = None

            if node.left:
                self.res.append(node.left)
            if node.right:
                self.res.append(node.right)
        self.res.append(root)
        return self.res


class Solution_3:
    def delNodes(self, root: TreeNode, to_delete):
        """
        BFS
        """
        to_delete = set(to_delete)
        res = [root]
        nodes = [root]
        while nodes:
            tmp = [i.val for i in nodes]
            print(tmp)
            nodes_2 = []
            for node in nodes:
                if node.left:
                    if node.left.val in to_delete:
                        # print(node.left.val)
                        # to_delete.remove(node.left.val)
                        if node.left.left:
                            res.append(node.left.left)
                            nodes_2.append(node.left.left)
                        if node.left.right:
                            res.append(node.left.right)
                            nodes_2.append(node.left.right)
                        node.left = None
                    else:
                        nodes_2.append(node.left)
                    if node.val in to_delete:
                        nodes_2.append(node.left)
                        res.append(node.left)
                if node.right:
                    if node.right.val in to_delete:
                        # print(node.right.val)
                        # to_delete.remove(node.right.val)
                        if node.right.left:
                            res.append(node.right.left)
                            nodes_2.append(node.right.left)
                        if node.right.right:
                            res.append(node.right.right)
                            nodes_2.append(node.right.right)
                        node.right = None
                    else:
                        nodes_2.append(node.right)
                    if node.val in to_delete:
                        nodes_2.append(node.right)
                        res.append(node.right)

            nodes = nodes_2
        tmp = [i.val for i in res]
        print(tmp)
        return [n for n in res if n.val not in to_delete]


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        """
        DFS
        """
        
        def dfs(pre,node,flag):
            if not node or not pre:
                return
            # print(node.val, pre.val)
            if node.val in to_delete:
                if flag: #left
                    pre.left = None
                else:
                    pre.right = None
                if node.left:
                    res.append(node.left)           
                if node.right:
                    res.append(node.right)
            dfs(node,node.left,1)
            dfs(node,node.right,0)

            
            
        to_delete = set(to_delete)
        dummy = TreeNode(0)
        dummy.left = root
        res = [root]

        dfs(dummy, root, 1)
        # tmp = [i.val for i in res]
        # print(tmp)
        return [n for n in res if n.val not in to_delete]

class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        """
        DFS
        """
        def dfs(pre,node,flag):
            if not node or not pre:
                return
            if node.val in to_delete:
                if flag: #left
                    pre.left = None
                else:
                    pre.right = None
                if node.left:
                    res.append(node.left)           
                if node.right:
                    res.append(node.right)
            dfs(node,node.left,1)
            dfs(node,node.right,0)

        to_delete = set(to_delete)
        dummy = TreeNode(0)
        dummy.left = root
        res = [root]
        dfs(dummy, root, 1)
        return [node for node in res if node.val not in to_delete]
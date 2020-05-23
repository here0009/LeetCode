"""
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:



Input: [3,0,0]
Output: 2

Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2

Example 4:



Input: [1,0,0,null,3]
Output: 4
 

Note:

1<= N <= 100
0 <= node.val <= N
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Tree_Builds_BFS(node_val_list):
    node_list = []
    for index, val in enumerate(node_val_list):
        if val is not None:
            node = TreeNode(val)
            # print(val)
        else:
            node = None
        if index == 0:
            root = node
            node_list.append(root)
        else:

            if index%2:
                tmp = node_list[index//2]
                tmp.left = node
            else:
                tmp = node_list[index//2-1]
                tmp.right = node
            node_list.append(node)
    return root



class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            root.val += dfs(root.left) + dfs(root.right)
            self.moves += abs(root.val-1)
            # print(root.val, self.moves)
            return root.val-1
        self.moves = 0
        dfs(root)
        return self.moves

s = Solution()
node_val_list = [3,0,0]
root = Tree_Builds_BFS(node_val_list)
ans = 2
print(s.distributeCoins(root), ans)

node_val_list = [0,3,0]
root = Tree_Builds_BFS(node_val_list)
ans = 3
print(s.distributeCoins(root), ans)

node_val_list = [1,0,2]
root = Tree_Builds_BFS(node_val_list)
ans = 2
print(s.distributeCoins(root), ans)

node_val_list = [1,0,0,None,3]
root = Tree_Builds_BFS(node_val_list)
ans = 4
print(s.distributeCoins(root), ans)

node_val_list = [1]
root = Tree_Builds_BFS(node_val_list)
ans = 0
print(s.distributeCoins(root), ans)
"""
Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

 

Example 1:


Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
 

Constraints:

root is the root of a binary tree with n nodes and distinct node values from 1 to n.
n is odd.
1 <= x <= n <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root, n, x):
        """
        x can be extended to parent, left_child, or right_child, if any of these extension have nodes >= n//2+1, y can block that direction, so y wins.
        """
        def dfs(root):
            if not root:
                return 0
            return dfs(root.left) + dfs(root.right) + 1
        bfs = [root]
        while len(bfs) >0:
            bfs_2 = []
            for node in bfs:
                if node.val == x:
                    left = dfs(node.left)
                    right = dfs(node.right)
                    up = n - left - right - 1
                    return max(left, right, up) >= n//2 + 1
                else:
                    if node.left:
                        bfs_2.append(node.left)
                    if node.right:
                        bfs_2.append(node.right)
                bfs = bfs_2


class Solution:
    def btreeGameWinningMove(self, root, n, x):
        """
        x can be extended to parent, left_child, or right_child, if any of these extension have nodes >= n//2+1, y can block that direction, so y wins.
        """
        def dfs(root):
            if not root:
                return 0
            return dfs(root.left) + dfs(root.right) + 1

        def findVal(root,val):
            if not root:
                return None
            if root.val == val:
                return root
            left_node = findVal(root.left, val)
            right_node = findVal(root.right, val)
            if left_node:
                return left_node
            elif right_node :
                return right_node

        node_x = findVal(root, x)
        left = dfs(node.left)
        right = dfs(node.right)
        up = n - left - right - 1
        return max(left, right, up) >= n//2 + 1

"""
The data structure TreeNode is used for binary tree, but it can also used to represent a single linked list (where left is null, and right is the next node in the list). Implement a method to convert a binary search tree (implemented with TreeNode) into a single linked list. The values should be kept in order and the operation should be performed in place (that is, on the original data structure).

Return the head node of the linked list after converting.

Note: This problem is slightly different from the original one in the book.

 

Example:

Input:  [4,2,5,1,3,null,6,0]
Output:  [0,null,1,null,2,null,3,null,4,null,5,null,6]
Note:

The number of nodes will not exceed 100000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binode-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node] + dfs(node.right)

        if not root:
            return None
        node_list = dfs(root) + [None]
        head = node = node_list[0]
        node.left = None
        for i in range(1, len(node_list) - 1):
            tmp = node_list[i]
            tmp.left = None
            node.right = tmp
            node = node.right
        return head
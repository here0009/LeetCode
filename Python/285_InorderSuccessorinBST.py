"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/inorder-successor-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node)
                inorder(node.right)

        res = []
        inorder(root)
        res.append(None)
        index = 0
        while res[index] != p:
            index += 1
        return res[index+1]


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        curr = root
        stack = []
        while curr:
            if curr.val > p.val:
                stack.append(curr)
                curr = curr.left
            elif curr.val < p.val:
                curr = curr.right
            else:
                if curr.right:
                    tmp = curr.right
                    while tmp.left:
                        tmp = tmp.left
                    return tmp
                else:
                    if stack:
                        return stack.pop()
                    else:
                        return None
        return None

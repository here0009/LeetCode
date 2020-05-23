"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        pre_index = 1
        post_index = 0
        while post[post_index] != pre[1]:
            post_index += 1
        root.left = self.constructFromPrePost(pre[1:post_index+2], post[:post_index+1])
        root.right = self.constructFromPrePost(pre[post_index+2:], post[post_index+1:-1])
        return root

def treeLevel(root):
    """
    return the depth of the tree
    """

    if not root:
        return 0
    else:
        return 1+max(treeLevel(root.left),treeLevel(root.right))

from collections import deque
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
            new_q.append(tmp.left)
            new_q.append(tmp.right)
            print(level*' ', tmp.val, end='')
        print('\n')
        q = new_q
        level -= 1
    return
    

    

s = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
root = s.constructFromPrePost(pre, post)
print(root.val)
print(root.left.val)
print(root.left.right.val)
print(treeLevel(root))
printBinaryTree(root)
# pre = [1]
# post = [1]
# root = s.constructFromPrePost(pre, post)
# print(root.val)
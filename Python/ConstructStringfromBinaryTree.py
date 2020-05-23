"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \\  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""
# Definition for a binary tree node.
# Definition for a binary tree node.
def Tree_Builds_BFS(node_val_list):
    node_list = []
    if not node_val_list:
        return None
    for index, val in enumerate(node_val_list):
        if val:
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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, root: 'TreeNode') -> 'str':
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        if not root.left:
            return  str(root.val) + '()(' + self.tree2str(root.right) + ')'
        if root.left and root.right:
            return  str(root.val) + '(' + self.tree2str(root.left) + ')(' + self.tree2str(root.right) + ')'



s = Solution()

val_list = [1,2,3,4]
root = Tree_Builds_BFS(val_list)
print(s.tree2str(root))

val_list = [1,2,3,None,4]
root = Tree_Builds_BFS(val_list)
print(s.tree2str(root))

val_list = [1]
root = Tree_Builds_BFS(val_list)
print(s.tree2str(root))

val_list = []
root = Tree_Builds_BFS(val_list)
print(s.tree2str(root))
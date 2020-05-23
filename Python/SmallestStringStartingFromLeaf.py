"""
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

 

Example 1:



Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:



Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:



Input: [2,2,1,null,1,0,null,0]
Output: "abc"
 

Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root, string):
            if not root:
                return
            string = chr(int(root.val)+ord('a')) + string
            if not root.left and not root.right:
                if not res[0]:
                    res[0] = string
                else:
                    res[0] = min(res[0], string)
            dfs(root.left, string)
            dfs(root.right, string)

        res = [None]
        dfs(root, '')
        return res[0]


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root, string):
            if not root:
                return
            string = chr(int(root.val)+ord('a')) + string
            if not root.left and not root.right:
                self.res = min(self.res, string)
            else:
                dfs(root.left, string)
                dfs(root.right, string)

        self.res = chr(ord('z')+1)
        dfs(root, '')
        return self.res


def test(res):
    res_str = ''.join([chr(int(s)+ord('a')) for s in res[0]])
    return res_str

res = '310'
print(test(res))
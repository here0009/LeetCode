"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \\     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          []         
[[3,5,4],[2],[1]], [[3,4,5],[2],[1]], etc, are also consider correct answers since per each level it doesn't matter the order on which elements are returned.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-leaves-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode):
        def depth(node):
            if not node:
                return 0
            ld, rd = depth(node.left), depth(node.right)
            res = max(ld, rd) + 1
            depth_dict[res].append(node.val)
            return res

        depth_dict = defaultdict(list)
        depth(root)
        keys = sorted(depth_dict.keys())
        return [depth_dict[k] for k in keys]

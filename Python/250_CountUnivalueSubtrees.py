"""
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
 

Constraints:

The numbrt of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-univalue-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def dfs(node):
            """
            return a tuple, True if it is a unival subtree, the value, the counts
            """
            if not node:
                return True, None
            if not node.left and not node.right:
                counts[node.val] += 1
                return True, node.val
            isLeft, leftVal = dfs(node.left)
            isRight, rightVal = dfs(node.right)
            if not isLeft or not isRight:
                return False, None
            if isLeft and isRight:
                if leftVal == rightVal == node.val or (leftVal is None and rightVal == node.val) or (rightVal is None and leftVal == node.val):
                    counts[node.val] += 1
                    return True, node.val
                else:
                    return False, None

        counts = Counter()
        dfs(root)
        return sum(counts.values())

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.isUni = True

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        res, root.isUni = 0, True
        if root.left:
            res += self.countUnivalSubtrees(root.left)
            root.isUni &= (root.left.isUni and root.left.val == root.val)
        if root.right:
            res += self.countUnivalSubtrees(root.right)
            root.isUni &= (root.right.isUni and root.right.val == root.val)
        return res+1 if root.isUni else res


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def dfs(node):
            """
            return a tuple,  if it is a unival subtree  (True/False) and the unival subtree in it
            """
            if not node:
                return
            res, isUni = 0, True
            if node.left:
                left_res, left_isUni = dfs(node.left)
                res += left_res
                isUni &= (left_isUni and node.val == node.left.val)
            if node.right:
                right_res, right_isUni = dfs(node.right)
                res += right_res
                isUni &= (right_isUni and node.val == node.right.val)
            return res + isUni, isUni

        if not root:
            return 0
        return dfs(root)[0]
        
"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
 

Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        while len(s) >= 2 and s[0] == '(' and s[-1] == ')':
            s = s[1:-1]
        if not s:
            return None
        left, right = None, None
        p = 0
        for i, v in enumerate(s):
            if v == '(':
                p += 1
                if left is None:
                    left = i
            elif v == ')':
                p -= 1
                if p == 0 and right is None:
                    right = i
                    break
        if left and right:
            node = TreeNode(int(s[:left]))
            node.left = self.str2tree(s[left:right+1])
            node.right = self.str2tree(s[right+1:])
        else:
            node = TreeNode(int(s))
        return node


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        while len(s) >= 2 and s[0] == '(' and s[-1] == ')':
            s = s[1:-1]
        if not s:
            return None
        left = s.find('(')
        if left == -1:
            return TreeNode(int(s))
        p = 1
        for right in range(left+1, len(s)):
            if s[right] == '(':
                p += 1
            elif s[right] == ')':
                p -= 1
                if p == 0:
                    break
        node = TreeNode(int(s[:left]))
        node.left = self.str2tree(s[left:right+1])
        node.right = self.str2tree(s[right+1:])
        return node
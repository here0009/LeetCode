"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # def findChild(root, target):
        #     if root is target:
        #         return True
        #     if not root:
        #         return False
        #     return findChild(root.left, target) or findChild(root.right, target)

        def traceRoot(node):
            res = []
            while node:
                res.append(node)
                node = node.parent
            return res

        p_parent = traceRoot(p)
        q_parent_set = set(traceRoot(q))
        for node in p_parent:
            if node in q_parent_set:
                return node
        # if findChild(p, q):
        #     return p
        # if findChild(q, p):
        #     return q
        return None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def traceRoot(node):
            res = []
            while node:
                res.append(node)
                node = node.parent
            return res

        p_parent = traceRoot(p)
        q_parent_set = set(traceRoot(q))
        for node in p_parent:
            if node in q_parent_set:
                return node
        return None


[3,5,1,6,2,0,8,null,null,7,4]
5
1

[3,5,1,6,2,0,8,null,null,7,4]
5
4

[1,2]
1
2

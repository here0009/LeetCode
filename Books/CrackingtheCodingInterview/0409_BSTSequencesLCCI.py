"""
A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

Example:
Given the following tree:

        2
       / \
      1   3
Output:

[
   [2,1,3],
   [2,3,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bst-sequences-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        """
        like toplogical sort, if a node got no indegree, we add it to zero_degree
        enumerate node in zero_degree to form a path
        """
        def dfs(node):
            if not node:
                return
            one_degree.add(node)
            dfs(node.left)
            dfs(node.right)

        def genSeq(seq, curr, zero_degree, one_degree):
            zero_degree.remove(curr)
            seq.append(curr.val)
            if not zero_degree and not one_degree:
                self.res.append(seq)
            tmp = []
            for child in [curr.left, curr.right]:
                if child:
                    zero_degree.add(child)
                    one_degree.remove(child)
                    tmp.append(child)
            lst = list(zero_degree)
            for node in lst:
                genSeq(seq[:], node, zero_degree, one_degree)  # make a copy of seq
            zero_degree.add(curr)
            for node in tmp:
                zero_degree.remove(node)
                one_degree.add(node)

        if not root:
            return [[]]
        one_degree = set()
        dfs(root)
        # print([node.val for node in one_degree])
        one_degree.remove(root)
        zero_degree = set([root])
        self.res = []
        genSeq([], root, zero_degree, one_degree)
        return self.res

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:

        def genSeq(seq, nodes):
            if not nodes:
                self.res.append(seq)
                return
            for i, node in enumerate(nodes):
                n2 = nodes[:i] + nodes[i + 1:]
                s2 = seq + [node.val]
                if node.left:
                    n2.append(node.left)
                if node.right:
                    n2.append(node.right)
                genSeq(s2, n2)

        if not root:
            return [[]]
        self.res = []
        genSeq([], [root])
        return self.res

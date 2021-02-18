"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \\ 
      2    3
     / \\    \\ 
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        bfs = [tree]
        while bfs:
            l_nodes = [ListNode(node.val) for node in bfs]
            for i in range(len(l_nodes) - 1):
                l_nodes[i].next = l_nodes[i + 1]
            res.append(l_nodes[0])
            bfs2 = []
            for node in bfs:

                if node.left:
                    bfs2.append(node.left)
                if node.right:
                    bfs2.append(node.right)
            bfs = bfs2
        return res

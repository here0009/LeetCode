"""
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-subtree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return '#'
            return '@'.join([str(node.val), dfs(node.left), dfs(node.right)])

        def check(node):
            if not node:
                return '#'
            string = '@'.join([str(node.val), check(node.left), check(node.right)])
            # print(node.val, string)
            if string == t2_string:
                self.res = True
            return string

        t2_string = dfs(t2)
        # print(t2_string)
        self.res = False
        check(t1)
        return self.res

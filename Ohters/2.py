"""
小扣有一个根结点为 root 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 val 价值。小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 k 个，求所有染成蓝色的结点价值总和最大是多少？

示例 1：

输入：root = [5,2,3,4], k = 2

输出：12

解释：结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12
image.png

示例 2：

输入：root = [4,1,3,9,null,null,2], k = 2

输出：16

解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16
image.png

提示：

1 <= k <= 10
1 <= val <= 10000
1 <= 结点数量 <= 10000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def dfs(node):
            if not node:
                return 0, 0, 0
            lb, lk, lnb = dfs(node.left)
            rb, rk, rnb = dfs(node.right)
            if lnb >= lb:
                lb, lk = lnb, 0
            if rnb >= rb:
                rb, rk = rnb, 0
            resb = lnb + rnb + node.val
            resk = 1
            bk_list = [(lnb + rnb + node.val, 1), (lb + rb + node.val, lk + rk + 1), (lb + 1, lk + 1), (rb + 1, rk + 1)]
            bk_list = [(_b, _k) for _b, _k in bk_list if _k <= k]
            bk_list.sort(key=lambda x: (-x[0], x[1]))
            resb, resk = bk_list[0]
            resnb = max(lb, lnb) + max(rb, rnb)
            return resb, resk, resnb

        b, k, nb = dfs(root)
        return max(b, nb)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def dfs(node):
            res = [0] * (k + 1)
            if not node:
                return res
            l_list = dfs(node.left)
            r_list = dfs(node.right)
            res[0] = l_list[-1] + r_list[-1]
            for i in range(1, k + 1):
                for left in range(i):
                    right = i - left - 1
                    res[i] = max(res[i], l_list[left] + r_list[right] + node.val)
                res[i] = max(res[i], res[i - 1])
            return res

        return dfs(root)[-1]

[4,1,3,9,null,null,2]
2
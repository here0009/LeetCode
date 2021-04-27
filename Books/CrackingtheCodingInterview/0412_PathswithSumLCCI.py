"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \\    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_val: int) -> int:
        """
        wrong answer
        """

        def dfs(node):
            if not node:
                return [[0]]
            left_lst = dfs(node.left)
            right_lst = dfs(node.right)
            if left_lst == [[0]]:
                total = right_lst
            elif right_lst == [[0]]:
                total = left_lst
            else:
                total = left_lst + right_lst
            res = []
            print(node.val, total)
            for lst in total:
                num = lst[-1] + node.val
                for i, v in enumerate(lst):
                    if num - sum_val == v:
                        self.res += 1
                lst.append(num)
                res.append(lst)
            return res

        self.res = 0
        dfs(root)
        return self.res


import copy
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum_val: int) -> int:

        def dfs(node, lst, val_dict):
            if not node:
                return
            print(node.val, lst, val_dict)

            v = lst[-1] + node.val
            lst.append(v)
            if v - sum_val in val_dict:
                for i in val_dict[v - sum_val]:
                    tmp = []
                    for j in range(i + 1, len(lst)):
                        tmp.append(lst[j] - lst[j - 1])
                    self.res.append(tmp)
            val_dict[v].append(len(lst) - 1)
            dfs(node.left, lst[:], copy.deepcopy(val_dict))
            dfs(node.right, lst[:], copy.deepcopy(val_dict))

        self.res = []
        val_dict = defaultdict(list)
        val_dict[0].append(0)
        dfs(root, [0], val_dict)
        return self.res


import copy
from collections import Counter
class Solution:
    def pathSum(self, root: TreeNode, sum_val: int) -> int:

        def dfs(node, total, counts):
            if not node:
                return
            total += node.val
            self.res += counts[total - sum_val]
            counts[total] += 1
            dfs(node.left, total, copy.copy(counts))
            dfs(node.right, total, copy.copy(counts))

        self.res = 0
        dfs(root, 0, Counter([0]))
        return self.res

S = Solution()
print(S.pathSum(root, sum_val))
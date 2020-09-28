"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import heapq
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int):
        def dfs(node):
            if node:
                heapq.heappush(pq, (abs(target - node.val), node.val))
                dfs(node.left)
                dfs(node.right)

        pq = []
        heapq.heapify(pq)
        dfs(root)
        res = []
        while k > 0:
            res.append(heapq.heappop(pq)[1])
            k -= 1
        return res


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int):
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []

        lst = inOrder(root)
        left, right = 0, len(lst)
        while right - left > k:
            if target - lst[left] > lst[right-1] - target:
                left += 1
            else:
                right -= 1
        return lst[left : right]


from collections import deque
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            retrun 
        res = deque([])
        self.inorder(root, target, k, res)
        return list (res)

    def inorder(self, root, target, k, res):
        """
        the traverse was did inorder, so the res is inordered
        """
        if not root:
            return
        self.inorder(root.left, target, k, res)
        if k > len(res):
            res.append(root.val)
        elif abs(res[0] - target) > abs(root.val - target):
            res.popleft()
            res.append(root.val)
        else:
            return
        self.inorder(root.right, target, k, res)

# 作者：fabriceli
# 链接：https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/solution/fei-di-gui-jie-fa-di-gui-jie-fa-shuang-zhi-zhen-ji/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
folow up
"""


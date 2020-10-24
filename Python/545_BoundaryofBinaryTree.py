"""
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \\          / 
4   5        6   
   / \\      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boundary-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        """
        wrong answer
        """
        if not root:
            return []
        left_lst = []
        right_lst = []
        leaves = []
        bfs = [(root, 0)]  # 0 for left and 1 for right
        while bfs:
            # print(bfs)
            bfs2 = []
            if len(bfs) == 1:
                node, sign = bfs[0]
                if sign == 0:
                    left_lst.append(node.val)
                else:
                    right_lst.append(node.val)
            else:
                left_lst.append(bfs[0][0].val)
                right_lst.append(bfs[-1][0].val)

            for node, _ in bfs[1:-1]:
                if not node.left and not node.right:
                    leaves.append(node.val)
            for node, _ in bfs:
                if node.left:
                    bfs2.append((node.left, 0))
                if node.right:
                    bfs2.append((node.right, 1))
            bfs = bfs2
        return left_lst + leaves + right_lst[::-1]




class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        """
        wrong answer
        """
        if not root:
            return []
        left_lst = []
        right_lst = []
        leaves = []
        left_set, right_set = set(), set()
        tmp = root
        if tmp.left:
            while tmp:
                left_lst.append(tmp.val)
                left_set.add(tmp)
                if tmp.left:
                    tmp = tmp.left
                elif tmp.right:
                    tmp = tmp.right
                else:
                    break
        else:
            left_set.add(root)
            left_lst = [root.val]
        tmp = root
        if tmp.right:
            while tmp:
                right_set.add(tmp)
                right_lst.append(tmp.val)
                if tmp.right:
                    tmp = tmp.right
                elif tmp.left:
                    tmp = tmp.left
                else:
                    break
        else:
            right_set.add(root)
            right_lst = [root.val]
        bfs = [root]
        while bfs:
            bfs2 = []
            for node in bfs:
                if node.left:
                    bfs2.append(node.left)
                if node.right:
                    bfs2.append(node.right)
            for node in bfs:
                if not node.left and not node.right:
                    if node not in left_set and node not in right_set:
                        leaves.append(node.val)
            bfs = bfs2
        return left_lst + leaves + right_lst[1:][::-1]


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        """
        wrong answer
        """
        if not root:
            return []
        left_lst = [root.val]
        right_lst = []
        leaves = []
        visited = {root}
        isLeft, isRight = 1, 1
        bfs = [root]
        if not root.left:
            isLeft = 0
        if not root.right:
            isRight = 0

        while bfs:
            if not isLeft and bfs[-1] not in visited:
                visited.add(bfs[-1])
                right_lst.append(bfs[-1].val)
            else:
                if bfs[0] not in visited:
                    visited.add(bfs[0])
                    left_lst.append(bfs[0].val)
                if isRight and bfs[-1] not in visited:
                    visited.add(bfs[-1])
                    right_lst.append(bfs[-1].val)
            bfs2 = []
            for node in bfs:
                if not node.left and not node.right and node not in visited:
                    visited.add(node)
                    leaves.append(node.val)
                if node.left:
                    bfs2.append(node.left)
                if node.right:
                    bfs2.append(node.right)
            bfs = bfs2
        return left_lst + leaves + right_lst[::-1]


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        """
        wrong answer
        """
        def insert(node, flag):
            if node is None:
                return
            bfs = [node]
            while bfs:
                bfs2 = []
                start, end = 0, len(bfs)
                if flag == 0:
                    left_lst.append(bfs[0].val)
                    start += 1
                else:
                    right_lst.append(bfs[-1].val)
                    end -= 1
                for i in range(start, end):
                    node = bfs[i]
                    if not node.left and not node.right:
                        leaves.append(node.val)
                for node in bfs:
                    if node.left:
                        bfs2.append(node.left)
                    if node.right:
                        bfs2.append(node.right)
                bfs = bfs2

        if not root:
            return []
        left_lst, right_lst, leaves = [root.val], [], []
        insert(root.left, 0)
        insert(root.right, 1)
        return left_lst + leaves + right_lst[::-1]


# 作者：ben-zhi-fei-zhai
# 链接：https://leetcode-cn.com/problems/boundary-of-binary-tree/solution/gen-jie-dian-xu-te-shu-chu-li-fen-bie-bian-li-zuo-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        """
        向左走之后，不会再向右
        """
        def dfs_left(node):
            if node:
                if node.left:
                    res.append(node.val)
                    dfs_left(node.left)
                elif node.right:
                    res.append(node.val)
                    dfs_left(node.right)

        def dfs_right(node):
            if node:
                if node.right:
                    stack.append(node.val)
                    dfs_right(node.right)
                elif node.left:
                    stack.append(node.val)
                    dfs_right(node.left)

        def dfs_leaves(node):
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                dfs_leaves(node.left)
                dfs_leaves(node.right)

        if not root:
            return []
        res, stack = [root.val], []
        if not root.left and not root.right:
            return res
        if root.left:
            dfs_left(root.left)
        dfs_leaves(root)
        if root.right:
            dfs_right(root.right)
        return res + stack[::-1]


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs_left(node):
            if not node:
                return
            if node.left:
                rt.append(node.val)
                dfs_left(node.left)
            elif node.right:
                rt.append(node.val)
                dfs_left(node.right)

        def dfs_right(node):
            if not node:
                return
            if node.right:
                stack.append(node.val)
                dfs_right(node.right)
            elif node.left:
                stack.append(node.val)
                dfs_right(node.left)

        def dfs_leaf(node):
            if not node:
                return
            if (not node.left) and (not node.right):
                rt.append(node.val)
            dfs_leaf(node.left)
            dfs_leaf(node.right)

        if not root:
            return []
        rt, stack = [root.val], []
        # 如果根节点无左右子树，则直接返回
        if not root.left and not root.right:
            return rt
        # 如果根节点无左子树，则直接跳过左边界
        if root.left: 
            dfs_left(root.left)
        dfs_leaf(root)
        # 如果根节点无右子树，则直接跳过右边界
        if root.right:  
            dfs_right(root.right)
        return rt + stack[::-1]



l1 = [-64,12,-4,-51,-31,-81,-53,33,78,60,8,-59,-51,-67,-88,-85,67,-17,-77,56,-88,-33,-40,24,92,72,-54,-66,-36,-72,43,-92,-98,-93,98,-84,-67,-53,37,-4,67,74,11,53,3,76,18]

l2 = [-64,12,-4,-51,-31,-81,33,-53,78,8,-67,-33,-54,-66,-36,-72,-85,43,-40,-92,-93,-98,-88,24,67,92,72,98,-17,-77,-59,56,-84,-88,-53,37,-4,-51,67,60,74,11,53,3,76,18]
print(len(l1), len(l2))
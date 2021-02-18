"""
Given the root of a binary tree and a leaf node, reroot the tree so that the leaf is the new root.

You can reroot the tree with the following steps for each node cur on the path starting from the leaf up to the root​​​ excluding the root:

If cur has a left child, then that child becomes cur's right child.
cur's original parent becomes cur's left child. Note that in this process the original parent's pointer to cur becomes null, making it have at most one child.
Return the new root of the rerooted tree.

Note: Ensure that your solution sets the Node.parent pointers correctly after rerooting or you will receive "Wrong Answer".

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
Output: [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
Output: [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
-109 <= Node.val <= 109
All Node.val are unique.
leaf exist in the tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree
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
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        """
        wrong answer
        """
        def dfs(node):
            if not node:
                return None, False
            if node == leaf:
                return ufs(node, node.parent)
            dfs(node.left)
            dfs(node.right)

        def ufs(node, parent):
            if node.left:
                node.right = node.left
            if parent.parent :
                node.left = ufs(parent, parent.parent)
                parent.parent = node
            return node

        return dfs(root)


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# 作者：goldfish_hcy
# 链接：https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree/solution/li-qing-ti-yi-zhu-yi-xi-jie-by-goldfish_hcy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        if root is leaf:
            return root
        
        node = leaf
        leaf.left, leaf.parent = leaf.parent, None
        while node.left is not root:
            if node.left.right is node:
                node.left.right = node.left.left
            
            node.left.left = node.left.parent
            node.left.parent = node
            node = node.left
        
        if node.left.left is node:
            node.left.left = None
        else:
            node.left.right = None
            
        node.left.parent = node
        return leaf
# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree/solution/python-kan-liao-ban-tian-cai-kan-dong-ti-mu-shuo-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        nodes = []
        cur = leaf
        while cur:
            nodes.append(cur)
            cur = cur.parent

        for i in range(len(nodes) - 1, -1, -1):
            cur = nodes[i]
            orig_left = cur.left
            cur.left = cur.parent
            if i >= 1 and cur.right == nodes[i - 1]:
                cur.right = orig_left

                if i == len(nodes)-1:
                    cur.left, cur.right = cur.right, cur.left
            cur.parent = nodes[i-1] if i >= 1 else None

        return leaf

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# 作者：user5788R
# 链接：https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree/solution/zhong-gui-zhong-ju-dfs-de-yi-xie-bian-xi-770c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        self.root = root
        self.res = leaf
        self.dfs(leaf.parent, leaf, None)
        return self.res

    def dfs(self, p, leaf, np):
        if not p:
            return None
        gp = p.parent
        if p.left == leaf:
            p.left = None
        else:
            if p == self.root:
                p.right = None
            else:
                p.right = p.left
                p.left = None

        p.parent = leaf
        leaf.left = p
        leaf.parent = np
        self.dfs(gp, p, leaf)

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        path = []
        node = leaf
        while node:
            path.append(node)
            node = node.parent
        print([node.val for node in path])
        pre = None
        while path:
            node = path.pop()
            print(node.val)
            if path:
                nxt = path[-1]
                if node.right == nxt:
                    node.right = node.left
                node.parent = nxt
                nxt.left = node
                node.left = pre
            pre = node
        node.parent = None
        return node


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        path = []
        node = leaf
        while node:
            path.append(node)
            node = node.parent
        print([node.val for node in path])
        # pre = path.pop()
        pre = None
        while path:
            node = path.pop()
            if node is root:
                if path and path[-1] is node.right:
                    node.right = None
                else:
                    node.left = None
            else:
                if path and path[-1] is node.right:
                    node.right = node.left
            if pre:
                pre.parent = node
                node.left = pre
            pre = node
        node.parent = None
        return node


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        if root == leaf:
            return root
        path = []
        node = leaf
        while node:
            path.append(node)
            node = node.parent
        pre = path.pop()  # root, root got at least one child
        if path[-1] is pre.right:
            pre.right = None
        else:
            pre.left = None
        while path:
            node = path.pop()
            if path and path[-1] is node.right:
                node.right = node.left
            pre.parent = node
            node.left = pre
            pre = node
        node.parent = None
        return node

# [3,5,1,6,2,0,8,null,null,7,4]
# 7
# [3,5,1,6,2,0,8,null,null,7,4]
# 0
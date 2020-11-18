"""
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy.

 

Example 1:


Input: root = [[1,null],null,[4,3],[7,0]]
Output: [[1,null],null,[4,3],[7,0]]
Explanation: The original binary tree is [1,null,4,7].
The random pointer of node one is null, so it is represented as [1, null].
The random pointer of node 4 is node 7, so it is represented as [4, 3] where 3 is the index of node 7 in the tree array.
The random pointer of node 7 is node 1, so it is represented as [7, 0] where 0 is the index of node 1 in the tree array
Example 2:


Input: root = [[1,4],null,[1,0],null,[1,5],[1,5]]
Output: [[1,4],null,[1,0],null,[1,5],[1,5]]
Explanation: The random pointer of a node can be the node itself.
Example 3:


Input: root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Output: [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Example 4:

Input: root = []
Output: []
Example 5:

Input: root = [[1,null],null,[2,null],null,[1,null]]
Output: [[1,null],null,[2,null],null,[1,null]]
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
Each node's value is between [1, 10^6].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/clone-binary-tree-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        """
        Thoughts: construc the tree 1st, then add random pointer
        """
        def deepCopy(node):
            if not node:
                return None
            left = deepCopy(node.left)
            right = deepCopy(node.right)
            return NodeCopy(node.val, left, right, None)

        def addPointer(node):

        copy_root = deepCopy(root)
        bfs = [copy_root]
        node_list = []
        while bfs:
            bfs2 = []
            node_list.extend(bfs)
            for node in bfs:
                if not node or (not node.left and not node.right):
                    continue
                bfs2.append(node.left)
                bfs2.append(node.right)


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':

        def deepCopy(node):
            if not node:
                return None
            if node in seen:
                return seen[node]
            copy_node = NodeCopy(node.val)
            seen[node] = copy_node  # a pointer to copy node, change copy node will change seen[node]
            copy_node.left = deepCopy(node.left)
            copy_node.right = deepCopy(node.right)
            copy_node.random = deepCopy(node.random)
            return copy_node

        seen = dict()
        return deepCopy(root)
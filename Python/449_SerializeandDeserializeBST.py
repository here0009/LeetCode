"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def strfy(node):
            if node is None:
                return ''
            left_string = strfy(node.left)
            right_string = strfy(node.right)
            return str(node.val) + '$' + left_string + right_string
        res = strfy(root)
        # print(res)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        e.g.: 7$2$5$9$8$10$
        """
        def tree(lst):
            if not lst:
                return None
            node = TreeNode(lst[0])
            index = 1
            while index < len(lst) and lst[index] <= lst[0]:
                index += 1
            node.left = tree(lst[1:index])
            node.right = tree(lst[index:])
            return node

        lst = [int(i) for i in data.split('$') if len(i) > 0]
        # print(lst)
        return tree(lst)



        

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
string = '7$2$5$9$8$10$'
print(string.split('$'))
root = codec.deserialize(string)
print(root.val)
print(codec.serialize(root))
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec_1:
    def treeNode(self,val):
        if val is None:
            return None
        else:
            return TreeNode(val)

    def construcTree(self,vals):
        v_root = TreeNode(vals[0])
        bfs = deque([v_root])
        index = 0
        len_v = len(vals)
        while bfs and index < len_v:
            node = bfs.popleft()
            if index+1 < len_v:
                node.left = self.treeNode(vals[index+1])
            if index+2 < len_v:
                node.right = self.treeNode(vals[index+2])
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
            index += 2
        return v_root

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return str([])
        bfs = [root]
        res = []
        while not all(node is None for node in bfs):
            bfs2 = []
            res.extend([node.val if node else None for node in bfs])
            for node in bfs:
                if node:
                    bfs2.append(node.left)
                    bfs2.append(node.right)
            bfs = bfs2
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if len(data) == 0:
            return None
        vals = []
        for s in data.split(','):
            if s.strip() == 'None':
                vals.append(None)
            else:
                vals.append(int(s))
        # vals = [int(s) if s.strip().isdigit() else None for s in  data.split(',')] #strip() take off extra space
        # print('vals',vals)
        root = self.construcTree(vals)
        return root

# codec = Codec_1()

# data = "[-1,0,1]"
# root = codec.deserialize(data)
# print('root.val:',root.val)
# print('root.left.val:',root.left.val)
# print(codec.serialize(root))
# # print('string:',string)
# print(codec.deserialize(codec.serialize(root)).val)


# data = "[1,2,3,None,None,4,5]"

# root = codec.deserialize(data)
# print('root.val:',root.val)
# print('root.left.val:',root.left.val)
# print(codec.serialize(root))
# # print('string:',string)
# print(codec.deserialize(codec.serialize(root)).val)


# data = '[1,2,None,3,None,4,None,5]'
# root = codec.deserialize(data)
# print('root.val:',root.val)
# print('root.left.val:',root.left.val)
# print(codec.serialize(root))
# # print('string:',string)
# print(codec.deserialize(codec.serialize(root)).val)         

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = [root.val] + [self.serialize(root.left)] + [self.serialize(root.right)] 
        # print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        root.left = self.deserialize(data[1])   
        root.right = self.deserialize(data[2])
        return root 

# Your Codec object will be instantiated and called as such:
codec = Codec()

data = [-1,[1,[],[]],[0,[],[]]]
root = codec.deserialize(data)
print('root.val:',root.val)
print('root.left.val:',root.left.val)
print(codec.serialize(root))
# print('string:',string)
print(codec.deserialize(codec.serialize(root)).val)



data = [1, [2, [], []], [3, [4, [], []], [5, [], []]]]
root = codec.deserialize(data)
print('root.val:',root.val)
print('root.left.val:',root.left.val)
print(codec.serialize(root))
# print('string:',string)
print(codec.deserialize(codec.serialize(root)).val)


# data = '[1,2,None,3,None,4,None,5]'
# root = codec.deserialize(data)
# print('root.val:',root.val)
# print('root.left.val:',root.left.val)
# print(codec.serialize(root))
# # print('string:',string)
# print(codec.deserialize(codec.serialize(root)).val)
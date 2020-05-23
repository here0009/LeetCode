"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:



Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:



Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 

Example 3:



Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def recoverFromPreorder(self, string: str) -> TreeNode:
        len_s = len(string)
        index = 0
        stack = [] #root store at stack[0], root.left store at stack[1], when encounter root.right, use it to replace root.left
        depth = 0
        while index < len_s:
            len_d = 0
            if string[index].isdigit():
                while index+len_d < len_s and string[index+len_d].isdigit():
                    len_d += 1
                node = TreeNode(int(string[index:index+len_d]))
                # print(string[index], node.val)
                if depth == len(stack): #depth is the same as len(stack), so we need to append a new layer, and node is left child the stack[-1]
                    if depth > 0: #if it is not the root
                        stack[-1].left = node 
                    stack.append(node)
                elif depth < len(stack): #depth is smaller than len(stack), we need to pop stack until meet the parent of current ndoe
                    while depth < len(stack):
                        stack.pop() 
                    stack[-1].right = node
                    stack.append(node) #right node replace left node
            elif string[index] == '-':
                while index+len_d < len_s and string[index+len_d] == '-':
                    len_d += 1
                depth = len_d
                # print(string[index],depth*'-')
            index += len_d
        return stack[0]

import re
class Solution_2:
    def recoverFromPreorder(self, string: str) -> TreeNode:
        # for k in re.findall('((-*)(\\d+))', string):
        #     print(k)

        vals = [(len(k[1]), int(k[2])) for k in re.findall('((-*)(\\d+))', string)][::-1]
        # print(vals)
        def fn(level):
            if not vals or level != vals[-1][0]:
                return None
            node = TreeNode(vals.pop()[1])
            node.left = fn(level+1)
            node.right = fn(level+1)
            return node
        return fn(0)

class Solution:
    def recoverFromPreorder(self, string: str) -> TreeNode:
        stack, index = [], 0
        len_s = len(string)
        while index < len_s:
            level, val = 0, ''
            while index < len_s and string[index] == '-':
                level, index = level+1, index+1
            while index < len_s and string[index].isdigit():
                val, index = val+string[index], index+1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(int(val))
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]



S = Solution()
string = "1-2--3--4-5--6--7"
root = S.recoverFromPreorder(string)
print(root.val)
print(root.left.left.val)
# print(root.right.right.val)
string = "1-2--3---4-5--6---7"
root = S.recoverFromPreorder(string)
print(root.val)
print(root.left.left.val)
# print(S.recoverFromPreorder(string))
string = "1-401--349---90--88"
root = S.recoverFromPreorder(string)
print(root.val)
print(root.left.left.val)
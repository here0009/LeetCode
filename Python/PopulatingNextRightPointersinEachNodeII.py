"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:



Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None
        bfs = [root]
        while len(bfs) > 0:
            bfs_2 = []
            for i in range(len(bfs)-1):
                bfs[i].next = bfs[i+1]
            for node in bfs:
                if node.left:
                    bfs_2.append(node.left)
                if node.right:
                    bfs_2.append(node.right)
            bfs = bfs_2
        return root

# test_case = {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

{"$id":"1","val":1,"left":{"$id":"2","val":2,"left":{"$id":"3","val":4,"left":null,"right":null,"next":{"$id":"4","val":5,"left":null,"right":null,"next":{"$id":"5","val":7,"left":null,"right":null,"next":null}}},"right":{"$ref":"4"},"next":{"$id":"6","val":3,"left":null,"right":{"$ref":"5"},"next":null}},"right":{"$ref":"6"},"next":null}

# expected = {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
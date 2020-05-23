"""
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class BSTNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, node):
        if node.val > self.val:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        if node.val < self.val:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node

class Solution:
    def nextLargerNodes(self, head: ListNode):
        """
        Thoughts: convert listNode to BST, the next greater node will be the left child of a node
        It is not very eazy to solve the problem using BST, try to use stack
        """
        res = []
        copy_head = head
        root = BSTNode(head.val)
        head = head.next
        while head:
            node = BSTNode(head.val)
            root.insert(node)
            head = head.next
        
        # for node in 
        pass

from collections import deque
class Solution:
    def nextLargerNodes(self, head: ListNode):
        q = deque()
        res = []
        copy_head = head
        index = 0
        # print(q)
        while head:
            while q and head.val > q[-1][1]:
                # print(q)
                res[q[-1][0]] = head.val
                q.pop()
            q.append((index,head.val))
            res.append(0)
            head = head.next
            index += 1
        return res
                

            
        


def construtListNode(A):
    head = ListNode(A[0])
    copy_head = head
    for n in A[1:]:
        tmp_node = ListNode(n)
        head.next = tmp_node
        head = tmp_node
    return copy_head

s = Solution()

A = [2,1,5]
head = construtListNode(A)
print(s.nextLargerNodes(head))

A = [2,7,4,3,5]
head = construtListNode(A)
print(s.nextLargerNodes(head))

A = [1,7,5,1,9,2,5,1]
head = construtListNode(A) 
print(s.nextLargerNodes(head))
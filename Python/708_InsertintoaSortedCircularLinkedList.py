"""
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

 

Example 1:


 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]
 

Constraints:

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)
        if not head:  # no head
            insertNode.next = insertNode
            return insertNode
        node = head
        if node.next is node:  # only one node
            node.next = insertNode
            insertNode.next = node
            return head
        min_v = max_v = node.val
        while node.next is not head:
            node = node.next
            min_v = min(min_v, node.val)
            max_v = max(max_v, node.val)
        if insertVal >= max_v:  # insertval is the max one
            while node.val != max_v:
                node = node.next
        elif insertVal <= min_v:  # insertval is the min one
            while node.next.val != min_v:
                node = node.next
        else:  # insertval between vals in list
            while not node.val <= insertVal <= node.next.val:
                node = node.next
        next_node = node.next
        node.next = insertNode
        insertNode.next = next_node
        return head


# test case
# [3,3,3]
# 0
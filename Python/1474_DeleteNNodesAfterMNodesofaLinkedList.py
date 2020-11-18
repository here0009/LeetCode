"""
Given the head of a linked list and two integers m and n. Traverse the linked list and remove some nodes in the following way:

Start with the head as the current node.
Keep the first m nodes starting with the current node.
Remove the next n nodes
Keep repeating steps 2 and 3 until you reach the end of the list.
Return the head of the modified list after removing the mentioned nodes.

Follow up question: How can you solve this problem by modifying the list in-place?

 

Example 1:



Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
Output: [1,2,6,7,11,12]
Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  (1 ->2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
Continue with the same procedure until reaching the tail of the Linked List.
Head of linked list after removing nodes is returned.
Example 2:



Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
Output: [1,5,9]
Explanation: Head of linked list after removing nodes is returned.
Example 3:

Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
Output: [1,2,3,5,6,7,9,10,11]
Example 4:

Input: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
Output: [9,7,8]
 

Constraints:

The given linked list will contain between 1 and 10^4 nodes.
The value of each node in the linked list will be in the range [1, 10^6].
1 <= m,n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        node = head
        counts = 0
        while node and counts < m-1:
            node = node.next
            counts += 1
        tail = node
        counts = 0
        while node and counts < n+1:
            node = node.next
            counts += 1
        if tail:
            tail.next = self.deleteNodes(node, m, n)
        return head


# 作者：HUST_PDE_YCX
# 链接：https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/solution/1474-shan-chu-lian-biao-m-ge-jie-dian-zhi-hou-de-n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            p,q = m,n
            while p > 0 and cur.next:
                p -= 1
                cur = cur.next
            while q > 0 and cur.next:     
                q -= 1
                cur.next = cur.next.next   # 直接改变cur的后继结点。

        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_num = 0
        tmp = head
        while tmp:
            node_num += 1
            tmp = tmp.next

        middleNum = node_num//2 + 1
        tmp2 = head
        for i in range(1, middleNum):
            tmp2 = tmp2.next
        return tmp2

node_list = list()

for i in range(1, 7):
    node_list.append(ListNode(i))

for i in range(5):
    node_list[i].next = node_list[i+1]

head = node_list[0]      
while head:
    print(head.val)
    head = head.next

s = Solution()

print("+++++++++++++")
print(node_list[0].val)
print((s.middleNode(node_list[0])).val)
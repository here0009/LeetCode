# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # sep = "->"
        # list_l1 = l1.split(sep)
        # list_l2 = l2.split(sep)
        list_l1 = list(l1)
        list_l2 = list(l2)
        output_list = []
        i = 0
        j = 0
        l1_len = len(list_l1)
        l2_len = len(list_l2)
        while (i < l1_len and j < l2_len):
            if list_l1[i] <= list_l2[j]:
                output_list.append(list_l1[i])
                i+=1
            else:
                output_list.append(list_l2[j])
                j+=1
        if i < l1_len:
            for k  in range(i, l1_len):
                output_list.append(list_l1[k])

        if j < l2_len:
            for k  in range(j, l2_len):
                output_list.append(list_l1[k])

        # return sep.join(output_list)
        return output_list

class Solution:
    def constructListNode(self, input_list):
        root = ListNode(0)
        curr = root
        for i in range(len(input_list)):
            curr.next = ListNode(input_list[i])
            curr = curr.next
        return root.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        curr = root
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return root.next



s = Solution()
s1 = [1,2,4]
s2 = [1,3,4]
s1 = s.constructListNode(s1)
s2 = s.constructListNode(s2)
res = s.mergeTwoLists(s1, s2)
print(res.val, res.next.val, res.next.next.val)
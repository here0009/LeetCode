"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        lt = []
        while head:
            lt.append(head.val)
            head = head.next
        len_lt = len(lt)
        k = k % len_lt
        lt2 = lt[len_lt-k:] + lt[:len_lt-k]
        print(lt2)
        head = ListNode(lt2[0])
        res = head
        for i in range(1,len_lt):
            head.next = ListNode(lt2[i])
            head = head.next
        return res


class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        counts = 0
        p = q = head
        while head.next:
            counts += 1
            head = head.next
        head.next = q
        k = k % counts
        for _ in range(counts-k-1):
            p = p.next
        res = p.next
        p.next = None
        return res

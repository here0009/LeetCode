"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq        
class Solution:
    def mergeKLists(self, lists):
        res = ListNode()
        node = res
        q = []
        for index, ln in enumerate(lists):
            if ln is not None:
                heapq.heappush(q, (ln.val, index))
                lists[index] = lists[index].next
        # print('start q',q)
        while q:
            # print(q)
            val, index = heapq.heappop(q)
            node.next = ListNode(val)
            node = node.next
            if lists[index] is not None:
                heapq.heappush(q, (lists[index].val, index))
                lists[index] = lists[index].next
        return res.next


#https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
import heapq     
class Solution:
    def mergeKLists(self, lists):
        ## If two elements have the same val, the next tuple items will be compared:
        ## "i" in the below code, which is guaranteed to be unique. 
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next: # exhausted one linked-list
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next)) # recycling tie-breaker i guarantees uniqueness
            curr.next = node    
            curr = curr.next
        return dummy.next

# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-concise-divide-and-conquer-solution.
class Solution:
    def mergeKLists(self, lists):
        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            curr.next = left or right
            return dummy.next
                

        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        left_list = self.mergeKLists(lists[:mid])
        right_list = self.mergeKLists(lists[mid:])
        return merge(left_list, right_list)

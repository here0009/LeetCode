"""
编写一个函数，检查输入的链表是否是回文的。

 

示例 1：

输入： 1->2
输出： false 
示例 2：

输入： 1->2->2->1
输出： true 
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        wrong for test case [1,3,0,2]
        """
        length = 0
        node = head
        val = 0
        while node:
            length += 1
            val ^= node.val
            node = node.next
        if length % 2 == 0:
            target = 0
        else:
            mid = length // 2
            node = head
            i = 0
            while i < mid: 
                i += 1
                node = node.next
            target = node.val
        # print(target, val)
        return val == target


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        mid = len(vals) // 2
        for i in range(mid):
            if vals[i] != vals[~i]:
                return False
        return True

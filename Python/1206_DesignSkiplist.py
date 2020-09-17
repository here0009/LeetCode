"""
Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists are just simple linked lists.

For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way:


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add , erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

To be specific, your design should include these functions:

bool search(int target) : Return whether the target exists in the Skiplist or not.
void add(int num): Insert a value into the SkipList. 
bool erase(int num): Remove a value in the Skiplist. If num does not exist in the Skiplist, do nothing and return false. If there exists multiple num values, removing any one of them is fine.
See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

 

Example:

Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return false.
skiplist.add(4);
skiplist.search(1);   // return true.
skiplist.erase(0);    // return false, 0 is not in skiplist.
skiplist.erase(1);    // return true.
skiplist.search(1);   // return false, 1 has already been erased.
 

Constraints:

0 <= num, target <= 20000
At most 50000 calls will be made to search, add, and erase.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

# https://leetcode.com/problems/design-skiplist/discuss/500036/python-nodes-with-two-pointers
from collections import deque
import random
class Skiplist:
    def __init__(self, levels = 30):
        self.heads = [Node(-float('inf')) for _ in range(levels)]
        for c,n in zip(self.heads, self.heads[1:]): # the lenght of zipped elements can be different
            c.down = n

    def search(self, target) -> bool:
        curr = self.heads[0] #-inf
        while curr:
            if curr.next is None or curr.val < target <= curr.next.val:
                if curr.next and target == curr.next.val:
                    return True
                curr = curr.down
            else:
                curr = curr.next
        return False

    def add(self, num: int) -> None:
        stack, curr, pre = deque([]), self.heads[0], None
        while curr:
            if curr.next is None or curr.val < num <= curr.next.val:
                stack.append(curr)
                curr = curr.down
            else:
                curr = curr.next

        while stack:
            curr = stack.pop()
            node = Node(num)
            node.next, curr.next = curr.next, node
            if pre:
                node.down = pre
            pre = node
            if random.randint(0, len(self.heads)-1) < len(self.heads)-1: #randint(0, len(self.heads)-1) equals to randrange(0, len(heads)), continue only 1/len(self.heads)
                break

    def erase(self, num: int) -> bool:
        b, curr = False, self.heads[0]
        while curr:
            if curr.next is None or curr.val < num <= curr.next.val:
                if curr.next and curr.next.val == num:
                    b, curr.next = True, curr.next.next
                curr = curr.down
            else:
                curr = curr.next
        return b
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
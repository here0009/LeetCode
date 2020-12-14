"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        tmp = self.head
        if not tmp:
            return -1
        counts = 0
        while counts < index:
            tmp = tmp.next
            counts += 1
            if not tmp:
                return -1
        return tmp.val

        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        tmp = Node(val)
        tmp.next = self.head
        self.head = tmp
        if not self.tail:
            self.tail = tmp
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        tmp = Node(val)
        self.tail.next = tmp
        self.tail = tmp
        if not self.head:
            self.head = tmp
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        tmp = self.head
        insert_node = Node(val)
        if index == 0:
            self.head = tmp
        for i in range(1, index):
            if tmp:
                tmp = tmp.next
            else:
                return

        if tmp is self.tail:
            tmp.next = insert_node
            self.tail = insert_node
        else:
            insert_node.next = tmp.next
            tmp.next = insert_node

        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        tmp = self.head
        if index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return
        for i in range(1, index):
            if tmp:
                tmp = tmp.next
            else:
                return
        if tmp.next:
            tmp.next = tmp.next.next


# ====================================================20201210
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(1000000)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.len = 0

    def _insertNode(self, pre_node, curr_node, i_node) -> None:
        """
        insert a node of val
        """
        # print('_insertNode', self.len)
        if not curr_node:  # delte node
            self.len -= 1
            pre_node.next = i_node
            i_node.pre = pre_node
        else:
            # print(pre_node.val, curr_node.val, i_node.val)
            self.len += 1
            pre_node.next, i_node.pre = i_node, pre_node
            i_node.next, curr_node.pre = curr_node, i_node

    def _getNode(self, index: int):
        """
        return the node.pre and node at the index
        """
        # print('_getNode', index, self.len)
        if index > self.len:  # when index == self.len, wil return last_node, self.tail
            return None, None
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        # print(node.val, node.next.val)
        return node, node.next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # print('get', index)
        if index >= self.len:
            return -1
        pre, curr = self._getNode(index)
        # self.printList()
        if curr:
            return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # print('addAtHead', val)
        self._insertNode(self.head, self.head.next, Node(val))
        # self.printList()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # print('addAtTail', val)
        self._insertNode(self.tail.pre, self.tail, Node(val))
        # self.printList()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # print('addAtIndex', index, val)
        # self.printList()
        if index > self.len:
            return -1
        pre_node, curr_node = self._getNode(index)
        if pre_node:
            self._insertNode(pre_node, curr_node, Node(val))

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # print('deleteAtIndex', index)
        # self.printList()
        if index >= self.len:
            return -1
        pre_node, curr_node = self._getNode(index)
        if curr_node:
            self._insertNode(pre_node, None, curr_node.next)

    # def printList(self):
        # node = self.head
        # lst = []
        # while node:
        #     lst.append(node.val)
        #     node = node.next
        # print(lst)

# ==========================================
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.pre = self.head
        self.len = 0

    def _insertNode(self, pre_node, curr_node, i_node) -> None:
        """
        insert a node of val
        """
        if not curr_node:  # delte node
            self.len -= 1
            pre_node.next = i_node
            i_node.pre = pre_node
        else:
            self.len += 1
            pre_node.next, i_node.pre = i_node, pre_node
            i_node.next, curr_node.pre = curr_node, i_node

    def _getNode(self, index: int):
        """
        return the node.pre and node at the index
        """
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node, node.next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.len:
            return -1
        pre, curr = self._getNode(index)
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._insertNode(self.head, self.head.next, Node(val))


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self._insertNode(self.tail.pre, self.tail, Node(val))


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len:
            return -1
        pre_node, curr_node = self._getNode(index)
        self._insertNode(pre_node, curr_node, Node(val))

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.len:
            return -1
        pre_node, curr_node = self._getNode(index)
        self._insertNode(pre_node, None, curr_node.next)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# def print_linkedList(ll):
    # print("==========")
    tmp = ll.head
    while tmp:
        # print(tmp.val)
        tmp = tmp.next
    # print("==========")

#Test 1
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
print_linkedList(linkedList)
# linkedList.addAtTail(3)
print_linkedList(linkedList)
# linkedList.addAtIndex(1, 2)
print_linkedList(linkedList)
print(linkedList.get(1))           
# linkedList.deleteAtIndex(1)
print(linkedList.get(1)) 

#Test 2
# ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
# [[],[1],[1,2],[1],[0],[2]]
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
print_linkedList(linkedList)
# linkedList.addAtIndex(1, 2)
print_linkedList(linkedList)
print(linkedList.get(1))
print(linkedList.get(0))
print(linkedList.get(2))
       

#Test 3
# ["MyLinkedList","get","addAtIndex","get","get","addAtIndex","get","get"]
# [[],[0],[1,2],[0],[1],[0,1],[0],[1]]
linkedList = MyLinkedList()
# print(linkedList.get(0))
linkedList.addAtIndex(1, 2)
# print_linkedList(linkedList)
# print(linkedList.get(0))
# print(linkedList.get(1))
linkedList.addAtIndex(0, 1)
# print_linkedList(linkedList)
# print(linkedList.get(0))
# print(linkedList.get(1))


["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]


Output
[null,null,null,null,3,null,0]
Expected
[null,null,null,null,2,null,3]


["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
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

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def print_linkedList(ll):
    print("==========")
    tmp = ll.head
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    print("==========")

#Test 1
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# print_linkedList(linkedList)
# linkedList.addAtTail(3)
# print_linkedList(linkedList)
# linkedList.addAtIndex(1, 2)
# print_linkedList(linkedList)
# print(linkedList.get(1))           
# linkedList.deleteAtIndex(1)
# print(linkedList.get(1)) 

#Test 2
# ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
# [[],[1],[1,2],[1],[0],[2]]
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# print_linkedList(linkedList)
# linkedList.addAtIndex(1, 2)
# print_linkedList(linkedList)
# print(linkedList.get(1))
# print(linkedList.get(0))
# print(linkedList.get(2))
       

#Test 3
# ["MyLinkedList","get","addAtIndex","get","get","addAtIndex","get","get"]
# [[],[0],[1,2],[0],[1],[0,1],[0],[1]]
linkedList = MyLinkedList()
print(linkedList.get(0))
linkedList.addAtIndex(1, 2)
print_linkedList(linkedList)
print(linkedList.get(0))
print(linkedList.get(1))
linkedList.addAtIndex(0, 1)
print_linkedList(linkedList)
print(linkedList.get(0))
print(linkedList.get(1))







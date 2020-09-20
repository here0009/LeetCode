"""
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);            // return true
circularDeque.insertLast(2);            // return true
circularDeque.insertFront(3);           // return true
circularDeque.insertFront(4);           // return false, the queue is full
circularDeque.getRear();            // return 2
circularDeque.isFull();             // return true
circularDeque.deleteLast();         // return true
circularDeque.insertFront(4);           // return true
circularDeque.getFront();           // return 4
 

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Deque library.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.length = 0
        self.head = None
        self.tail = None
        self.k = k
        # print(self.k)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length < self.k:
            node = Node(value)
            self.length += 1
            if self.length == 1:
                self.tail = node
            else:
                node.next, self.head.pre = self.head, node
            self.head = node
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length < self.k:
            node = Node(value)
            self.length += 1
            if self.length == 1:
                self.head = node
            else:
                node.pre, self.tail.next = self.tail, node
            self.tail = node
            return True
        return False
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.length > 0:
            self.tail = self.tail.pre
            self.length -= 1
            if self.length == 0:
                self.head = None
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.head.val
        return -1 

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.k
      

# https://leetcode.com/problems/design-circular-deque/discuss/476131/Two-python-implementations-based-on-list-and-doubly-linked-list.  
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
        self.capacity = k
        self.size = 0
        
        self.circular_deque = [ 0 ] * k
        
        self.rear = 0
        self.front = k-1
        
        
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.front ] = value
            self.front = (self.front-1)%self.capacity
            self.size += 1
        
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.rear ] = value
            self.rear = (self.rear+1)%self.capacity
            self.size += 1
        
            return True
        
        else:
            return False
        
        
        
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if self.size != 0:
            
            self.front = (self.front+1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if self.size != 0:
            
            self.rear = (self.rear-1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False        
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.front+1)%self.capacity ]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.rear-1)%self.capacity ]
        else:
            return -1
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
circularDeque = MyCircularDeque(3) # set the size to be 3
print(circularDeque.insertLast(1))            # return true
print(circularDeque.insertLast(2))            # return true
print(circularDeque.insertFront(3))           # return true
print(circularDeque.insertFront(4))           # return false, the queue is full
print(circularDeque.getRear())            # return 2
print(circularDeque.isFull())             # return true
print(circularDeque.deleteLast())         # return true
print(circularDeque.insertFront(4))           # return true
print(circularDeque.getFront())           # return 4


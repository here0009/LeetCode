"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.q.popleft()
                

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.q
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())
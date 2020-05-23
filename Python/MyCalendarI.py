"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
from bisect import bisect_left
from bisect import insort
class MyCalendar_1:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if not self.booked:
            self.booked.append((start,end))
            return True
        index = bisect_left(self.booked, (start,end))
        if index < len(self.booked):
            if self.booked[nxt][0] < end:
                return False 
        if index > 0:
            pre = index-1
            if self.booked[pre][1] > start:
                return False
        insort(self.booked, (start, end))
        # print(self.booked)
        return True

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node, root=None):
        if not self.root:
            self.root = node
            return True
        if not root:
            root = self.root
        if node.start >= root.end:
            if not root.right:
                root.right = node
                return True
            else:
                return self.insert(node, root.right)
        elif node.end <= root.start:
            if not root.left:
                root.left = node
                return True
            else:
                return self.insert(node, root.left)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.tree = Tree()

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        return self.tree.insert(node)


# Your MyCalendar object will be instantiated and called as such:
mc = MyCalendar();
# print(mc.book(10, 20))
# print(mc.book(15, 25))
# print(mc.book(20, 30))


print(mc.book(47,50))
print(mc.book(33,41))
print(mc.book(39,45))

# ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
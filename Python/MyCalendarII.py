"""
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
"""
Thoughts:
keep the record in the format start,end,flag. 
flag is True if there is an overlap in start, end region.
"""
from bisect import bisect_left
from bisect import insort
class MyCalendarTwo:
    """
    something was wrong, did not figure it out
    """      
    def __init__(self):
        self.calander = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        if not self.calander:
            self.calander.append((start,end))
            return True

        print('++++++++++')
        print(start, end)

        if self.overlap:
            o_index = bisect_left(self.overlap, (start,end))
            if o_index < len(self.overlap):
                 i_start,i_end = self.overlap[o_index]
                 if i_start < end:
                    return False
            if o_index > 0:
                i_start,i_end = self.overlap[o_index-1]
                if i_end > start:
                    return False

        index = bisect_left(self.calander, (start,end))

        if index < len(self.calander):
            i_start,i_end = self.calander[index]
            if i_start < end:
                #start < i_start, because it inserted before i_start
                insort(self.overlap, (i_start, min(end,i_end)))

        if index > 0:
            i_start,i_end = self.calander[index-1]
            if i_end > start:
                insort(self.overlap, (start, min(end,i_end)))

        insort(self.calander, (start, end))

        print(self.calander)
        print(self.overlap)
        return True
        
from bisect import bisect_left
from bisect import insort
class MyCalendarTwo:      
    def __init__(self):
        self.calander = []

    def book(self, start: int, end: int) -> bool:
        insort(self.calander, (start,1))
        insort(self.calander, (end,-1))
        counts = 0
        for i,v in self.calander:
            counts += v
            if counts == 3:
                self.calander.pop(bisect_left(self.calander,(start,1)))
                self.calander.pop(bisect_left(self.calander,(end,-1)))
                return False
        return True

class MyCalendarTwo:      
    def __init__(self):
        self.calander = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for i,j in self.overlap:
            if i < end and j > start:
                return False

        for i,j in self.calander:
            if i < end and j > start:
                self.overlap.append((max(start,i),min(end,j)))
        self.calander.append((start,end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

mc = MyCalendarTwo()
# print(mc.book(10, 20))
# print(mc.book(50, 60))
# print(mc.book(10, 40))
# print(mc.book(5, 15))
# print(mc.book(5, 10))
# print(mc.book(25, 55))

input_list = [[33,44],[85,95],[20,37],[91,100],[89,100],[77,87],[80,95],[42,61],[40,50],[85,99],[74,91],[70,82],[5,17],[77,89],[16,26],[21,31],[30,43],[96,100],[27,39],[44,55],[15,34],[85,99],[74,93],[84,94],[82,94],[46,65],[31,49],[58,73],[86,99],[73,84],[68,80],[5,18],[75,87],[88,100],[25,41],[66,79],[28,41],[60,70],[62,73],[16,33]]

for i,j in input_list:
    print(mc.book(i,j))

"""
Output:
[null,true,true,true,true,false,true,false,true,false,false,false,true,true,false,true,false,false,true,false,true,false,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,true,false,false]
Expected:
[null,true,true,true,true,false,true,false,true,false,false,false,true,true,false,true,false,false,true,false,true,false,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false]
"""
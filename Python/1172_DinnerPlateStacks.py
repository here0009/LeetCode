"""
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

# print(DinnerP)lates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) Pushes the given positive integer val into the leftmost stack with size less than capacity.
int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) Returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[None,None,None,None,None,None,2,None,None,20,21,5,4,3,1,-1]

Explanation: 
# print(DinnerP)lates D = DinnerPlates(2);  // Initialize with capacity = 2
# print(D.push()1);
# print(D.push()2);
# print(D.push()3);
# print(D.push()4);
# print(D.push()5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
# print(D.popAt)Stack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
# print(D.push()20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
# print(D.push()21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
# print(D.popAt)Stack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
# print(D.popAt)Stack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
# print(D.pop())            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
# print(D.pop())            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
# print(D.pop())            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
# print(D.pop())            // Returns 1.  There are no stacks.
# print(D.pop())            // Returns -1.  There are still no stacks.
 

Constraints:

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
At most 200000 calls will be made to push, pop, and popAtStack.
"""


import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.plates = []
        self.pq = []

    def push(self, val: int) -> None:
        # print('push', val)
        while self.pq and (self.pq[0] >= len(self.plates) or len(self.plates[self.pq[0]]) >= self.capacity):
            heapq.heappop(self.pq)
        if not self.pq:
            heapq.heappush(self.pq, len(self.plates))
            self.plates.append([])
        index = self.pq[0]
        self.plates[index].append(val)
        if len(self.plates[index]) == self.capacity:
            heapq.heappop(self.pq)
        # print(self.pq)
        # print(self.plates)

    def pop(self) -> int:
        # print('pop')
        while len(self.plates) > 0 and len(self.plates[-1]) == 0:  # pop the empty stack at the end of self.plates, reserve at least one stack
            self.plates.pop()
        # print(self.pq)
        # print(self.plates)
        res = self.plates[-1].pop() if len(self.plates) > 0 else -1
        print(res)
        return res 

    def popAtStack(self, index: int) -> int:
        # print('popAtStack', index)
        if len(self.plates) > index and len(self.plates[index]) > 0:
            heapq.heappush(self.pq, index)
            # print(self.pq)
            # print(self.plates)
            return self.plates[index].pop()
        # print(self.pq)
        # print(self.plates)
        return -1


import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.plates = []
        self.pq = []

    def push(self, val: int) -> None:
        while self.pq and (self.pq[0] >= len(self.plates) or len(self.plates[self.pq[0]]) >= self.capacity):  # the insertion place is not avaliable
            heapq.heappop(self.pq)
        if not self.pq:   # no insertion place, add a new plate
            heapq.heappush(self.pq, len(self.plates))
            self.plates.append([])
        index = self.pq[0]
        self.plates[index].append(val)
        if len(self.plates[index]) == self.capacity:
            heapq.heappop(self.pq)

    def pop(self) -> int:
        while len(self.plates) > 0 and len(self.plates[-1]) == 0:  # pop the empty plate at the end of self.plates
            self.plates.pop()
        return self.plates[-1].pop() if len(self.plates) > 0 else -1

    def popAtStack(self, index: int) -> int:
        if len(self.plates) > index and len(self.plates[index]) > 0:
            heapq.heappush(self.pq, index)
            return self.plates[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# D = DinnerPlates(2)  # Initialize with capacity = 2
print(D.push(1))
print(D.push(2))
print(D.push(3))
print(D.push(4))
print(D.push(5))         # The stacks are now:  2  4  1  3  5  ﹈ ﹈ ﹈
print(D.popAtStack(0))   # Returns 2.  The stacks are now:     4  1  3  5  ﹈ ﹈ ﹈
print(D.push(20))        # The stacks are now: 20  4  1  3  5  ﹈ ﹈ ﹈
print(D.push(21))        # The stacks are now: 20  4 21  1  3  5  ﹈ ﹈ ﹈
print(D.popAtStack(0))   # Returns 20.  The stacks are now:     4 21  1  3  5  ﹈ ﹈ ﹈
print(D.popAtStack(2))   # Returns 21.  The stacks are now:     4  1  3  5  ﹈ ﹈ ﹈ 
print(D.pop())            # Returns 5.  The stacks are now:      4  1  3   ﹈ ﹈  
print(D.pop())            # Returns 4.  The stacks are now:   1  3   ﹈ ﹈   
print(D.pop())            # Returns 3.  The stacks are now:   1   ﹈   
print(D.pop())            # Returns 1.  There are no stacks.
print(D.pop())            # Returns -1.  There are still no stacks.

# ["DinnerPlates","push","push","popAtStack","pop","push","push","pop","pop"]
# [[1],[1],[2],[1],[],[1],[2],[],[]]

# D = DinnerPlates(1)  # Initialize with capacity = 2
print(D.push(1))
print(D.push(2))
print(D.popAtStack(1))
print(D.pop())
print(D.push(1))
print(D.push(2))  
print(D.pop())
print(D.pop())


command = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop"]
parameter = [[2],[471],[177],[1],[29],[333],[154],[130],[333],[1],[0],[2],[0],[165],[383],[267],[367],[53],[373],[388],[249],[],[],[],[]]

output = [None,None,None,None,None,None,None,None,None,29,177,154,471,None,None,None,None,None,None,None,None,333,130,333,1]

expected = [None,None,None,None,None,None,None,None,None,29,177,154,471,None,None,None,None,None,None,None,None,249,388,373,53]

for c, p, o, e in zip(command, parameter, output, expected):
    print(c, p, o, e)
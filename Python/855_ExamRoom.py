"""
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""

from bisect import insort
class ExamRoom:

    def __init__(self, N: int):
        self.nums = []
        self.upper = N-1
        self.lower = 0

    def seat(self) -> int:
        if len(self.nums) == 0:
            self.nums.append(0)
            return 0
        gap, res = 0, 0
        if self.nums[0] != self.lower:
            gap = self.nums[0]
            res = self.lower
        if self.nums[-1] != self.upper and (self.upper - self.nums[-1]) > gap:
            gap = 0
            res = self.upper
        for i in range(1, len(self.nums)):
            tmp = (self.nums[i] - self.nums[i-1])//2
            if tmp > gap:
                gap = tmp
                res = self.nums[i-1] + gap
        insort(self.nums, res)
        return res

    def leave(self, p: int) -> None:
        self.nums.remove(p)


from bisect import insort
class ExamRoom:

    def __init__(self, N: int):
        self.nums = []
        self.upper = N-1


    def seat(self) -> int:
        if len(self.nums) == 0:
            res = 0
        else:
            gap, res = self.nums[0], 0
            for i in range(1, len(self.nums)):
                tmp = (self.nums[i] - self.nums[i-1])//2
                if tmp > gap:
                    gap = tmp
                    res = self.nums[i-1] + gap
            if self.upper - self.nums[-1] > gap:
                gap = self.upper - self.nums[-1]
                res = self.upper
        insort(self.nums, res)
        return res

    def leave(self, p: int) -> None:
        self.nums.remove(p)

# https://leetcode.com/problems/exam-room/discuss/185690/Python-heapq-clean-solution-with-explanation-seat-O(log-n)-leave-O(n)
import heapq
class ExamRoom:
    
    def dist(self, x, y):  # length of the interval (x, y)
        if x == -1:        # note here we negate the value to make it maxheap
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x-y)//2) 
        
    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap
        
    def seat(self):
        _, x, y = heapq.heappop(self.pq)  # current max interval 
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x+y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat
        
    def leave(self, p):
        head = tail = None
        for interval in self.pq:  # interval is in the form of (d, x, y)
            if interval[1] == p:  
                tail = interval
            if interval[2] == p:  
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)  # important! re-heapify after deletion
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(N)
param_1 = obj.seat()
obj.leave(p)
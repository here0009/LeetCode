"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collectiions import Counter
import heapq
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.pq = []
        self.counts = Counter()
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.pq, -x)

    def pop(self) -> int:
        if self.stack:
            num = self.stack.pop()
            if self.counts[num] > 0:  #already poped by popMax
                self.counts[num] -= 1
            elif self.counts[num] == 0:
                return num
        return None

    def top(self) -> int:
        if self.stack:
            num = self.stack[-1]
            if self.counts[num] > 0:  #already poped by popMax
                self.counts[num] -= 1
                self.stack.pop()
            elif self.counts[num] == 0:
                return num
        return None

    def peekMax(self) -> int:
        if self.pq:
            v = heapq.heappop(pq)
            heappop.heappush(v)
            return -v
        return None

    def popMax(self) -> int:
        if self.pq:
            v = heapq.heappop(pq)
            self.counts[-v] += 1
            return -v
        return None



import heapq
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def peekMax(self) -> int:
        if self.stack:
            return max(self.stack)
        return None

    def popMax(self) -> int:
        max_v = self.peekMax()
        if max_v is not None:
            index = len(self.stack) -1
            while index > 0 and self.stack[index] != max_v:
                index -= 1
            self.stack = self.stack[:index] + self.stack[index+1:]
            return max_v
        return None


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
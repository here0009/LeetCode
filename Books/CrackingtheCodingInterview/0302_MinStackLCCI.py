"""
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。


示例：

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq
from collections import Counter
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.pq = []
        self.counts = Counter()


    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.pq, x)
        self.counts[x] += 1

    def pop(self) -> None:
        if self.stack:
            self.counts[self.stack.pop()] -= 1
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        while self.pq and self.counts[self.pq[0]] == 0:
            heapq.heappop(self.pq)
        if self.pq:
            return self.pq[0]
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
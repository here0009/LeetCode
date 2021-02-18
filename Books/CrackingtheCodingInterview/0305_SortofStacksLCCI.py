"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:

 输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 输出：
[null,null,null,1,null,2]
示例2:

 输入： 
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 输出：
[null,null,null,null,null,true]
说明:

栈中的元素数目在[0, 5000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-of-stacks-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import heapq
class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        heapq.heappush(self.stack, val)

    def pop(self) -> None:
        if not self.isEmpty():
            heapq.heappop(self.stack)

    def peek(self) -> int:
        if not self.isEmpty():
            return self.stack[0]
        return -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0



# Your SortedStack object will be instantiated and called as such:
obj = SortedStack()
obj.push(val)
obj.pop()
param_3 = obj.peek()
param_4 = obj.isEmpty()
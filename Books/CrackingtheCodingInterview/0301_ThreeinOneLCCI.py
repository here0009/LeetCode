"""
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:

 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:

 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-in-one-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TripleInOne:

    def __init__(self, stackSize: int):
        self.stacks = [[] for _ in range(3)]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stacks[stackNum]) < self.stackSize:
            self.stacks[stackNum].append(value)
        print(self.stacks)


    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.stacks[stackNum].pop()
        return -1


    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.stacks[stackNum][-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stacks[stackNum]) > 0



# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
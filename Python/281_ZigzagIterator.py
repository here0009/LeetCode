"""
Given two 1d vectors, implement an iterator to return their elements alternately.

 

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
 

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.index = 0
        matrix = [v1, v2]
        len_row = [len(v) for v in matrix]
        max_row = len(matrix)
        self.total, max_col = sum(len_row), max(len_row)
        self.lst = []
        for j in range(max_col):
            for i in range(max_row):
                if j < len_row[i]:
                    self.lst.append(matrix[i][j])
        # print(self.lst)

    def next(self) -> int:
        if self.hasNext():
            v = self.lst[self.index]
            self.index += 1
            return v

    def hasNext(self) -> bool:
        return self.index < self.total


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.i = 0
        self.j = 0
        self.matrix = [v1, v2]
        self.len_row = [len(v) for v in self.matrix]
        self.row = len(self.matrix)
        self.col = max(self.len_row)

    def next(self) -> int:
        if self.hasNext():
            v = self.matrix[self.i][self.j]
            self.i += 1
            return v

    def hasNext(self) -> bool:
        while self.j < self.col:
            if self.i == self.row:
                self.i = 0
                self.j += 1
            if self.j >= self.col or self.j < self.len_row[self.i]:
                break
            else:
                self.i += 1
        return self.j < self.col


# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2]
v2 = [3,4,5,6] 

v1 = [1,2]
v2 = []
i, v = ZigzagIterator(v1, v2), []
# print(i.matrix)
while i.hasNext(): 
    v.append(i.next())
print(v)

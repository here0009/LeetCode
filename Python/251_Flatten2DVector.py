"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-2d-vector
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Vector2D:
    def __init__(self, v):
        self.lst = v
        self.i = 0
        self.length = len(self.lst)
        self.j = 0
        print(self.lst)

    def next(self) -> int:
        if self.hasNext():
            v = self.lst[self.i][self.j]
            self.j += 1
            if self.j >= len(self.lst[self.i]):
                self.i += 1
                self.j = 0
            return v

    def hasNext(self) -> bool:
        while self.i < self.length:
            if self.j >= len(self.lst[self.i]):
                self.i += 1
                self.j = 0
            else:
                break
        if (self.i >= self.length) or \
            (self.i == self.length-1 and self.j >= len(self.lst[self.i])):
            return False
        return True


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.inner = 0
        self.outer = 0
    

    def advance_to_next(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0
        
    def next(self) -> int:
        self.advance_to_next()
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result
        

    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.outer < len(self.vector)


class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i, self.j = 0, 0

    def next(self) -> int:
        if self.hasNext():
            val = self.v[self.i][self.j]
            self.j += 1
            return val

    def hasNext(self) -> bool:
        while self.i < len(self.v) and self.j >= len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.v) and self.j < len(self.v[self.i])




# Your Vector2D object will be instantiated and called as such:
# iterator = Vector2D([[1,2],[3],[4]])
# print(iterator.next())
# print(iterator.next())
# print(iterator.next())
# print(iterator.hasNext())
# print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())


iterator = Vector2D([[],[3]])
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
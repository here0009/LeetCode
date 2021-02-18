"""
动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。

enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。

dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。

示例1:

 输入：
["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [], [], []]
 输出：
[None,None,None,[0,0],[-1,-1],[1,0]]
示例2:

 输入：
["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
 输出：
[None,None,None,None,[2,1],[0,0],[1,0]]
说明:

收纳所的最大容量为20000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/animal-shelter-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
# import random
from collections import deque
class AnimalShelf:
    """
    wrong answer, if dequeueAny, we should deque the oldest animal
    """
    def __init__(self):
        self.cats = deque([])
        self.dogs = deque([])
        self.max_limit = 20000
        self.animals = [self.cats, self.dogs]

    def enqueue(self, animal: List[int]) -> None:
        idx, kind = animal
        if len(self.animals[kind]) < self.max_limit:
            self.animals[kind].append(idx)

    def dequeueAny(self) -> List[int]:
        length = list(map(len, self.animals))
        max_len = max(length)
        if max_len == 0:
            return [-1, -1]
        kind = length.index(max_len)
        return [self.animals[kind].popleft(), kind]

    def dequeueDog(self) -> List[int]:
        if len(self.dogs) > 0:
            return [self.dogs.popleft(), 1]
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        if len(self.cats) > 0:
            return [self.cats.popleft(), 0]
        return [-1, -1]

from typing import List
# import random
from collections import deque
class AnimalShelf:

    def __init__(self):
        self.cats = deque([])
        self.dogs = deque([])
        self.max_limit = 20000
        self.animals = deque([])

    def enqueue(self, animal: List[int]) -> None:
        if len(self.cats) + len(self.dogs) < self.max_limit:
            idx, kind = animal
            self.animals.append(animal)
            if kind == 0:
                self.cats.append(idx)
            elif kind == 1:
                self.dogs.append(idx)

    def dequeueAny(self) -> List[int]:
        while self.animals:
            idx, kind = self.animals.popleft()
            if kind == 0 and self.cats and idx == self.cats[0]:
                self.cats.popleft()
                return [idx, kind]
            elif kind == 1 and self.dogs and idx == self.dogs[0]:
                self.dogs.popleft()
                return [idx, kind]
        return [-1,-1]

    def dequeueDog(self) -> List[int]:
        if len(self.dogs) > 0:
            return [self.dogs.popleft(), 1]
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        if len(self.cats) > 0:
            return [self.cats.popleft(), 0]
        return [-1, -1]



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()

command = ["AnimalShelf", "dequeueCat", "dequeueCat", "dequeueAny", "dequeueDog", "dequeueCat", "enqueue", "dequeueAny", "enqueue", "dequeueCat", "enqueue", "dequeueCat", "dequeueAny", "dequeueAny", "enqueue", "dequeueDog", "enqueue", "dequeueCat", "dequeueDog", "enqueue", "dequeueCat", "dequeueCat", "dequeueDog", "enqueue", "dequeueDog", "dequeueCat", "dequeueDog", "dequeueAny", "dequeueCat", "dequeueAny", "enqueue", "enqueue", "dequeueDog", "dequeueAny", "dequeueDog", "dequeueCat", "enqueue", "dequeueAny", "enqueue", "enqueue", "dequeueDog", "dequeueAny", "dequeueAny", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny", "dequeueCat", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueDog", "dequeueDog", "dequeueDog", "dequeueDog", "enqueue", "enqueue", "enqueue", "enqueue", "enqueue", "dequeueCat", "dequeueCat", "dequeueDog", "enqueue"]
para = [[], [], [], [], [], [], [[0, 1]], [], [[1, 0]], [], [[2, 1]], [], [], [], [[3, 1]], [], [[4, 0]], [], [], [[5, 0]], [], [], [], [[6, 0]], [], [], [], [], [], [], [[7, 1]], [[8, 1]], [], [], [], [], [[9, 1]], [], [[10, 1]], [[11, 1]], [], [], [], [[12, 0]], [], [], [], [], [[13, 0]], [[14, 0]], [], [], [], [], [], [], [[15, 1]], [[16, 1]], [[17, 0]], [[18, 1]], [[19, 1]], [], [], [], [[20, 1]]]

output = [None,[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,[0,1],None,[1,0],None,[-1,-1],[-1,-1],[-1,-1],None,[0,1],None,[4,0],[2,1],None,[5,0],[-1,-1],[3,1],None,[-1,-1],[6,0],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,None,[7,1],[8,1],[8,1],[-1,-1],None,[9,1],None,None,[9,1],[10,1],[-1,-1],None,[12,0],[10,1],[-1,-1],[-1,-1],None,None,[13,0],[11,1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,None,None,None,None,[14,0],[17,0],[15,1],None]

expected = [None,[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,[0,1],None,[1,0],None,[-1,-1],[2,1],[-1,-1],None,[3,1],None,[4,0],[-1,-1],None,[5,0],[-1,-1],[-1,-1],None,[-1,-1],[6,0],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,None,[7,1],[8,1],[-1,-1],[-1,-1],None,[9,1],None,None,[10,1],[11,1],[-1,-1],None,[12,0],[-1,-1],[-1,-1],[-1,-1],None,None,[13,0],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],None,None,None,None,None,[14,0],[17,0],[15,1],None]

for c, p, o, e in zip(command, para, output, expected):
    print(c, p, o, e)
    if o != e:
        print('!!!!!!!!')
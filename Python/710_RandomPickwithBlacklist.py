"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


from typing import List
from random import choice
class Solution:
    """
    TLE
    """
    def __init__(self, N: int, blacklist: List[int]):
        self.nums = list(set(range(N)) - set(blacklist))
        print(self.nums)

    def pick(self) -> int:
        return choice(self.nums)
        

from random import choice, shuffle
class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.nums = list(set(range(N)) - set(blacklist))
        shuffle(self.nums)
        self.index = 0

    def pick(self) -> int:
        res = self.nums[self.index]
        self.index += 1
        if self.index == len(self.nums):
            shuffle(self.nums)
            self.index = 0
        return res



from random import randrange
from random import choice
class Solution:
    """
    Thoughts: map keys in black list to [self.length, N)]
    """
    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.length = N - len(blacklist)
        self.blacklist = set(blacklist)
        self.dict = dict()
        # print(self.N, self.length, self.blacklist)

    def pick(self) -> int:
        rand_num = randrange(0, self.length)
        # print(rand_num)
        if rand_num in self.blacklist:
            if rand_num not in self.dict:
                tmp = randrange(self.length, self.N)
                while tmp in self.blacklist:
                    tmp = randrange(self.length, self.N)
                self.dict[rand_num] = tmp  # some num in blacklist probably lies in self.legth ~ self.N
            return self.dict[rand_num]
        return rand_num


from random import randrange
from random import choice
class Solution:
    """
    Thoughts: map keys in black list to [self.length, N)]
    """
    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.length = N - len(blacklist)
        self.blacklist = set(blacklist)
        self.extra = list(set(range(self.length, N)) - self.blacklist)
        self.dict = dict()
        # print(self.N, self.length, self.blacklist)

    def pick(self) -> int:
        rand_num = randrange(0, self.length)
        # print(rand_num)
        if rand_num in self.blacklist:
            self.dict[rand_num] = choice(self.extra)  # some num in blacklist probably lies in self.legth ~ self.N
            return self.dict[rand_num]
        return rand_num

# Your Solution object will be instantiated and called as such:
obj = Solution(4, [1])
for i in range(10):
    print(obj.pick())
# param_1 = obj.pick()
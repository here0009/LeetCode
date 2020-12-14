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

# Your Solution object will be instantiated and called as such:
obj = Solution(4, [2])
for i in range(3):
    print(obj.pick())
# param_1 = obj.pick()
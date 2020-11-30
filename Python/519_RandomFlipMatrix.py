"""
You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any
"""

from random import sample
from typing import List
class Solution:
    """
    TLE
    """
    def __init__(self, n_rows: int, n_cols: int):
        self.R = n_rows
        self.C = n_cols
        self.index = set(list(range(n_rows*n_cols)))

    def flip(self) -> List[int]:
        if not self.index:
            return None
        index = sample(self.index, 1)[0]
        self.index.remove(index)
        i, j = divmod(index, self.C)
        return [i,j]

    def reset(self) -> None:
        self.index = set(list(range(self.R*self.C)))


from random import shuffle
from typing import List
class Solution:
    """
    wrong answer, probably not random enough
    """
    def __init__(self, n_rows: int, n_cols: int):
        self.R = n_rows
        self.C = n_cols
        self.randindex = list(range(self.R*self.C))
        shuffle(self.randindex)
        self.index = 0

    def flip(self) -> List[int]:
        i, j = divmod(self.randindex[self.index], self.C)
        self.index += 1
        return [i,j]

    def reset(self) -> None:
        self.index = 0


from random import shuffle
from typing import List
class Solution:
    """
    generate a random sequence at the beginning
    """
    def __init__(self, n_rows: int, n_cols: int):
        self.R = n_rows
        self.C = n_cols
        self.lst = list(range(self.R*self.C))
        shuffle(self.lst)
        self.index = 0

    def flip(self) -> List[int]:
        i, j = divmod(self.lst[self.index], self.C)
        self.index += 1
        return [i,j]

    def reset(self) -> None:
        shuffle(self.lst)
        self.index = 0

# Your Solution object will be instantiated and called as such:
# https://leetcode.com/problems/random-flip-matrix/discuss/154429/Python-solution-based-on-random-shuffle-with-explanation
from random import randrange, randint
class Solution:
    """
    generate a random sequence at the beginning
    """
    def __init__(self, n_rows: int, n_cols: int):
        self.R = n_rows
        self.C = n_cols
        self.end = n_rows*n_cols-1
        self.start = 0
        self.dict = dict()

    def flip(self) -> List[int]:
        rand = randint(self.start, self.end)
        res = self.dict.get(rand, rand)
        self.dict[rand] = self.dict.get(self.start, self.start)
        self.start += 1
        return list(divmod(res, self.C))


    def reset(self) -> None:
        self.dict = dict()
        self.start = 0


import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows= n_rows
        self.n_cols = n_cols
        self.start = 0
        self.end = self.n_rows * self.n_cols
        self.pos_dict = collections.defaultdict()

    def flip(self) -> List[int]:
        # generate index
        rand_idx = random.randrange(self.start, self.end)
        res = self.pos_dict.get(rand_idx, rand_idx)
        # swap - put total at index that we generated
        self.pos_dict[rand_idx] = self.pos_dict.get(self.end-1, self.end-1)
        # decrease total number of values
        self.end -= 1
        return [res // self.n_cols, res % self.n_cols]


    def reset(self) -> None:
        self.pos_dict = collections.defaultdict()
        self.end = self.n_rows * self.n_cols


class Solution:
    def __init__(self, n_rows, n_cols):
        self.rows, self.cols, self.used = n_rows, n_cols, set()
        
    def flip(self):
        while True:
            r, c = random.randint(1, self.rows), random.randint(1, self.cols)
            if (r, c) not in self.used:
                self.used.add((r, c))
                return [r - 1, c - 1]
            
    def reset(self):
        self.used = set()

        
obj = Solution(2,2)
for i in range(4):
    print(obj.flip())
# print(obj.flip())
obj.reset()

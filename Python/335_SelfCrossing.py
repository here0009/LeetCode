"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

 

Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false 
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true 
"""


from typing import List
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        wrong answer
        """
        i, j = 0, 0
        dir4 = [(0,1), (-1,0), (0,-1), (1,0)]
        for k in range(len(x)):
            i += x[k]*dir4[k%4][0]
            j += x[k]*dir4[k%4][1]
            if k >= 3 and j >= 0 and i >= 0:
                return True
        return False


# https://leetcode.com/problems/self-crossing/discuss/79141/Another-python...
from typing import List
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        a, b, c, d, e, f = [0]*6
        for num in x:

            a, b, c, d, e, f = num, a, b, c, d, e
            # print(a, b, c, d, e, f)
            if d >= b > 0 and (c <= a or (a >= c-e >= 0 and f+b >= d)):
                return True
        return False
# from typing import List
# class Solution:
#     def isSelfCrossing(self, x: List[int]) -> bool:
#         a, b, c, d, e, f = [-1]*6
#         for num in x:
#             # f, e, d, c, b, a = e, d, c, b, a, z
#             a, b, c, d, e, f = num, a, b, c, d, e
#             if d >= 0 and (c <= a) and (d >= b):
#                 return True
#             if e >= 0 and (c > a) and (d == b) and (e >= c - a):
#                 return True
#             if f >= 0 and (c > a) and (d > b) and (e >= c - a and e <= c) and (f >= d - b):
#                 return True
#         return False

from typing import List
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        x = x + [0]*6
        for i in range(len(x)-6+1):
            a, b, c, d, e, f = x[i:i+6]
            if d >= b > 0 and (c <= a or (a >= c-e >= 0 and f+b >=d)):
                return True
        return False

S = Solution()
x = [2,1,1,2]
print(S.isSelfCrossing(x))
x = [1,2,3,4]
print(S.isSelfCrossing(x))
x = [1,1,1,1]
print(S.isSelfCrossing(x))
x = [1,1,2,1,1]
print(S.isSelfCrossing(x))
x = [1,2,2,3,4]
print(S.isSelfCrossing(x))
# Output
# true
# Expected
# false
x = [3,3,3,2,1,1]
# Output
# true
# Expected
# false
x = [1,1,2,1,1]
# Output
# false
# Expected
# true
print(S.isSelfCrossing(x))
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
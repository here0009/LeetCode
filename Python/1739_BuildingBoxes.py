"""
You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

You can place the boxes anywhere on the floor.
If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the floor.

 

Example 1:



Input: n = 3
Output: 3
Explanation: The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
Example 2:



Input: n = 4
Output: 3
Explanation: The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
Example 3:



Input: n = 10
Output: 6
Explanation: The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on the back side.
 

Constraints:

1 <= n <= 109
"""

# https://leetcode.com/problems/building-boxes/discuss/1032016/C%2B%2B-Python-3-variables-solution-with-drawing-explanation
class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        row base boxes
        1    1   1
        2    3   4
        3    6   10
        ...
        1. find the base that base(i - 1) < n < base(i)
        2. add box one by one, if we add one base, we can add j + 1 boxes
        """
        row, base, boxes = 0, 0, 0
        while boxes < n:
            row += 1
            base += row
            boxes += base
            # print(row, base, boxes)
        if boxes == n:
            return base
        boxes -= base
        base -= row
        row = 0
        while boxes < n:
            row += 1
            boxes += row
            base += 1
        return base

S = Solution()
print(S.minimumBoxes(3))
print(S.minimumBoxes(4))
print(S.minimumBoxes(10))
print(S.minimumBoxes(15))
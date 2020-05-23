"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinetely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
"""
class Solution_1:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0,0]
        directions = [(0,1),(1,0),(0,-1),(-1,0)] #up,right,down,left
        d_index = 0
        d = directions[d_index] #up
        for i in range(4):
            for s in instructions:
                # print(start)
                # if s == 'G':
                #     d_index = d_index
                if s == 'R':
                    d_index = (d_index + 1) % 4
                    d = directions[d_index]
                elif s == 'L':
                    d_index = (d_index - 1) % 4
                    d = directions[d_index]
                start[0] += d[0]
                start[1] += d[1]
                if start[0] == 0 and start[1] == 0: #this is wrong, for the requirements is never leave the circle, but not return to the start point
                    return True

        return False


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0,0]
        directions = [(0,1),(1,0),(0,-1),(-1,0)] #up,right,down,left
        d_index = 0
        d = directions[d_index] #up
        for i in range(4):
            for s in instructions:
                if s == 'G':
                    start[0] += d[0]
                    start[1] += d[1]
                elif s == 'R':
                    d_index = (d_index + 1) % 4
                    d = directions[d_index]
                elif s == 'L':
                    d_index = (d_index - 1) % 4
                    d = directions[d_index]
        return start[0] == 0 and start[1] == 0

s = Solution()
print(s.isRobotBounded("GGLLGG"))
print(s.isRobotBounded("GG"))
print(s.isRobotBounded("GL"))
print(s.isRobotBounded("LLGRL"))
print(s.isRobotBounded("LRRRRLLLRL"))
print(s.isRobotBounded("RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"))



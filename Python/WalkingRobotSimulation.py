"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""
from collections import defaultdict
from bisect import bisect_left
class Solution:
    def robotSim(self, commands, obstacles):
        """
        change obstacles to dict, use bisect to find it, if if was found on the path, stop at the coord of obstacles, too complicated
        """
        obs_set = set(map(tuple, obstacles))
        # print(obs_set)

        directions = [(0,1),(1,0),(0,-1),(-1,0)] #NESW
        d_index = 0
        pos_x, pos_y = 0, 0
        res = 0
        for c in commands:
            if c == -1:
                d_index = (d_index+1)%4
            elif c == -2:
                d_index = (d_index-1+4)%4
            else:
                dx, dy = directions[d_index]
                while c > 0 and (pos_x+dx, pos_y+dy) not in obs_set:
                    # print(pos_x,pos_y)
                    pos_x += dx
                    pos_y += dy
                    c -= 1
                    res = max(res,pos_x**2 + pos_y**2 )
        # print(pos_x,pos_y)
        return res

s = Solution()
commands = [4,-1,3]
obstacles = []
print(s.robotSim(commands, obstacles))


commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
print(s.robotSim(commands, obstacles))

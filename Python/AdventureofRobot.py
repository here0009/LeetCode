"""
力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

示例 1：

输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
示例 2：

输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。
示例 3：

输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 

限制：

2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点
"""
class Solution:
    def robot(self, command: str, obstacles, x: int, y: int):
        ob_set = set(tuple(i) for i in obstacles)
        # print(ob_set)
        def check(ix,iy):
            if ix == x and iy == y:
                return 1
            if ix > x or iy > y:
                return -1
            if (ix,iy) in ob_set:
                return -1
            else:
                return 0
        dx,dy = 0,0
        while True:
            for c in command:
                if c == 'U':
                    dy += 1
                elif c == 'R':
                    dx += 1
                k = check(dx,dy)
                if k == 1:
                    return True
                elif k == -1:
                    return False

from collections import Counter
class Solution:
    def robot(self, command: str, obstacles, x: int, y: int):

        c_counter = Counter(command)
        rights = c_counter['R']
        ups = c_counter['U']
        
        def hit(dest_x,dest_y):
            circle = min(dest_x//rights, dest_y//ups)
            ix = circle*rights
            iy = circle*ups
            if ix == dest_x and iy == dest_y:
                return True
            for c in command:
                if c == 'U':
                    iy += 1
                elif c == 'R':
                    ix += 1
                if ix == dest_x and iy == dest_y:
                    return True
                elif ix > dest_x or iy > dest_y:
                    return False
            return False

        if not hit(x,y):
            return False

        for ox,oy in obstacles:
            if ox > x or oy > y:
                pass
            else:
                if hit(ox,oy):
                    return False
        return True




s = Solution()
command = "URR"
obstacles = []
x = 3
y = 2
print(s.robot(command, obstacles, x, y))

command = "URR"
obstacles = [[2, 2]]
x = 3
y = 2
print(s.robot(command, obstacles, x, y))

command = "URR"
obstacles = [[4, 2]]
x = 3
y = 2
print(s.robot(command, obstacles, x, y))

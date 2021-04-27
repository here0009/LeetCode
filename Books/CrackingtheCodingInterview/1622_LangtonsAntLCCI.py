"""
一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。

(1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
(2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。

编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。

网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R', 'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。

示例 1:

输入: 0
输出: ["R"]
示例 2:

输入: 2
输出:
[
  "_X",
  "LX"
]
示例 3:

输入: 5
输出:
[
  "_U",
  "X_",
  "XX"
]
说明：

K <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/langtons-ant-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List

class Solution:
    def __init__(self):
        self.cur = (0, 0) # 现在位置
        self.orientation = 'R' # 现在朝向
        self.moved = {(0, 0):'_'}  # 已走过位置，及其颜色

    def printKMoves(self, K):
        # 右转变换矩阵
        r_dir = {'L':[(0, 1), 'U'], 'U':[(1, 0), 'R'], 'R':[(0, -1), 'D'], 'D':[(-1, 0), 'L']}
        # 左转变换矩阵
        l_dir = {'L':[(0, -1), 'D'], 'U':[(-1, 0), 'L'], 'R':[(0, 1), 'U'], 'D':[(1, 0), 'R']}
        for _ in range(K):
            color = self.moved[self.cur] # 当前方块颜色
            if color == '_':
                self.moved[self.cur] = 'X' # 变换方块颜色
                self.cur = (self.cur[0]+r_dir[self.orientation][0][0], self.cur[1]+r_dir[self.orientation][0][1]) # 移动到的位置
                self.orientation = r_dir[self.orientation][1] # 当前朝向
                if self.cur not in self.moved:
                    self.moved[self.cur] = '_' # 添加当前位置到已走位置
                
            else:
                # 同上
                self.moved[self.cur] = '_'
                self.cur = (self.cur[0]+l_dir[self.orientation][0][0], self.cur[1]+l_dir[self.orientation][0][1])
                self.orientation = l_dir[self.orientation][1]
                if self.cur not in self.moved:
                    self.moved[self.cur] = '_'
        self.moved[self.cur] = self.orientation # 将终点位置改为朝向
        return self.draw()      
    
    def draw(self):
        # 根据走过位置及其方块绘制答案图
        l, r, u, d = float('inf'), float('-inf'), float('-inf'), float('inf')
        # 寻找左右上下边界
        for i, j in self.moved.keys():
            l = min(i, l)
            r = max(i, r)
            u = max(j, u)
            d = min(j, d)
        ans = []
        print(l,r,u,d)
        for y in range(u, d-1, -1):
            row = ''
            for x in range(l, r+1):
                if (x, y) in self.moved:
                    row += self.moved[(x, y)]
                else:
                    row += '_'
            ans.append(row)
        return ans

# 作者：ttresaui
# 链接：https://leetcode-cn.com/problems/langtons-ant-lcci/solution/pythonban-ben-by-ttresaui/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:

    def __init__(self):
        self.West = 0
        self.East = 0
        self.North = 0
        self.South = 0

    def printKMoves(self, K: int) -> List[str]:
        coorRec = {}
        # 方向表示如下:
        # L:0  U:1  R:2  D:3
        point = [(0, 0), 2]
        for step in range(K):
            # 改变蚂蚁原地点的颜色以及爬行方向
            if coorRec.get(point[0], "_") == "_":
                coorRec[point[0]] = "X"
                point[1] = (point[1] + 1) % 4
            else:
                coorRec[point[0]] = "_"
                point[1] = (point[1] + 3) % 4
            self.move(point)
        coorRec[point[0]] = ["L", "U", "R", "D"][point[1]]
        return ["".join([coorRec.get((x, y), "_")\
               for x in range(self.West, self.East + 1)])\
               for y in range(self.North, self.South - 1, -1)]

    def move(self, point):
        # 蚂蚁按照方向移动一步
        x, y = point[0]
        if point[1] == 0: point[0] = (x - 1, y)  # 方向向左
        elif point[1] == 1: point[0] = (x, y + 1)  # 方向向上
        elif point[1] == 2: point[0] = (x + 1, y)  # 方向向右
        else: point[0] = (x, y - 1)  # 方向向下
        # 修改东西南北边界
        x, y = point[0]
        self.East = max(self.East, x)
        self.West = min(self.West, x)
        self.South = min(self.South, y)
        self.North = max(self.North, y)


# 作者：NPEKUU1139
# 链接：https://leetcode-cn.com/problems/langtons-ant-lcci/solution/ji-lu-shang-xia-zuo-you-bian-jie-ji-ke-by-npekuu11/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
1. 使用curr记录蚂蚁当前位置及方向
2. 使用pos记录蚂蚁走过的位置及颜色
3. 使用limits记录蚂蚁走过的极限坐标
4. 对于每一步， 先更新蚂蚁当前位置的颜色和方向，再根据方向将蚂蚁移动到下一个位置。最后更新位置，进入下一步。
"""

class Solution:
    def printKMoves(self, K: int) -> List[str]:

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW
        curr = [(0, 0), 1]  # {index and orientation} of the ant
        pos = {(0, 0): '_'}  # recorded positions
        limits = [0] * 4  # limit for NESW
        for i in range(K):
            idx, ori = curr
            if pos.get(idx, '_') == '_':  # change the color and turn right
                pos[idx] = 'X'
                ori = (ori + 1) % 4
            else:  # change the color and turn left
                pos[idx] = '_'
                ori = (ori - 1) % 4
            dx, dy = dirs[ori]  # the movement direction
            x, y = dx + idx[0], dy + idx[1]
            # update the limits of 4 directions
            limits[0] = min(limits[0], x)
            limits[1] = max(limits[1], y)
            limits[2] = max(limits[2], x)
            limits[3] = min(limits[3], y)
            curr = [(x, y), ori]
        pos[curr[0]] = 'URDL'[curr[1]]
        res = []
        for i in range(limits[0], limits[2] + 1):
            res.append(''.join([pos.get((i, j), '_') for j in range(limits[3], limits[1] + 1)]))
        return res


S = Solution()
for i in range(10):
    print(i)
    print(S.printKMoves(i))

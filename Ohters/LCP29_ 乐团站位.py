"""
某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。

为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。例如当 num = 5 时，站位如图所示

image.png

请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。

示例 1：

输入：num = 3, Xpos = 0, Ypos = 2

输出：3

解释：
image.png

示例 2：

输入：num = 4, Xpos = 1, Ypos = 2

输出：5

解释：
image.png

提示：

1 <= num <= 10^9
0 <= Xpos, Ypos < num
"""


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        layer = min(xPos, yPos, num - 1 - xPos, num - 1 - yPos)
        if xPos == layer:
            col = yPos - layer
        elif yPos == num - 1 - layer:
            col = num - 2 * layer - 1 + xPos - layer
        elif xPos == num - 1 - layer:
            col = 2 * (num - 2 * layer - 1) + num - 1 - layer - yPos
        elif yPos == layer:
            col = 3 * (num - 2 * layer - 1) + num - 1 - layer - xPos
        idx = col + ((num - 1) * 4 + (num + 1 - 2 * layer) * 4) // 2 * layer
        # print(xPos, yPos,layer, col, idx)
        return idx % 9 + 1


S = Solution()
# num = 3
# xpos = 0
# ypos = 2
# print(S.orchestraLayout(num, xpos, ypos))
# num = 4
# xpos = 1
# ypos = 2
# print(S.orchestraLayout(num, xpos, ypos))
# num = 5
# xpos = 2
# ypos = 2
# res = [[0]*num for _ in range(num)]
# for xpos in range(0, num):
#     for ypos in range(0, num):
#         res[xpos][ypos] = S.orchestraLayout(num, xpos, ypos)
for num in range(10):
    res = [[0]*num for _ in range(num)]
    for xpos in range(0, num):
        for ypos in range(0, num):
            res[xpos][ypos] = S.orchestraLayout(num, xpos, ypos)
    for row in res:
        print(row)
    print('++++++++++++++++')
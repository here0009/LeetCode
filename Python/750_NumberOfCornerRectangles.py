"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

 

Example 1:

Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:

Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:

Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-corner-rectangles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        TLE
        """
        R, C = len(grid), len(grid[0])
        res = 0
        # for row in grid:
        #     print(row)
        for rd in range(1, R):
            for cd in range(1, C):
                # print(rd, cd)
                for i in range(R-rd):
                    for j in range(C-cd):
                        if grid[i][j] == grid[i+rd][j] == grid[i+rd][j+cd] == grid[i][j+cd] == 1:
                            res += 1
            # print('res', res)
        return res

class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        still TLE
        """
        R, C = len(grid), len(grid[0])
        res = 0
        # for row in grid:
        #     print(row)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    continue
                for rd in range(1, R):
                    if i+rd >= R:
                        break
                    if grid[i+rd][j] == 0:
                        continue
                    for cd in range(1, C):
                        if j+cd >= C:
                            break
                        if grid[i][j] == grid[i+rd][j] == grid[i+rd][j+cd] == grid[i][j+cd] == 1:
                            res += 1
        return res


from collections import Counter
class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        res = 0
        counts = Counter()
        for row in grid:
            for i in range(C-1):
                if row[i] == 1:
                    for j in range(i+1, C):
                        if row[j] == 1:
                            counts[(i,j)] += 1
        for v in counts.values():
            res += v*(v-1)//2
        return res



S = Solution()
grid = [[1, 0, 0, 1, 0],[0, 0, 1, 0, 1],[0, 0, 0, 1, 0],[1, 0, 1, 0, 1]]
print(S.countCornerRectangles(grid))
grid = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
print(S.countCornerRectangles(grid))
grid = [[1, 1, 1, 1]]
print(S.countCornerRectangles(grid))
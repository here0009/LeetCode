"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-meeting-point
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minTotalDistance(self, grid) -> int:
        """
        Thoughts: choose the median of x and y as meeting point
        """
        def dist_to_median(lst):
            lst = sorted(lst)
            length = len(lst)
            median = lst[length//2]
            return sum([abs(num - median) for num in lst])

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        x_s, y_s = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_s.append(i)
                    y_s.append(j)

        return dist_to_median(x_s) + dist_to_median(y_s)

S = Solution()
grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(S.minTotalDistance(grid))
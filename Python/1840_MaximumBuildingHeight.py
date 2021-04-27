"""
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city rst on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city rst on the maximum height of specific buildings. These rst are given as a 2D integer array rst where rst[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in rst, and building 1 will not be in rst.

Return the maximum possible height of the tallest building.

 

Example 1:


Input: n = 5, rst = [[2,1],[4,1]]
Output: 2
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.
Example 2:


Input: n = 6, rst = []
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
Example 3:


Input: n = 10, rst = [[5,3],[2,5],[7,4],[10,3]]
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.
 

Constraints:

2 <= n <= 109
0 <= rst.length <= min(n - 1, 105)
2 <= idi <= n
idi is unique.
0 <= maxHeighti <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-building-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maxBuilding(self, n: int, rst: List[List[int]]) -> int:

        rst.append([1, 0])
        rst.sort()
        if rst[-1][0] != n:
            rst.append([n, n - 1])
        for i in range(1, len(rst)):
            gap = rst[i][0] - rst[i - 1][0]
            rst[i][1] = min(rst[i][1], gap + rst[i - 1][1])
        for i in range(len(rst) - 2, -1, -1):
            gap = rst[i + 1][0] - rst[i][0]
            rst[i][1] = min(rst[i][1], gap + rst[i + 1][1])
        res = 0
        # print(rst)
        for i in range(1, len(rst)):
            # gap = rst[i][0] - rst[i - 1][0]
            # max_v = max(rst[i - 1][1], rst[i][1])
            # min_v = min(rst[i - 1][1], rst[i][1])
            # res = max(res, max_v + (gap - (max_v - min_v)) // 2)
            res = max(res, (rst[i][0] - rst[i - 1][0] + rst[i][1] + rst[i - 1][1]) // 2)
            # print(i, rst[i], res)
        return res

S = Solution()
n = 5
rst = [[2,1],[4,1]]
print(S.maxBuilding(n, rst))
n = 6
rst = []
print(S.maxBuilding(n, rst))
n = 10
rst = [[5,3],[2,5],[7,4],[10,3]]
print(S.maxBuilding(n, rst))
n = 10
rst = [[6,0],[5,2],[7,0],[9,1],[2,4],[3,4],[4,0],[8,2],[10,0]]
print(S.maxBuilding(n, rst))
# 输出：
# 2
# 预期结果：
# 1
"""
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
Example 1:

Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:
​​​​​
Note:

All given positions won't overlap.
The squirrel can take at most one nut at one time.
The given positions of nuts have no order.
Height and width are positive integers. 3 <= height * width <= 10,000.
The given positions contain at least one nut, only one tree and one squirrel.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squirrel-simulation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, height: int, width: int, tree, squirrel, nuts) -> int:
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        length = len(nuts)
        distTree = [0]*length
        distSquirrel = [0]*length
        res = float('inf')
        for i in range(length):
            distTree[i] = dist(nuts[i], tree)
            distSquirrel[i] = dist(nuts[i], squirrel)
            res = min(res, distSquirrel[i]-distTree[i])
        return 2*sum(distTree) + res

S = Solution()

height = 5
width = 7
tree =  [2,2]
squirrel =  [4,4]
nuts = [[3,0], [2,5]]
print(S.minDistance(height, width, tree, squirrel, nuts))

print(S.minDistance(1,3,[0,1],[0,0],[[0,2]]))
# 输出：
# 1
# 预期结果：
# 3

print(S.minDistance(5,5,[3,2],[0,1],[[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]]))

# 输出：
# 108
# 预期结果：
# 100
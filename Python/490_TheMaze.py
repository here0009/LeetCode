"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
 

Constraints:

1 <= maze.length, maze[i].length <= 100
maze[i][j] is 0 or 1.
start.length == 2
destination.length == 2
0 <= startrow, destinationrow <= maze.length
0 <= startcol, destinationcol <= maze[i].length
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The maze contains at least 2 empty spaces.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-maze
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col

        def dfs(i,j,d):
            if [i,j] == destination:
                self.res = True
                return
            visited.add((i,j,d))
            di,dj = directions[d]
            step = 1
            while inRange(i+step*di, j+step*dj) and maze[i+step*di][j+step*dj] == 0:
                step += 1
            step -= 1
            if (i+step*di, j+step*dj, d) not in visited:
                dfs(i+step*di, j+step*dj, d)
            for next_d in range(4):
                if (i,j,next_d) not in visited:
                    dfs(i,j,next_d)

        row, col = len(maze), len(maze[0])
        visited = set()
        self.res = False
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        i,j = start
        # for d in range(4):
        dfs(i,j,0)
        return self.res

S = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(S.hasPath(maze, start, destination))
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(S.hasPath(maze, start, destination))
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(S.hasPath(maze, start, destination))

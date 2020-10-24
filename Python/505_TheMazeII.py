"""There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-maze-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        """
        dfs may not find shortest distance, try to use priority queue
        """
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col

        def dfs(i,j,d,dist):
            if [i,j] == destination:
                self.res = min(self.res, dist)
                return
            visited.add((i,j,d))
            for next_d in range(4):
                if (i,j,next_d) not in visited:
                    dfs(i,j,next_d,dist)
            di,dj = directions[d]
            step = 1
            while inRange(i+step*di, j+step*dj) and maze[i+step*di][j+step*dj] == 0:
                step += 1
            step -= 1
            if (i+step*di, j+step*dj, d) not in visited:
                dfs(i+step*di, j+step*dj, d, dist+step)

        # for line in maze:
        #     print(line)
        row, col = len(maze), len(maze[0])
        visited = set()
        self.res = float('inf')
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        i,j = start
        for d in range(4):
            dfs(i,j,d,0)
        return self.res if self.res != float('inf') else -1

# 作者：user2198v
# 链接：https://leetcode-cn.com/problems/the-maze-ii/solution/mi-gong-2you-xian-dui-lie-bfs-by-user2198v/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
import heapq
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        m,n = len(maze),len(maze[0])
        start,destination = tuple(start),tuple(destination)
        stack = [(0,start)]
        visited = set()

        while stack:
            path,cur = heapq.heappop(stack)
            if cur == destination:
                return path
            visited.add(cur)
            for dx,dy in direction:
                x,y = cur
                length = 0
                while x+dx >= 0 and x+dx < m and y+dy >= 0 and y+dy < n and maze[x+dx][y+dy] == 0:
                    x,y = x+dx,y+dy
                    length += 1
                if (x,y) not in visited:
                    heapq.heappush(stack,(path+length,(x,y)))
        return -1


import heapq
class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col

        row, col = len(maze), len(maze[0])
        visited = set()
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        si,sj = start
        pq = []
        heapq.heappush(pq, (0,si,sj,0))
        visited.add((si,sj,0))

        while pq:
            dist, i, j, d = heapq.heappop(pq)
            if [i,j] == destination:
                return dist
            for next_d in range(4):
                if (i,j,next_d) not in visited:
                    visited.add((i,j,next_d))
                    heapq.heappush(pq, (dist,i,j,next_d))
            di,dj = directions[d]
            step = 1
            while inRange(i+step*di, j+step*dj) and maze[i+step*di][j+step*dj] == 0:
                step += 1
            step -= 1
            if (i+step*di, j+step*dj, d) not in visited:
                heapq.heappush(pq, (dist+step, i+step*di, j+step*dj, d))
        return -1


import heapq
class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col

        row, col = len(maze), len(maze[0])
        visited = set()
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        si,sj = start
        pq = []
        heapq.heappush(pq, (0,si,sj))

        while pq:
            dist, i, j = heapq.heappop(pq)
            visited.add((i,j)) #(i,j) is added here
            if [i,j] == destination:
                return dist
            for di,dj in directions:
                ni,nj = i,j
                steps = 0
                while inRange(ni+di,nj+dj) and maze[ni+di][nj+dj] == 0:
                    ni += di
                    nj += dj
                    steps += 1
                if (ni,nj) not in visited:
                    # visited.add((i,j)) # ni,nj can not be added here, there may exist the same ni,nj but with shorter dist, add (ni,nj) here won't pass some test cases
                    heapq.heappush(pq, (dist+steps, ni, nj))
        return -1

S = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(S.shortestDistance(maze, start, destination))
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(S.shortestDistance(maze, start, destination))
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(S.shortestDistance(maze, start, destination))
maze =[[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
start = [0,0]
destination =[8,6]
print(S.shortestDistance(maze, start, destination))
# 输出：
# 54
# 预期结果：
# 26
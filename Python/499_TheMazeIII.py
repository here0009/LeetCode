"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

 

Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-maze-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq
class Solution:
    def findShortestWay(self, maze, ball, hole) -> str:
        def inRange(i,j):
            return 0 <= i < row and 0 <= j < col

        row, col = len(maze), len(maze[0])
        visited = set()
        shortest_dist = float('inf')
        res_list = []
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        path_string = 'ldru'
        si,sj = ball
        pq = []
        for d in range(4):
            heapq.heappush(pq, (0, path_string[d], si,sj,d))
            visited.add((si,sj,d))

        while pq:
            dist, path, i, j, d = heapq.heappop(pq)
            for next_d in range(4):
                if (i,j,next_d) not in visited:
                    visited.add((i,j,next_d))
                    heapq.heappush(pq, (dist, path+path_string[next_d], i,j,next_d))
            di,dj = directions[d]
            step = 1
            while inRange(i+step*di, j+step*dj) and maze[i+step*di][j+step*dj] == 0:
                if [i+step*di, j+step*dj] == hole:
                    tmp_dist = dist+step
                    if tmp_dist < shortest_dist:
                        res_list = [path]
                        shortest_dist = tmp_dist
                    elif tmp_dist == shortest_dist:
                        res_list.append(path)
                step += 1
            step -= 1
            if (i+step*di, j+step*dj, d) not in visited and dist+step <= shortest_dist:
                heapq.heappush(pq, (dist+step, path, i+step*di, j+step*dj, d))

        return min(res_list) if res_list else 'impossible'


S = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(S.findShortestWay(maze, start, destination))
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(S.findShortestWay(maze, start, destination))
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(S.findShortestWay(maze, start, destination))
maze =[[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
start = [0,0]
destination =[8,6]
print(S.findShortestWay(maze, start, destination))

maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(S.findShortestWay(maze, start, destination))
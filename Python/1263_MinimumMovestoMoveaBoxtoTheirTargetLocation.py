"""
Storekeeper is a game, in which the player pushes boxes around in a warehouse, trying to get them to target locations.

The game is represented by a grid of size n*m, where each element is a wall, floor or a box.

Your task is move the box 'B' to the target position 'T' under the following rules:

Player is represented by character 'S' and can move up, down, left, right in the grid if its a floor (empy cell).
Floor is represented by character '.' that means free cell to walk.
Wall is represented by character '#' that means obstacle  (impossible to walk there). 
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:



Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.
Example 4:

Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1
 

Constraints:

1 <= grid.length <= 20
1 <= grid[i].length <= 20
grid contains only characters '.', '#',  'S' , 'T', or 'B'.
There is only one character 'S', 'B' and 'T' in the grid.
"""


class Solution:
    def minPushBox(self, grid) -> int:
        """
        Thoughts: use bfs to find the min path
        use dfs to check the postions that the player can get to
        because the box may block the way, we need to recaculat it every time.
        may be try to use union-find to check if player and postion are connected
        because the player can only push the box, so he can definetely go back to where he was started unless the box was there
        hard to implement
        """
        def connected(p, q, b):
            # print('connected' ,p, q, b)
            grid[b[0]][b[1]] = '#'
            seen = set([p])
            bfs = set([p])
            while bfs:
                bfs2 = set()
                # print(bfs)
                for pos in bfs:
                    if pos == q:
                        grid[b[0]][b[1]] = '.'
                        return True
                    for nxt_pos in neighbors(pos):
                        if nxt_pos not in seen:
                            seen.add(nxt_pos)
                            bfs2.add(nxt_pos)
                bfs = bfs2
            grid[b[0]][b[1]] = '.'
            return False

        def valid_pos(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != '#'

        def neighbors(pos):
            i, j = pos
            for k in range(4):
                ti, tj = i + dir4[k][0], j + dir4[k][1]
                if valid_pos(ti, tj):
                    yield (ti, tj)


        def neighbors2(pos):
            """
            generate the valid target postion and push position for input postion
            """
            # print(pos)
            i, j = pos
            for k in range(4):
                ti, tj = i + dir4[k][0], j + dir4[k][1]
                pi, pj = i + dir4[~k][0], j + dir4[~k][1]
                if valid_pos(ti, tj) and valid_pos(pi, pj):
                    yield (ti, tj), (pi, pj)

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)

        dir4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        bfs = set()
        visited = set()
        bfs.add((box, player))
        visited.add((box, player))
        steps = 0
        while bfs:
            # print(bfs)
            bfs2 = set()
            for b, p in bfs:
                # print(b, p)
                if b == target:
                    return steps
                for nxt_b, nxt_p in neighbors2(b):
                    # print(nxt_b, nxt_p)
                    if (nxt_b, nxt_p) not in visited and connected(p, nxt_p, b):
                        visited.add((nxt_b, nxt_p))
                        bfs2.add((nxt_b, nxt_p))
            steps += 1
            bfs = bfs2
        return -1


import heapq
class Solution:
    def minPushBox(self, grid) -> int:
        """
        Thoughts: use bfs to find the min path
        use dfs to check the postions that the player can get to
        because the box may block the way, we need to recaculat it every time.
        may be try to use union-find to check if player and postion are connected
        because the player can only push the box, so he can definetely go back to where he was started unless the box was there
        hard to implement
        """
        def heuristic(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        def connected(p, q, b):
            grid[b[0]][b[1]] = '#'
            seen = set([p])
            pq = [(heuristic(p, q), 0, p)]
            while pq:
                _, steps, pos = heapq.heappop(pq)
                if pos == q:
                    grid[b[0]][b[1]] = '.'
                    return True
                steps += 1
                for nxt_pos in neighbors(pos):
                    if nxt_pos not in seen:
                        seen.add(nxt_pos)
                        heapq.heappush(pq, (heuristic(nxt_pos, q) + steps, steps, nxt_pos))
            grid[b[0]][b[1]] = '.'
            return False

        def valid_pos(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != '#'

        def neighbors(pos):
            i, j = pos
            for k in range(4):
                ti, tj = i + dir4[k][0], j + dir4[k][1]
                if valid_pos(ti, tj):
                    yield (ti, tj)


        def neighbors2(pos):
            i, j = pos
            for k in range(4):
                ti, tj = i + dir4[k][0], j + dir4[k][1]
                pi, pj = i + dir4[~k][0], j + dir4[~k][1]
                if valid_pos(ti, tj) and valid_pos(pi, pj):
                    yield (ti, tj), (pi, pj)

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)

        dir4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pq = [(heuristic(box, target), 0, box, player)]
        visited = set()
        visited.add((box, player))
        while pq:
            _, steps, b, p = heapq.heappop(pq)
            if b == target:
                return steps
            steps += 1
            for nxt_b, nxt_p in neighbors2(b):
                if (nxt_b, nxt_p) not in visited and connected(p, nxt_p, b):
                    visited.add((nxt_b, nxt_p))
                    heapq.heappush(pq, (heuristic(nxt_b, target) + steps, steps, nxt_b, nxt_p))
        return -1


class Solution:
    def minPushBox(self, grid) -> int:     
        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])
        
        def out_bounds(location):  # return whether the location is in the grid and not a wall
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == "#"
              
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "T":
                    target = (r, c)
                if grid[r][c] == "B":
                    start_box = (r, c)
                if grid[r][c] == "S":
                    start_person = (r, c)

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()
        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in visited: # do not visit same state again
                continue
            visited.add((person, box))
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_person = (person[0] + dr, person[1] + dc)  # move person rather than box, count the box, clever trick
                if out_bounds(new_person):
                    continue
                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box]) # box remains same
        return -1

S = Solution()
grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
print(S.minPushBox(grid))
grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#","#","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
print(S.minPushBox(grid))
grid = [["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
print(S.minPushBox(grid))
grid = [["#","#","#","#","#","#","#"],["#","S","#",".","B","T","#"],["#","#","#","#","#","#","#"]]
print(S.minPushBox(grid))
grid = [[".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".","#","#",".","B",".",".",".",".","."],[".",".",".","#",".",".",".",".","#","#",".","."],[".",".","#",".",".",".",".",".",".",".",".","."],["#",".","#",".",".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".",".","S",".","T","#"],[".","#",".",".",".","#",".",".",".",".",".","#"],["#",".",".",".",".","#",".",".","#",".",".","."],["#",".",".","#","#",".",".",".",".",".",".","."],[".",".",".",".","#",".","#",".",".",".","#","."],[".",".","#",".","#",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".","#"]]
print(S.minPushBox(grid))
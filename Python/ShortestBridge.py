"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
class Solution:
    def shortestBridge(self, A) -> int:
        def inRange(i,j):
            return i>=0 and i<n and j>=0 and j<n

        def dfs(i,j):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs.append((i,j))
                for di,dj in directions:
                    if inRange(i+di,j+dj) and A[i+di][j+dj] == 1:
                        dfs(i+di,j+dj)

        n = len(A)
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        break_flag = False
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    start_i,start_j = i,j
                    break
            if break_flag:
                break


        visited = [[0]*n for _ in range(n)]
        bfs = []
        dfs(start_i,start_j)
        # print(start_i,start_j)
        # print(bfs)
        counts = 0
        visited = [[0]*n for _ in range(n)] #refresh it
        for i,j in bfs:
            visited[i][j] = 1
        while bfs: 
            bfs2 = []
            for i,j in bfs:
                for di,dj in directions:
                    tmp_i,tmp_j = i+di,j+dj
                    if inRange(tmp_i,tmp_j) and visited[tmp_i][tmp_j] == 0:
                        visited[tmp_i][tmp_j] = 1
                        if A[tmp_i][tmp_j] == 0:
                            bfs2.append((i+di,j+dj))
                        else:
                            return counts
            # print(bfs2)
            counts += 1
            bfs = bfs2 

        return counts

S = Solution()
A = [[0,1],[1,0]]
print(S.shortestBridge(A))
A = [[0,1,0],[0,0,0],[0,0,1]]
print(S.shortestBridge(A))
A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(S.shortestBridge(A))
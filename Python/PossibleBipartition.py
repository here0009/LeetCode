"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
from collections import defaultdict
class Solution_1:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        def dfs(node,layer):
            # print(node,layer%2)
            if not self.res:
                return
            if layer%2 == 0:
                if node not in q:
                    p.add(node)
                else:
                    self.res = False
                    return
            else:
                if node not in p:
                    q.add(node)
                else:
                    self.res = False
                    return
            for neighbor in graph[node]:
                dfs(neighbor, layer+1)

        self.res = True
        graph = defaultdict(list)
        
        for i,j in dislikes:
            graph[i].append(j)

        for node in range(N):
            p,q = set(),set() #p for even, q for odd
            if node not in p and node not in q:
                dfs(node,0)

        return self.res


from collections import defaultdict
from collections import deque
class Solution_2:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = defaultdict(list)
        visited = [-1]*(N+1)
        dislikes = sorted(dislikes)
        for i,j in dislikes:
            graph[i].append(j)
            # graph[j].append(i)

        # print(graph)
        for i in range(1,N):
            # print(i)
            if visited[i] == -1:
                visited[i] = 0
                bfs = deque([(i,0)])
                while bfs:
                    print(bfs)
                    node,flag = bfs.popleft()
                    if visited[node] == -1:
                        visited[node] = flag
                    elif visited[node] != flag:
                        print(node, visited[node], flag)
                        return False

                    for neighbor in graph[node]:
                        if visited[neighbor] == -1:
                            bfs.append((neighbor,1-flag))
                        elif visited[neighbor] == flag:
                            print(neighbor, visited[neighbor], flag)
                            return False
        # print(bfs)
        return True

from collections import defaultdict
from collections import deque
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = defaultdict(list)
        visited = [-1]*(N+1)
        dislikes = sorted(dislikes)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        for i in range(1,N):
            if visited[i] == -1:
                visited[i] = 0
                bfs = deque([(i,0)])
                while bfs:
                    # print(bfs)
                    node,flag = bfs.popleft()
                    if visited[node] == -1:
                        visited[node] = flag
                    elif visited[node] != flag:
                        # print(node, visited[node], flag)
                        return False

                    for neighbor in graph[node]:
                        if visited[neighbor] == -1:
                            bfs.append((neighbor,1-flag))
                        elif visited[neighbor] == flag:
                            # print(neighbor, visited[neighbor], flag)
                            return False
        return True


from collections import defaultdict
from collections import deque
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = defaultdict(list)
        visited = [-1]*(N+1)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        for i in range(1,N):
            if visited[i] == -1:
                visited[i] = 0
                bfs = deque([(i,0)])
                while bfs:
                    node,flag = bfs.popleft()
                    for neighbor in graph[node]:
                        if visited[neighbor] == -1:
                            visited[neighbor] = 1-flag
                            bfs.append((neighbor,1-flag))
                        elif visited[neighbor] == flag:
                            return False
        return True


from collections import defaultdict
from collections import deque
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(neighbor, 1-c) for neighbor in graph[node])

        graph = defaultdict(list)
        color = dict()
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        return all(dfs(node, 0) for node in range(1,N+1) if node not in color)

S = Solution()
N = 4
dislikes = [[1,2],[1,3],[2,4]]
print(S.possibleBipartition(N,dislikes))
N = 3
dislikes = [[1,2],[1,3],[2,3]]
print(S.possibleBipartition(N,dislikes))
N = 6
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(S.possibleBipartition(N,dislikes))


N = 50
dislikes =[[21,47],[4,41],[2,41],[36,42],[32,45],[26,28],[32,44],[5,41],[29,44],[10,46],[1,6],[7,42],[46,49],[17,46],[32,35],[11,48],[37,48],[37,43],[8,41],[16,22],[41,43],[11,27],[22,44],[22,28],[18,37],[5,11],[18,46],[22,48],[1,17],[2,32],[21,37],[7,22],[23,41],[30,39],[6,41],[10,22],[36,41],[22,25],[1,12],[2,11],[45,46],[2,22],[1,38],[47,50],[11,15],[2,37],[1,43],[30,45],[4,32],[28,37],[1,21],[23,37],[5,37],[29,40],[6,42],[3,11],[40,42],[26,49],[41,50],[13,41],[20,47],[15,26],[47,49],[5,30],[4,42],[10,30],[6,29],[20,42],[4,37],[28,42],[1,16],[8,32],[16,29],[31,47],[15,47],[1,5],[7,37],[14,47],[30,48],[1,10],[26,43],[15,46],[42,45],[18,42],[25,42],[38,41],[32,39],[6,30],[29,33],[34,37],[26,38],[3,22],[18,47],[42,48],[22,49],[26,34],[22,36],[29,36],[11,25],[41,44],[6,46],[13,22],[11,16],[10,37],[42,43],[12,32],[1,48],[26,40],[22,50],[17,26],[4,22],[11,14],[26,39],[7,11],[23,26],[1,20],[32,33],[30,33],[1,25],[2,30],[2,46],[26,45],[47,48],[5,29],[3,37],[22,34],[20,22],[9,47],[1,4],[36,46],[30,49],[1,9],[3,26],[25,41],[14,29],[1,35],[23,42],[21,32],[24,46],[3,32],[9,42],[33,37],[7,30],[29,45],[27,30],[1,7],[33,42],[17,47],[12,47],[19,41],[3,42],[24,26],[20,29],[11,23],[22,40],[9,37],[31,32],[23,46],[11,38],[27,29],[17,37],[23,30],[14,42],[28,30],[29,31],[1,8],[1,36],[42,50],[21,41],[11,18],[39,41],[32,34],[6,37],[30,38],[21,46],[16,37],[22,24],[17,32],[23,29],[3,30],[8,30],[41,48],[1,39],[8,47],[30,44],[9,46],[22,45],[7,26],[35,42],[1,27],[17,30],[20,46],[18,29],[3,29],[4,30],[3,46]]
print(S.possibleBipartition(N,dislikes))
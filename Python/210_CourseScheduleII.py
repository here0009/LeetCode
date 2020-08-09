"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        bfs = []
        res = []
        out_edges = defaultdict(list)
        in_edges = defaultdict(set)
        for i, j in prerequisites:
            out_edges[j].append(i)
            in_edges[i].add(j)
        for i in range(numCourses):
            if i not in in_edges:
                bfs.append(i)
        res = bfs[:]
        # print(bfs)
        # print(out_edges)
        # print(in_edges)
        while bfs:
            bfs2 = []
            for course in bfs:
                for next_course in out_edges[course]:
                    if course in in_edges[next_course]:
                        in_edges[next_course].remove(course)
                        if len(in_edges[next_course]) == 0:
                            bfs2.append(next_course)
                            res.append(next_course)
            bfs = bfs2
        return res if len(res) == numCourses else []

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        pre, suc = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        out = []
        while free:
            a = free.pop()
            out.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return out if (len(out) == numCourses) else []

class Solution:
    def findOrder(self, numCourses, prerequisites):
        def dfs_circle(x):
            vis[x] = -1
            for y in G[x]:
                if vis[y] < 0 or (not vis[y] and dfs_circle(y)):
                    return True
            vis[x] = 1
            orders.append(x)
            return False

        G = [set() for _ in range(numCourses)]
        for d, s in prerequisites:
            G[s].add(d)
        vis, orders = [0]*numCourses, []
        for x in range(numCourses):
            if not vis[x] and dfs_circle(x):
                return []
        return orders[::-1]

# https://leetcode.com/problems/course-schedule-ii/discuss/311215/Different-Python-solutions-(BFS-DFS)
# Method 4: recursive DFS: visited[i] == 0 means not visited before, visited[i] == 1 means visited in the current path, visited[i] == 2 means visited before.
# Time complexity O(n + m) (Beat 94.95%)
class Solution:
    def findOrder(self, numCourses, prerequisites):
        def dfs(i):
            visited[i] = 1
            for j in edges[i]:
                if visited[j] == 1:
                    return False
                elif visited[j] == 0:
                    if not dfs(j):
                        return False
            finish_order.append(i)
            visited[i] = 2
            return True
        
        edges = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            edges[v].append(u)
        visited = [0 for _ in range(numCourses)]
        finish_order = []
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return finish_order[::-1]


S = Solution()
numCourses = 2
prerequisites = [[1,0]] 
print(S.findOrder(numCourses, prerequisites))
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(S.findOrder(numCourses, prerequisites))
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(S.findOrder(numCourses, prerequisites))

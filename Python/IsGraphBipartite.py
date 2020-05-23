"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0-----1
| \\  |
|  \\ |
3-----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""
class Solution:
    def isBipartite(self, graph) -> bool:
        """
        wrong answer
        """
        a_list = [0]
        b_list = []
        a_set = set(a_list)
        b_set = set(b_list)
        while a_list or b_list:
            print(a_list)
            print(b_list)
            tmp = []
            if len(a_list) > 0:
                for a in a_list:
                    tmp.extend(graph[a])
                    b_list = tmp
                if a_set & set(b_list):
                    return False
                b_set |= set(b_list)
                a_list = []
            elif len(b_list) > 0:
                for b in b_list:
                    tmp.extend(graph[b])
                    a_list = tmp
                if b_set & set(a_list):
                    return False
                a_set |= set(a_list)
                b_list = []
        print(a_set)
        print(b_set)
        return True

class Solution:
    def isBipartite(self, graph) -> bool:
        """
        dfs or bfs from node 0, recored the visited nodes, if node 1 is not in recoreded nodes, then it can be colored either the same as node 0 or the opposite as node 0, it does not matter
        """
        def dfs(node):
            for ngb in graph[node]:
                if ngb in colored:
                    if colored[ngb] == colored[node]:
                        return False
                else:
                    colored[ngb] = 1 - colored[node]
                    if not dfs(ngb):
                        return False
            return True

        colored = dict()
        for node,ngbs in enumerate(graph):
            if node not in colored:
                colored[node] = 0
                if not dfs(node):
                    return False
        return True


class Solution_1:
    def isBipartite(self, graph) -> bool:
        """
        dfs or bfs from node 0, recored the visited nodes, if node 1 is not in recoreded nodes, then it can be colored either the same as node 0 or the opposite as node 0, it does not matter
        BFS
        """
        colored = dict()
        for node in range(len(graph)):
            if node not in colored:
                colored[node] = 0            
            stack = [node]
            while stack:
                j = stack.pop()
                for i in graph[j]:
                    if i in colored:
                        if colored[i] == colored[j]:
                            return False
                    else:
                        colored[i] = 1 - colored[j]
                        stack.append(i)            
        return True

                
            




s = Solution()
graph = [[1,3], [0,2], [1,3], [0,2]]
print(s.isBipartite(graph))

graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
print(s.isBipartite(graph))

graph = [[1],[0,3],[3],[1,2]]
print(s.isBipartite(graph))
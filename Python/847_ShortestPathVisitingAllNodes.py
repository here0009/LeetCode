"""
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
"""


class Solution:
    def shortestPathLength(self, graph) -> int:
        """
        because we need to revisit nodes, we can not simply use a set to record the visited nodes. but we can use bitmask to record the visited node
        rather than start from a single nodes, we start from all the nodes
        """
        length = len(graph)
        target = (1 << length) - 1
        # print(graph)
        # print(target)
        bfs = set((i, 1<<i) for i in range(length))
        seen = set((i, 1<<i) for i in range(length))
        step = 0
        while bfs:
            bfs2 = set()
            for i, mask in bfs:
                if mask == target:
                    return step
                for j in graph[i]:
                    m2 = mask | 1<<j
                    if (j, m2) not in seen:
                        bfs2.add((j, m2))
                        seen.add((j, m2))
            bfs = bfs2
            step += 1
        return None


S = Solution()
graph = [[1,2,3],[0],[0],[0]]
print(S.shortestPathLength(graph))

graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(S.shortestPathLength(graph))
"""
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
 

Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        red_dict = defaultdict(list)
        blue_dict = defaultdict(list)
        for i,j in red_edges:
            red_dict[i].append(j)
        for i,j in blue_edges:
            blue_dict[i].append(j)

        def dfs()

        res = [0]
        red_res = [0] + [-1]*n-1
        blue_res = [0] + [-1]*n-1
        red_res = red_dict[0] #start from red_dict[0]
        blue_res = blue_dict[0] #start from blue_dict[0]
        for i,v in enumerate(red_res):
            if v == -1:
                red_res = dfs(0,i,'r')
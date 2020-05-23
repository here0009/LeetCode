"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, otherwise, it does not have any apple.

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 2:



Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Constraints:

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""
# class TreeNode(x):
#     self.val = x
#     self.gotApple = False
#     self.left = None
#     self.right = None

from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        def dfs_appletree(node):
            res = int(hasApple[node])
            if node in tree:
                res += sum([dfs_appletree(child) for child in tree[node]])
            apples_in_subtree[node] = res
            return res

        apples_in_subtree = dict()
        tree = defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
        dfs_appletree(0)
        # print(apples_in_subtree)
        bfs = [0]
        res = 0
        while bfs:
            bfs2 = []
            for node in bfs:
                if node in tree:
                    for child in tree[node]:
                        if apples_in_subtree[child] > 0:
                            bfs2.append(child)
            res += len(bfs)
            bfs = bfs2
        return (res-1)*2


S = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
print(S.minTime(n, edges, hasApple))
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]
print(S.minTime(n, edges, hasApple))
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,False,False,False,False,False]
print(S.minTime(n, edges, hasApple))


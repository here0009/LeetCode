"""
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return

1 if the mouse wins the game,
2 if the cat wins the game, or
0 if the game is a draw.
 

Example 1:


Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Example 2:


Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
 

Constraints:

3 <= graph.length <= 50
1 <= graph[i].length < graph.length
0 <= graph[i][j] < graph.length
graph[i][j] != i
graph[i] is unique.
The mouse and the cat can always move.
"""

# https://leetcode.com/problems/cat-and-mouse/discuss/298937/DP-memory-status-search-search-strait-forward-and-easy-to-understand
# https://www.acwing.com/solution/leetcode/content/556/
from typing import List
from functools import lru_cache
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(t, mouse, cat):
            if t == 2 * N:
                return 0
            if mouse == 0:
                return 1
            if mouse == cat:
                return 2
            if t % 2 == 0:
                if any(dp(t + 1, m2, cat) == 1 for m2 in graph[mouse]):
                    return 1
                if all(dp(t + 1, m2, cat) == 2 for m2 in graph[mouse]):
                    return 2
                return 0
            else:
                if any(dp(t + 1, mouse, c2) == 2 for c2 in graph[cat] if c2 != 0):
                    return 2
                if all(dp(t + 1, mouse, c2) == 1 for c2 in graph[cat] if c2 != 0):
                    return 1
                return 0

        N = len(graph)
        return dp(0, 1, 2)


S = Solution()
graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
print(S.catMouseGame(graph))
graph = [[1,3],[0],[3],[0,2]]
print(S.catMouseGame(graph))
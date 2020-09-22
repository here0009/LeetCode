"""
There is a strange printer with the following two special requirements:

On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
Once the printer has used a color for the above operation, the same color cannot be used again.
You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

Return true if it is possible to print the matrix targetGrid, otherwise, return false.

 

Example 1:



Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
Output: true
Example 2:



Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
Output: true
Example 3:

Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
Output: false
Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
Example 4:

Input: targetGrid = [[1,1,1],[3,1,3]]
Output: false
 

Constraints:

m == targetGrid.length
n == targetGrid[i].length
1 <= m, n <= 60
1 <= targetGrid[row][col] <= 60
"""



class Solution:
    def isPrintable(self, targetGrid) -> bool:
        """
        Thoughts: record the topleft and bottomright index of a color, if this square got the same color(or same color + visited grid), we can put the color in visited.
        Iterate unvisited color until no change in the unvisited color
        """
        R, C = len(targetGrid), len(targetGrid[0])
        visited = [[0]*C for _ in range(R)]
        pos_dict = dict()
        color_set = set()

        for i in range(R):
            for j in range(C):
                color = targetGrid[i][j]
                if color not in pos_dict:
                    pos_dict[color] = [i,j,i,j]
                    color_set.add(color)
                else:
                    n,w,s,e = pos_dict[color] # north, west, south, east
                    pos_dict[color] = [min(n,i), min(w,j), max(s,i), max(e,j)]


        # print(pos_dict)
        # print(color_set)
        def test(color):
            cord = pos_dict[color]
            n, w, s, e = cord
            unvisited = set()
            for i in range(n, s+1):
                for j in range(w, e+1):
                    if visited[i][j] == 0:
                        if targetGrid[i][j] != color:
                            return False
                        else:
                            unvisited.add((i,j))
            for i,j in unvisited:
                visited[i][j] = 1
            return True

        while color_set:
            color_set2 = set()
            for color in color_set:
                if not test(color):
                    color_set2.add(color)
            if len(color_set) == len(color_set2):
                return False
            color_set = color_set2
        return True
# https://leetcode.com/problems/strange-printer-ii/discuss/854185/Python-3-N3-with-clean-code
# toplogical sort
from collections import defaultdict
class Solution:
    def isPrintable(self, targetGrid) -> bool:
        R, C = len(targetGrid), len(targetGrid[0])
        pos_dict = dict()

        for i in range(R):
            for j in range(C):
                color = targetGrid[i][j]
                if color not in pos_dict:
                    pos_dict[color] = [i,j,i,j]
                else:
                    n,w,s,e = pos_dict[color] # north, west, south, east
                    pos_dict[color] = [min(n,i), min(w,j), max(s,i), max(e,j)]

        graph = defaultdict(set)
        for color, cord in pos_dict.items():
            n,w,s,e = pos_dict[color]
            for i in range(n, s+1):
                for j in range(w, e+1):
                    if targetGrid[i][j] != color:
                        graph[color].add(targetGrid[i][j])

        visited = set()
        processing = set()
        def dfs(node):
            processing.add(node)
            for pre_node in graph[node]:
                if pre_node not in visited:
                    if pre_node in processing or not dfs(pre_node):
                        return False
            processing.remove(node)
            visited.add(node)
            return True

        for node in pos_dict.keys():
            if node not in visited:
                if not dfs(node):
                    return False
        return True



S = Solution()
targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
print(S.isPrintable(targetGrid))
targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
print(S.isPrintable(targetGrid))
targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
print(S.isPrintable(targetGrid))
targetGrid = [[1,1,1],[3,1,3]]
print(S.isPrintable(targetGrid))
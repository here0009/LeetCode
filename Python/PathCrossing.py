"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

 

Example 1:



Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:



Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 10^4
path will only consist of characters in {'N', 'S', 'E', 'W}
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction_dict = {'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)}
        visited = set()
        pos = [0, 0]
        visited.add(tuple(pos))
        for d in path:
            di,dj = direction_dict[d]
            pos[0], pos[1] = pos[0] + di, pos[1] + dj
            t_pos = tuple(pos)
            if t_pos in visited:
                return True
            visited.add(t_pos)
        return False


S = Solution()
path = "NES"
print(S.isPathCrossing(path))
path = "NESWW"
print(S.isPathCrossing(path))
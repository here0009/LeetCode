"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""
from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        visited = {x,y}
        if z == x or z == y or z == 0:
            return True
        bfs = deque([abs(x-y)])
        while bfs:
            # print(bfs)
            r = bfs.popleft()
            if r == z or r+x == z or r+y == z:
                return True
            visited.add(r)
            if abs(x-r) not in visited:
                bfs.append(abs(x-r))
            if abs(y-r) not in visited:
                bfs.append(abs(y-r))
        return False

S = Solution()
x = 3
y = 5
z = 4
print(S.canMeasureWater(x,y,z))
x = 2
y = 6
z = 5
print(S.canMeasureWater(x,y,z))
x = 1
y = 2
z = 3
print(S.canMeasureWater(x,y,z))

x = 1
y = 0
z = 0
print(S.canMeasureWater(x,y,z))

x = 11
y = 13
z = 0
print(S.canMeasureWater(x,y,z))
"""
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        print(sx,sy,tx,ty)
        while True:
            # put smaller num at the beginning
            if sx > sy:
                sx, sy = sy, sx
            if tx > ty:
                tx, ty = ty, tx
            print(sx,sy,tx,ty)
            if sx == tx and sy == ty:
                return True
            elif sy > tx:
                return False
            tx, ty = ty - tx, tx


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx #because tx > sx and ty > sy, so we know both tx and ty have not reach the final points, we can use the % operation
        return (sx == tx and sy <= ty and (ty - sy) % sx == 0) or (sy == ty and sx <= tx and (tx - sx) % sy == 0)

S = Solution()
sx = 1
sy = 1
tx = 3
ty = 5
print(S.reachingPoints(sx, sy, tx, ty))
sx = 1
sy = 1
tx = 2
ty = 2
print(S.reachingPoints(sx, sy, tx, ty))
sx = 1
sy = 1
tx = 1
ty = 1
print(S.reachingPoints(sx, sy, tx, ty))

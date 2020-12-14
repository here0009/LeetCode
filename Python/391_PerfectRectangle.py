"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
"""


from typing import List
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        TLE
        """
        si, sj, ei, ej = float('inf'), float('inf'), float('-inf'), float('-inf')
        for a, b, c, d in rectangles:
            si = min(si, a)
            sj = min(sj, b)
            ei = max(ei, c)
            ej = max(ej, d)
        # print(si,sj,ei,ej)
        matrix = [[0]*(ej-sj) for _ in range(ei-si)]
        # print(matrix)
        for a, b, c, d in rectangles:
            a, b, c, d = a-si, b-sj, c-si, d-sj
            for i in range(a, c):
                for j in range(b, d):
                    if matrix[i][j] == 1:
                        return False
                    matrix[i][j] = 1
        # for row in matrix:
        #     print(row)
        return sum(sum(row) for row in matrix) == (ej-sj)*(ei-si)
"""
The right answer must satisfy two conditions:

the large rectangle area should be equal to the sum of small rectangles
count of all the points should be even, and that of all the four corner points should be one

https://leetcode.com/problems/perfect-rectangle/discuss/87180/O(n)-solution-by-counting-corners-with-detailed-explaination
"""


from typing import List
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        si, sj, ei, ej = float('inf'), float('inf'), float('-inf'), float('-inf')
        corners = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            si = min(si, x1)
            sj = min(sj, y1)
            ei = max(ei, x2)
            ej = max(ej, y2)
            area += (x2-x1)*(y2-y1)
            for coord in [(x1,y1),(x2,y1),(x1,y2),(x2,y2)]:
                if coord not in corners:
                    corners.add(coord)
                else:
                    corners.remove(coord)
        return area == (ei-si)*(ej-sj) and corners == set([(si,sj),(ei,ej),(si,ej),(ei,sj)])


S = Solution()
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(S.isRectangleCover(rectangles))
rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
print(S.isRectangleCover(rectangles))
rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
print(S.isRectangleCover(rectangles))
rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
print(S.isRectangleCover(rectangles))
rectangles = [[0,0,4,1],[0,0,4,1]]
print(S.isRectangleCover(rectangles))
"""
Virtual User Accepted: 0
Virtual User Tried: 0
Virtual Total Accepted: 0
Virtual Total Submissions: 0
Difficulty: Medium
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""
class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
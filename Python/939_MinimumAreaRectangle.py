"""
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


from collections import defaultdict
class Solution:
    def minAreaRect(self, points) -> int:
        p_dict = defaultdict(set)
        for x, y in points:
            p_dict[x].add(y)
        res = float('inf')
        # print(p_dict)
        x_list = sorted(p_dict.keys())
        for i in range(len(x_list) - 1):
            for j in range(i+1, len(x_list)):
                y_set = p_dict[x_list[i]] & p_dict[x_list[j]]
                # print(y_set)
                if len(y_set) >= 2:
                    y_list = sorted(y_set)
                    tmp = (x_list[j] - x_list[i]) * min(y_list[k] - y_list[k-1] for k in range(1, len(y_list)))
                    res = min(res, tmp)
        return res if res != float('inf') else 0

class Solution:
    def minAreaRect(self, points) -> int:
        visited = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    res = min(res, abs(y2 -y1) * abs(x2 -x1))
            visited.add((x1, y1))
        return res if res != float('inf') else 0

S = Solution()
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(S.minAreaRect(points))
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(S.minAreaRect(points))
points = [[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]
print(S.minAreaRect(points))
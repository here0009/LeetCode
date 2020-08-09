"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""


class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0], x[1]))
        # print(points)
        res = 1
        start, end = points[0]
        for i in range(1, len(points)):
            s_i, e_i = points[i]
            if s_i > end:
                res += 1
                start, end = s_i, e_i
            else:
                start, end = max(start, s_i), min(end, e_i)
        return res


class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0], x[1]))
        # print(points)
        res = 1
        end = points[0][1]
        for i in range(1, len(points)):
            s_i, e_i = points[i]
            if s_i > end: #since points were sorted, s_i is always bigger than start
                res += 1
                end = e_i
            else:
                end = min(end, e_i)
        return res


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        arrows = 1
        left = points[0][1]    
        for p in range(1,len(points)):                    
            if left < points[p][0]:               
                arrows += 1
                left = points[p][1]                     
        return arrows

S = Solution()
points = [[10,16], [2,8], [1,6], [7,12]]
print(S.findMinArrowShots(points))
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(S.findMinArrowShots(points))
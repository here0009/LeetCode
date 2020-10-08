"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, in other words, answer whether or not if there exists a line that after reflecting all points over the given line the set of the original points is the same that the reflected ones.

Note that there can be repeated points.

Follow up:
Could you do better than O(n2) ?

 

Example 1:


Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.
Example 2:


Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
 

Constraints:

n == points.length
1 <= n <= 10^4
-10^8 <= points[i][j] <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/line-reflection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def isReflected(self, points) -> bool:
        """
        group the points that got the same y-axis together
        """
        def check(lst, num):
            left, right = 0, len(lst)-1
            while left <= right:
                if num - lst[left] != lst[right] - num:
                    return False
                left += 1
                right -= 1
            return True

        sum_x = 0
        points_set = set(tuple(p) for p in points)
        y_dict = defaultdict(list)
        for i,j in points_set:
            y_dict[j].append(i)
            sum_x += i
        avg_x = sum_x/len(points_set)
        # print(avg_x)
        for key, lst in y_dict.items():
            y_dict[key] = sorted(lst)
            if not check(y_dict[key], avg_x):
                return False
        return True


from collections import defaultdict
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        ydict = defaultdict(set)
        minX = float('inf')
        maxX = float('-inf')
        for x,y in points:
            ydict[y].add(x)
            minX = min(minX, x)
            maxX = max(maxX, x)
        axis = (minX + maxX) / 2
        for vals in ydict.values():
            for x in vals:
                if 2 * axis - x not in vals:
                    return False
        return True


S = Solution()
points = [[1,1],[-1,1]]
print(S.isReflected(points))
points = [[1,1],[-1,-1]]
print(S.isReflected(points))
points = [[0,0],[1,0],[3,0]]
print(S.isReflected(points))
points = [[-16,0],[16,0],[16,0]]
print(S.isReflected(points))
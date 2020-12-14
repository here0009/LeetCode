"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""


from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        wrong answer
        """
        res = []
        stack = []
        for left, right, height in buildings:
            if not stack:
                res.append([left, height])
                stack.append([right, height])
                continue
            if left > stack[-1][0]:
                res.append([stack[-1][0], 0])
                stack = []
                res.append([left, height])
            if height > stack[-1][1]:
                res.append([left, height])
                stack.append([right, height])


from collections import defaultdict
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        use a line  parallel y axis to slide along x-axis. 
        """
        ys_set = set()
        xs_dict = defaultdict(list)
        for x1, x2, y in buildings:
            xs_dict[x1].append((y, 1))  # 1 for begin, -1 for end
            xs_dict[x2].append((y, -1))
            ys_set.add(y)
        ys = sorted(list(ys_set))
        len_y = len(ys)
        y_index = {v: i for i, v in enumerate(ys)}
        counts = [0] * len_y
        x_keys = sorted(xs_dict.keys())
        # print(ys, xs, y_index)
        res = []
        for x in x_keys:
            lst = xs_dict[x]
            for y, sign in lst:
                counts[y_index[y]] += sign
            # print(x, y, sign)
            # print([(v, counts[i]) for v,i in y_index.items()])
            for j in range(len_y - 1, -1, -1):
                if counts[j] > 0:
                    if not res or ys[j] != res[-1][1]:
                        res.append([x, ys[j]])
                    break
            else:
                res.append([x, 0])
        return res


from collections import defaultdict, Counter
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        use a line  parallel y axis to slide along x-axis. 
        """
        xs_dict = defaultdict(list)
        for x1, x2, y in buildings:
            xs_dict[x1].append((y, 1))  # 1 for begin, -1 for end
            xs_dict[x2].append((y, -1))

        counts = Counter()
        x_keys = sorted(xs_dict.keys())
        # print(x_keys, xs_dict)
        pq = []
        res = []
        for x in x_keys:
            lst = xs_dict[x]
            for y, sign in lst:
                counts[y] += sign
                if counts[y] == 1:
                    heapq.heappush(pq, -y)
            # print(x, lst, pq, counts)
            while pq and counts[-pq[0]] == 0:
                heapq.heappop(pq)
            if not pq:
                res.append([x, 0])
            else:
                if not res or -pq[0] != res[-1][1]:
                    res.append([x, -pq[0]])
        return res


from collections import defaultdict, Counter
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        y_line = [(x1, -y, x2) for x1, x2, y in buildings]  # if the two building got same x, we enter the one with max y first.
        y_line.extend([(x2, 0, 0) for _, x2, _ in buildings])
        res = [[0, 0]]
        y_line.sort()
        heights = [(0, float('inf'))]  # y and x
        # print(y_line)
        for x1, y, x2 in y_line:
            # print(x1, x2, y, heights)
            while heights[0][1] <= x1:  # lines before, the right line will pop the left line
                heapq.heappop(heights)
            if y < 0: # the right line do not enter to heap
                heapq.heappush(heights, (y, x2))
            if -heights[0][0] != res[-1][1]:
                res.append([x1, -heights[0][0]])
        return res[1:]


S = Solution()
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(S.getSkyline(buildings))

buildings = [[0,2,3],[2,5,3]]
print(S.getSkyline(buildings))
# Output
# [[0,3],[2,0],[2,3],[5,0]]
# Expected
# [[0,3],[5,0]]
"""
On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

 
Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:

Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:
After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum height of any square is 2.

After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__ -------------- The maximum height of any square is 5. The larger square stays on top of the smaller square despite where its center of gravity is, because squares are infinitely sticky on their bottom edge.

After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a -------------- The maximum height of any square is still 5. Thus, we return an answer of [2, 5, 5].

 

 
Example 2:

Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
 

Note:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
"""




class Solution(object):


    def fallingSquares(self, positions):
        # coords = set()
        # for left, size in positions:
        #     coords.add(left)
        #     coords.add(left + size - 1)
        # index = {x: i for i, x in enumerate(sorted(coords))}

        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans


from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        we use axis and heights to record the postion of the squares
        for a square, we record it as [left_index, heights], [right_index, pre_heights]
        left_index is where the square beigin, right_index is where the square end
        e.g. axis and heights were both initialized as [0] and [0].
        insert a square [2, 3], [2, 3] and [5, 0] were inserted. then axis is [0, 2, 5], heights is [0, 3, 0]
        then 
        """
        axis = [0]
        heights = [0]
        res = []
        max_h = 0
        for left, side in positions:
            right = left + side
            left_idx = bisect_right(axis, left)   # axis[left_idx] > left, and axis[left_idx - 1] <= left, because positions[i][0] >= 1, so left_idx - 1 is at least 0
            right_idx = bisect_left(axis, right)  # right_idx is the pos this square can not reach
            # print(left_idx, right_idx, h, left, side)
            h = max(heights[left_idx - 1: right_idx] or [0]) + side
            max_h = max(max_h, h)
            res.append(max_h)
            axis[left_idx: right_idx] = [left, right]
            heights[left_idx: right_idx] = [h, heights[right_idx - 1]]
        return res

from typing import List
from bisect import bisect_left, bisect_right
class Solution_1:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = dict()
        res = []
        total_max = 0
        for left, side_length in positions:
            right = left + side_length - 1
            lst = [v for k, v in heights.items() if not (k[1] < left or k[0] > right)]
            hmax = max(lst) if lst else 0
            hmax += side_length
            heights[(left, right)] = hmax
            total_max = max(total_max, hmax)
            res.append(total_max)
        return res


S = Solution()
positions = [[1, 2], [2, 3], [6, 1]]
print(S.fallingSquares(positions))
positions = [[100, 100], [200, 100]]
print(S.fallingSquares(positions))
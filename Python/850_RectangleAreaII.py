"""
We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""

# https://leetcode.com/problems/rectangle-area-ii/discuss/137914/JavaC%2B%2BPython-Discretization-and-O(NlogN)
# https://leetcode.com/problems/rectangle-area-ii/solution/
# https://leetcode.com/problems/rectangle-area-ii/discuss/906751/Python-NlogN

from typing import List
# from collections import defaultdict

# ==================================================================
class Solution:
    """
    try segement tree later
    """
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ys = []
        xs = set()
        for x1, y1, x2, y2 in rectangles:
            ys.append((y1, x1, x2, 1))
            ys.append((y2, x1, x2, -1))
            xs |= set([x1, x2])
        ys.sort()
        xs = sorted(list(xs))
        len_x = len(xs)
        x_dict = {v: i for i, v in enumerate(xs)}
        counts = [0] * len_x
        pre_y = None
        len_y = len(ys)
        res = 0

        M = 10**9 + 7
        # print(xs, ys, x_dict, counts)
        for i in range(len_y):
            curr_y, x1, x2, flag = ys[i]
            if pre_y is not None and curr_y != pre_y:
                x_sum = sum(xs[_i + 1] - xs[_i] for _i in range(len_x - 1) if counts[_i] > 0)
                res = (res + (curr_y - pre_y) * x_sum) % M
            for _i in range(x_dict[x1], x_dict[x2]):
                counts[_i] += flag
            # print(ys[i], counts, res)
            pre_y = curr_y
        return res



# ==================================================================
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def query(active):
            result = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                result += max(0, x2 - cur)
                cur = max(cur, x2)
            return result

        endpoints = []
        for x1, y1, x2, y2 in rectangles:
            endpoints.append((y1, False, x1, x2))
            endpoints.append((y2, True, x1, x2))
        endpoints.sort()

        result = 0
        active = []
        cur_y = endpoints[0][0]

        for y, is_closed, x1, x2 in endpoints:
            result += query(active) * (y - cur_y)
            if not is_closed:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))

            cur_y = y

        return result % (10**9 + 7)


# ==================================================================
# wrong answer
class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0
        self.total = 0


class Solution:
    def _bulid(self, left, right):
        node = SegmentTreeNode(self.xs[left], self.xs[right])
        if left == right:
            return node

        mid = (left+right)//2
        node.left = self._bulid(left, mid)
        node.right = self._bulid(mid + 1, right)
        return node
    
    def _update(self, node, i, j, flag):
        if i >= j:
            return 0
        if node.start == i and node.end == j:
            node.count += flag
        else:
            mid = (i + j) // 2
            self._update(node.left, i, mid, flag)
            self._update(node.right, mid, j, flag)

        if node.count > 0:
            node.total = self.xs[node.high] - self.xs[node.low]
        else:
            node.total = node.left.total + node.right.total

        return self.total


    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        lines = []
        xs = set()
        for x1, y1, x2, y2 in rectangles:
            lines.append((y1, x1, x2, 1))
            lines.append((y2, x1, x2, -1))
            xs |= set([x1, x2])
        lines.sort()
        self.xs = sorted(list(xs))
        x_dict = {v: i for i, v in enumerate(xs)}
        root = self._bulid(0, len(x) - 1)
        pre_y = None
        len_y = len(lines)
        res = 0
        x_sum = 0
        M = 10**9 + 7
        for i in range(len_y):
            curr_y, x1, x2, flag = lines[i]
            if pre_y is not None and curr_y != pre_y:
                res = (res + (curr_y - pre_y) * x_sum) % M
            x_sum = self._update(root, x_dict[x1], x_dict[x2], flag)
            pre_y = curr_y
        return res

# https://leetcode.com/problems/rectangle-area-ii/solution/
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = 0
        self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total


class Solution_1(object):
    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)

# try to not use global variables 
# ==============================================================
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.count = 0
        self.left = None
        self.right = None


class Solution:
    def bulid(self, start, end):
        node = Node(start, end)
        if start <= end - 1:
            return node
        mid = (start + end) // 2
        node.left = self.bulid(start, mid)
        node.right = self.bulid(mid, end)
        return node

    def update(self, node, i, j, val):
        # print(node.start, node.end, i, j, val, node.count, node.total)
        if i >= j:
            return 0
        if node.start <= i and node.end <= j:
            node.count += val
        else:
            mid = (node.start + node.end) // 2
            if node.left:
                self.update(node.left, i, min(mid, j), val)
            if node.right:
                self.update(node.right, max(mid, i), j, val)

        if node.count > 0:
            node.total = self.xs[node.end] - self.xs[node.start]
        else:
            node.total += node.left.total + node.right.total
            # if node.right:
            #     node.total += 
        return node.total

    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        x_set = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            x_set.add(x1)
            x_set.add(x2)
        events.sort()

        self.xs = sorted(list(x_set))
        x_dict = {x: i for i, x in enumerate(self.xs)}

        root = self.bulid(0, len(self.xs) - 1)
        print('root', root.count, root.total, root.start, root.end)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            print(y, typ, x1, x2, cur_x_sum)
            print(ans)
            cur_x_sum = self.update(root, x_dict[x1], x_dict[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)

# ============================================================
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = 0
        self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right


class Solution:
    def update(self, node, i, j, val):
        if i >= j:
            return 0
        if node.start == i and node.end == j:
            node.count += val
        else:
            self.update(node.left, i, min(node.mid, j), val)
            self.update(node.right, max(node.mid, i), j, val)

        if node.count > 0:
            node.total = self.xs[node.end] - self.xs[node.start]
        else:
            node.total = node.left.total + node.right.total

        return node.total

    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        x_set = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            x_set.add(x1)
            x_set.add(x2)
        events.sort()

        self.xs = sorted(list(x_set))
        x_dict = {x: i for i, x in enumerate(self.xs)}

        root = Node(0, len(self.xs) - 1)
        # print('root', root.count, root.total, root.start, root.end)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            # print(y, typ, x1, x2, cur_x_sum)
            # print(ans)
            cur_x_sum = self.update(root, x_dict[x1], x_dict[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)

S = Solution()
rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
print(S.rectangleArea(rectangles))
rectangles = [[0,0,1000000000,1000000000]]
print(S.rectangleArea(rectangles))

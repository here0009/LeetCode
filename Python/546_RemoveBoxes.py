"""
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
 

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
"""


from typing import List, Tuple
from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        TLE: 20 / 61 test cases passed.
        """
        @lru_cache(None)
        def dp(status: Tuple[int]) -> int:
            """
            return the max score we can get of the given status
            """
            pre_i = 0
            res = 0
            for i, v in enumerate(status):
                if v != status[pre_i]:
                    k = i - pre_i
                    status2 = status[:pre_i] + status[i:]
                    res = max(res, k * k + dp(status2))
                    pre_i = i
            # print(status, res)s
            return res
        boxes.append(None)
        return dp(tuple(boxes))


from typing import List, Tuple
from functools import lru_cache
from collections import Counter
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(status: Tuple[int]) -> int:
            """
            return the max score we can get of the given status
            try to eliminate the keys that counts == 1
            """
            pre_i = 0
            res = 0
            for i, v in enumerate(status):
                if v != status[pre_i]:
                    k = i - pre_i
                    status2 = status[:pre_i] + status[i:]
                    res = max(res, k * k + dp(status2))
                    pre_i = i
            # print(status, res)s
            return res

        counts = Counter(boxes)
        print(counts)
        boxes.append(None)
        pre_i = 0
        lst = []
        for i, v in enumerate(boxes):
            if v != boxes[pre_i]:
                lst.append((boxes[pre_i], i - pre_i))
                pre_i = i
    
        print(lst)
        return
        # dp(tuple(boxes))


from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def remove(status):
            """
            remove the boxes only in one continous sequence
            """
            counts = Counter(status)
            res = 0
            s2 = []
            pre_i = 0
            for i, v in enumerate(status):
                pre_v = status[pre_i]
                if v != pre_v:
                    k = i - pre_i
                    if k == counts[pre_v]:
                        res += k * k
                    else:
                        s2.extend(k * [pre_v])
            return res, tuple(s2)


        @lru_cache(None)
        def dp(status: Tuple[int]) -> int:
            """
            return the max score we can get of the given status
            """
            res, status = remove(status)
            pre_i = 0
            for i, v in enumerate(status):
                if v != status[pre_i]:
                    k = i - pre_i
                    status2 = status[:pre_i] + status[i:]
                    res = max(res, k * k + dp(status2))
                    pre_i = i
            # print(status, res)s
            return res
        boxes.append(None)
        return dp(tuple(boxes))


from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            """
            k is the counts previous boxes[i] that has not been removed, we can remove them now or later
            """
            if i > j:
                return 0
            i2 = i + 1
            while i2 <= j and boxes[i2] == boxes[i]:
                i2 += 1
            k += i2 - i
            res = dp(i2, j, 0) + k**2
            for x in range(i2 + 1, j + 1):
                if boxes[x] == boxes[i]:
                    res = max(res, dp(i2, x - 1, 0) + dp(x, j, k))
            return res

        return dp(0, len(boxes) - 1, 0)

S = Solution()
boxes = [1,3,2,2,2,3,4,3,1]
print(S.removeBoxes(boxes))
boxes =[3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]
print(S.removeBoxes(boxes))